from flask import Flask, render_template, request
from PIL import Image
import matplotlib.pyplot as plt
from model.predict import predict_image
from db.database import Database
from minio import Minio
import config as cf
app = Flask(__name__)


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")


@app.route("/about")
def about_page():
    return "Please subscribe  Artificial Intelligence Hub..!!!"


@app.route("/submit", methods=['GET', 'POST'])
def get_output():
    try:
        if request.method == 'POST':
            img = request.files['my_image']
            img_path = "static/" + img.filename
            img.save(img_path)
            p = predict_image(img_path)
            minio_client = Minio(cf.minio_url,
                                 access_key=cf.minio_access,
                                 secret_key=cf.minio_secret,
                                 secure=False,
                                 )
            minio_client.fput_object('image', img.filename, img_path)
            db = Database()
            query = "insert into label_image (img_path, img_label) values (%s,%s)"
            value = ('image/' + img.filename, p)
            db.insert_db(query, value)
            return render_template("index.html", prediction=p, img_path=img_path)
    except Exception as exc:
        print(exc)
        return render_template("index.html", prediction="Không phân biệt được ảnh",
                               img_path="static/happysun.jpg")


if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True)
