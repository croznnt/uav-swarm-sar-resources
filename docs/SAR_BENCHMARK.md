# Đề xuất benchmark tìm kiếm cứu nạn

Đây là thiết kế thí nghiệm, chưa có kết quả thực nghiệm. Tách phát hiện, xác nhận vị trí và cứu hộ thực tế thành các sự kiện khác nhau. Phát hiện mục tiêu trong mô phỏng không đồng nghĩa hoàn thành cứu hộ.

## Kịch bản

| Mã | Tình huống | Biến số | Phép đo chính |
| :--- | :--- | :--- | :--- |
| S01 | Tìm người trên vùng đất 2D | Số UAV là 2, 4, 8 và 16 | Thời gian phát hiện đầu tiên, tỷ lệ mục tiêu tìm thấy |
| S02 | Tìm người trôi dạt trên biển | Dòng chảy, nhiễu vị trí ban đầu, độ tin cậy prior | Xác suất tìm thấy theo thời gian, độ phủ có trọng số |
| S03 | Tìm kiếm khi liên lạc hạn chế | Tầm truyền, độ trễ, mất gói | Phát hiện trùng lặp, độ trễ hợp nhất thông tin |
| S04 | Nhiệm vụ có giới hạn pin | Dung lượng pin, vị trí trạm, dự trữ quay về | Số mục tiêu trên đơn vị năng lượng, UAV cạn pin |
| S05 | Tìm kiếm có vật cản và che khuất | Mật độ vật cản, tầm nhìn | Va chạm, vi phạm khoảng cách, mục tiêu bị bỏ sót |

## Baseline và tính công bằng

1. Random walk làm mốc đơn giản, với seed cố định.
2. Chia vùng bằng nhau và quét zíc zắc làm baseline có cấu trúc.
3. Ưu tiên ô có xác suất mục tiêu cao, chỉ dùng thông tin tác tử thực sự được phép biết.
4. Chính sách thích nghi hoặc MARL dùng cùng bản đồ, cảm biến, ngân sách thời gian và năng lượng.

Chạy thử 30 seed cho mỗi cấu hình như một điểm bắt đầu, rồi đánh giá độ bất định để quyết định có cần thêm lần chạy. Ghép cùng seed giữa các thuật toán. Báo cáo median và phân vị, hoặc trung bình kèm khoảng tin cậy với cách tính đã công bố. Không loại các lần thất bại khỏi thống kê.

## Quy ước phép đo

Thời gian phát hiện đầu tiên tính từ lúc bắt đầu nhiệm vụ đến khi có phát hiện hợp lệ. Nếu không tìm thấy, ghi nhận là chưa phát hiện khi hết ngân sách, không gán bằng không. Tỷ lệ phát hiện bằng số mục tiêu duy nhất tìm thấy chia tổng mục tiêu. Độ phủ có trọng số bằng tổng xác suất prior của các ô đã quan sát chia tổng xác suất prior ban đầu; ghi rõ cách xử lý prior động trên biển.

Nếu simulator không có mô hình năng lượng hoặc va chạm, ghi phép đo đó là không áp dụng. Không so thời gian mô phỏng với thời gian máy chạy. Công bố riêng thời gian nhiệm vụ, tốc độ mô phỏng, phần cứng và số tác tử.

## Dữ liệu tối thiểu cho mỗi lần chạy

```json
{
  "scenario": "S01",
  "simulator_repo": "owner/repository",
  "simulator_commit": "record_exact_commit",
  "policy": "partitioned_lawnmower",
  "seed": 42,
  "num_uavs": 4,
  "target_count": 5,
  "duration_seconds": 600,
  "targets_found": null,
  "first_detection_seconds": null,
  "energy_model": null,
  "collision_count": null
}
```

Các giá trị null là chưa đo, không phải kết quả. Lưu thêm cấu hình cảm biến, pin, liên lạc, tọa độ, đơn vị, vị trí khởi tạo, điều kiện dừng, log quỹ đạo và phiên bản mã chính sách. Không so trực tiếp hai công cụ khi khác mô hình quan sát hoặc ngân sách nhiệm vụ mà chưa giải thích khác biệt.
