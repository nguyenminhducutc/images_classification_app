## Project: Xây dựng website cho mô hình phân loại AI (phần backend kết nối với mô hình  AI)

## Công nghệ sử dụng: 
- Flask API
- Minio Storage
- Postgresql

## Cài đặt môi trường:
* `python -m pip install --upgrade pip`
* `python -m pip install --user virtualenv`
* `python -m venv envs`
* `Set-ExecutionPolicy Unrestricted -Scope Process`
* `envs/Scripts/activate`
* `pip install -r requirements.txt`

## Cài đặt Minio Storage:
- Hướng dẫn cài đặt Minio Storage: https://hub.docker.com/r/minio/minio
- Minio là một server lưu trữ đối tượng dạng phân tán với hiệu năng cao
- Đặc biệt là Minio cung cấp các api làm việc giống như Amazon S3, do đó ta có thể upload, download file, lấy link… 
qua API một cách đơn giản
- Dữ liệu sẽ được đẩy lên lưu trữ tại Minio Storage (cài đặt bằng docker) đồng thời insert vào bảng label_image trong database 
- Chạy docker bằng lệnh `docker-compose up -d`
- Cổng truy cập Minio:
      * "9000:9000"
      * "9001:9001"

## Cài đặt database:
B1: Cài đặt database postgresql cho ubuntu 20.04
  * sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
  * sudo wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
  * sudo apt-get update
  * sudo apt-get -y install postgresql-14
  * Tham khảo: https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart

Hướng dẫn cài đặt cho windows: https://www.postgresql.org/download/windows/

B2: 
- Tạo database: `create database ai_images;`
- Tạo bảng: `create table label_image(
                 ind int GENERATED ALWAYS AS IDENTITY,
                 img_path varchar(50),
                 img_label varchar(50),
                 update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
             )`
 
## Cấu trúc project:
- Các thư mục
  * db: chứa class Database và các hàm xử lý database
  * model: mô hình AI
  * static: thư mục lưu trữ
  * templates: chứa file html

- Các file:
  * .env: chứa các biến môi trường chung cho toàn project
  * app.py: file làm việc chính chứa các API
  * config.py: tệp cấu hình, cho phép chỉnh sửa thông tin cần thiết
  * docker-compose.yaml: tạo và chạy ứng dụng Minio Storage
  * requirements.txt: chúa các thư viện được sử dụng cho project

## Chạy project 
- Dùng câu lệnh `python.\app.py`
- Cổng truy cập API: localhost:5000
- Click Choose File => upload ảnh vật thể cần nhận dạng
- Ấn submit => trả về kết quả phân loại vật thể 







