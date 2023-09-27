from db.database import Database

db = Database()
query = "insert into label_image (img_path, img_label) values (%s,%s)"
value = ("abc", "cho")
db.insert_db(query, value)
