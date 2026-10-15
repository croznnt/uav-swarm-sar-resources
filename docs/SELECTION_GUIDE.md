# Chọn công cụ mô phỏng UAV bầy đàn

## Chọn mức mô hình trước

| Câu hỏi nghiên cứu | Điểm bắt đầu | Phần cần kiểm tra |
| :--- | :--- | :--- |
| Làm sao tìm người trôi dạt nhanh hơn? | DSSE | Mô hình dòng chảy, xác suất phát hiện, tiêu chuẩn kết thúc |
| Chia vùng tìm kiếm dưới giới hạn pin và liên lạc? | SwarmSAR | Mức hoàn thiện, tính lặp lại, cách tính pin và truyền tin |
| Nhiều UAV phối hợp tìm mục tiêu qua ảnh? | CTS visual drone swarm | Dữ liệu ảnh, giả định quan sát và phụ thuộc phiên bản |
| Chính sách điều khiển có bay ổn định? | gym-pybullet-drones, QuadSwarm | Động lực học, tần số điều khiển và mô hình va chạm |
| Kiểm tra thuật toán bầy đàn bằng MATLAB? | SwarmLab, SwarmFly | Toolbox, phiên bản MATLAB và phạm vi mô hình |
| Cần autopilot và cảm biến 3D? | XTDrone, Pegasus | Ma trận ROS, PX4, Gazebo hoặc Isaac Sim |
| Chuẩn bị thí nghiệm Crazyflie? | Crazyswarm2 | Backend mô phỏng, định vị và cấu hình đội hình |
| Nghiên cứu mạng cho cứu nạn? | uav-swarm-sim | Mô hình kênh truyền, độ trễ, mất gói và tích hợp NS-3 |

## Môi trường làm việc

Tạo môi trường riêng cho từng dự án. Không dùng chung một môi trường Python cho toàn bộ danh mục. Với ROS, Gazebo và PX4, chọn hệ điều hành và bản phân phối theo tài liệu của đúng nhánh nguồn. Trên Windows, đánh giá WSL2 hoặc máy Linux nếu upstream yêu cầu Linux; GPU và hiển thị cần kiểm tra riêng.

Pegasus phụ thuộc NVIDIA Isaac Sim, cần kiểm tra GPU, driver, giấy phép và phiên bản tương thích trước khi tải. SwarmLab yêu cầu MATLAB cùng Statistics and Machine Learning Toolbox theo README upstream. Các yêu cầu của SwarmFly cần đọc riêng, không suy ra từ SwarmLab.

## Trình tự triển khai đề xuất

1. Chọn một công cụ và ghi commit nguồn, hệ điều hành, phiên bản runtime và giấy phép.
2. Chạy ví dụ tối thiểu theo upstream, lưu log và ảnh kết quả.
3. Xác định UAV quan sát được gì và thông tin nào chỉ bộ đánh giá được biết.
4. Tạo baseline chia vùng, đo độ phủ và thời gian phát hiện.
5. Thêm pin, liên lạc và cảm biến từng phần để xác định nguyên nhân thay đổi kết quả.
6. Chỉ chuyển sang mô phỏng vật lý khi câu hỏi nghiên cứu cần xét động lực học hoặc cảm biến.

Môi trường tìm kiếm trên lưới không xác nhận khả năng bay của bộ điều khiển. Mô phỏng nhiều UAV cũng không tự cung cấp phân công nhiệm vụ, bản đồ xác suất hay mô hình nạn nhân.
