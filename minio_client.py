from minio import Minio
from datetime import timedelta
import config as cf

if __name__ == '__main__':
    minio_client = Minio(cf.minio_url,
                         access_key=cf.minio_access,
                         secret_key=cf.minio_secret,
                         secure=False,
                         )
    minio_client.fput_object('image', '7.jpg', 'D:/Computer-Vision-problem/image_classification/static/7.jpg')
