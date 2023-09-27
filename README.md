## Project: Xây dựng website cho mô hình phân loại AI (phần backend kết nối với mô hình  AI)

## Công nghệ sử dụng: Flask API, Minio Storage, Postgresql

## Cài đặt môi trường:
- python -m pip install --upgrade pip
- python -m pip install --user virtualenv
- python -m venv envs
- Set-ExecutionPolicy Unrestricted -Scope Process
- envs/Scripts/activate

## Cài đặt database:
- Sử dụng postgreSQL
- Tạo database: `create database ai_images;`
- Tạo bảng: `create table label_image(
                 ind int GENERATED ALWAYS AS IDENTITY,
                 img_path varchar(50),
                 img_label varchar(50),
                 update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
             )`
## Tạo file requirements: `pip3 freeze > requirements.txt` 

## Cấu trúc project:
- Các thư mục
db: chứa class Database và các hàm xử lý database
model: mô hình AI
static: thư mục lưu trữ
templates: chứa file html

- Các file:
.env: chứa các biến môi trường chung cho toàn project
app.py: file làm việc chính chứa các API
config.py: tệp cấu hình, cho phép chỉnh sửa thông tin cần thiết
docker-compose.yaml: tạo và chạy ứng dụng Minio Storage
requirements.txt: chúa các thư viện được sử dụng cho project

## Chạy project 
- Dùng câu lệnh `python.\app.py`
- Click Choose File => upload ảnh vật thể cần nhận dạng
- Ấn submit => trả về kết quả phân loại vật thể 

## Bật Minio Storage `docker-compose up -d`
- Minio là một server lưu trữ đối tượng dạng phân tán với hiệu năng cao
- Đặc biệt là MinIO cung cấp các api làm việc giống như Amazon S3, do đó ta có thể upload, download file, lấy link… 
qua API một cách đơn giản
- Dữ liệu sẽ được đẩy lên lưu trữ tại Minio Storage (cài đặt bằng docker) đồng thời insert vào bảng label_image trong database 






