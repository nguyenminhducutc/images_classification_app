## Project: Xây dựng website cho mô hình phân loại AI (phần backend kết nối với mô hình  AI)

## Công nghệ sử dụng: Flask API, Minio Storage, Postgresql

## Cấu trúc project:
db.database: chứa class Database và các hàm xử lý database
model: mô hình AI
static: thư mục lưu trữ
templates: chứa file html
app: file chính chứa các API 


## Database:
- Tạo database ai_images để insert dữ liệu 
- Tạo bảng label_image với các thông tin : ind, img_path, img_label, update_time

## Chạy file app.py, click Choose file, upload file, ấn submit test kết quả trả về
- Dữ liệu sẽ được đẩy lên lưu trữ tại Minio Storage (cài đặt bằng docker) đồng thời insert vào bảng label_image trong database 






