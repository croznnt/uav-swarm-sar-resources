# 🚁 UAV Swarm Simulation & Search and Rescue

Danh mục 11 dự án mô phỏng UAV bầy đàn và công cụ liên quan, ưu tiên tìm kiếm cứu nạn (SAR). Bao gồm Python, MATLAB, ROS, mô phỏng vật lý, học tăng cường nhiều tác tử và mạng liên lạc.

## 🎯 Bắt đầu theo mục tiêu

1. Tìm người gặp nạn trên biển: bắt đầu với DSSE, có môi trường tìm kiếm và phủ vùng gắn với mô hình trôi dạt.
2. Phối hợp tìm kiếm trên bản đồ 2D: khảo sát SwarmSAR, kiểm tra lại các tuyên bố hiệu năng trước khi chọn.
3. Tìm mục tiêu bằng thị giác: xem CTS visual drone swarm, phân biệt tìm mục tiêu với mô phỏng cứu nạn hoàn chỉnh.
4. Mô phỏng động lực học bằng Python: xem gym-pybullet-drones hoặc QuadSwarm.
5. Mô phỏng bầy đàn bằng MATLAB: bắt đầu với SwarmLab, xem thêm SwarmFly.
6. Kiểm tra điều khiển bay và nhiều phương tiện: xem XTDrone, Pegasus hoặc Crazyswarm2.
7. Liên lạc khẩn cấp: xem uav-swarm-sim để khảo sát mạng UAV.

## 📚 Danh mục

| Dự án | Nhóm | Nền tảng | Liên hệ SAR | Hồ sơ |
| :--- | :--- | :--- | :--- | :--- |
| [DSSE](https://github.com/capstone-insper/drone-swarm-search) | SAR | Python, PettingZoo, Pygame, OpenDrift | Có sẵn bài toán SAR trên biển. | [Chi tiết](repositories/capstone-insper__drone-swarm-search.md) |
| [SwarmSAR](https://github.com/AngusMcGlynn/SwarmSAR) | SAR | Python, Pygame | Có sẵn định hướng tìm kiếm cứu nạn. | [Chi tiết](repositories/AngusMcGlynn__SwarmSAR.md) |
| [CTS visual drone swarm](https://github.com/NTU-ICG/CTS-visual-drone-swarm) | Tìm mục tiêu | Mã nghiên cứu, mô phỏng thị giác, MARL | Tìm mục tiêu hợp tác, có thể phát triển cho SAR. | [Chi tiết](repositories/NTU-ICG__CTS-visual-drone-swarm.md) |
| [gym-pybullet-drones](https://github.com/learnsyslab/gym-pybullet-drones) | Nền tảng | Python, PyBullet, Gymnasium | Cần tự xây dựng nhiệm vụ SAR. | [Chi tiết](repositories/learnsyslab__gym-pybullet-drones.md) |
| [QuadSwarm](https://github.com/Zhehui-Huang/quad-swarm-rl) | Nền tảng | Python, học tăng cường, Sample Factory | Cần tự xây dựng nhiệm vụ SAR. | [Chi tiết](repositories/Zhehui-Huang__quad-swarm-rl.md) |
| [XTDrone](https://github.com/robin-shaun/XTDrone) | Nền tảng | ROS, PX4, Gazebo, Python, C++ | Nền tảng nhiều UAV để xây dựng kịch bản SAR. | [Chi tiết](repositories/robin-shaun__XTDrone.md) |
| [Pegasus Simulator](https://github.com/PegasusSimulator/PegasusSimulator) | Nền tảng | Python, NVIDIA Isaac Sim, PX4 | Nền tảng 3D để xây dựng kịch bản SAR. | [Chi tiết](repositories/PegasusSimulator__PegasusSimulator.md) |
| [Crazyswarm2](https://github.com/IMRCLab/crazyswarm2) | Nền tảng | ROS 2, Python, Crazyflie | Phù hợp thử nghiệm phối hợp quy mô phòng thí nghiệm. | [Chi tiết](repositories/IMRCLab__crazyswarm2.md) |
| [SwarmLab](https://github.com/lis-epfl/swarmlab) | Nền tảng | MATLAB | Cần tự xây dựng nhiệm vụ SAR. | [Chi tiết](repositories/lis-epfl__swarmlab.md) |
| [SwarmFly](https://github.com/abhishekphadke/SwarmFly) | Nền tảng | MATLAB, MATLAB GUI | Công cụ thiết kế thí nghiệm có thể mở rộng cho SAR. | [Chi tiết](repositories/abhishekphadke__SwarmFly.md) |
| [UAV Swarm Network Simulator](https://github.com/pabloramesc/uav-swarm-sim) | Mạng | Python, NS-3, C++ | Liên quan liên lạc khẩn cấp hỗ trợ cứu nạn. | [Chi tiết](repositories/pabloramesc__uav-swarm-sim.md) |

## 🔎 Cách đọc danh mục

Nhóm SAR có bài toán tìm kiếm cứu nạn trong tài liệu dự án. Nhóm tìm mục tiêu tập trung vào tìm kiếm hợp tác. Nhóm nền tảng cung cấp mô phỏng hoặc điều khiển, cần bổ sung nhiệm vụ SAR. Nhóm mạng phục vụ nghiên cứu liên lạc hỗ trợ cứu nạn.

Các nhận xét về mức độ phù hợp là đánh giá biên tập từ nguồn chính thức, không phải kết quả so sánh thực nghiệm. Ngày đọc nguồn: 15 tháng 10 năm 2026. Chưa cài đặt, chạy thử hoặc xác nhận hiệu năng của các dự án bên thứ ba. Không dùng số sao để thay cho chất lượng hoặc độ phù hợp. Danh mục không khẳng định các dự án tương thích với nhau.

## 🧪 Lộ trình nghiên cứu

Đọc [hướng dẫn chọn công cụ](docs/SELECTION_GUIDE.md), sau đó dùng [thiết kế benchmark SAR](docs/SAR_BENCHMARK.md) để xây dựng phép so sánh có thể lặp lại. Bắt đầu với chia vùng và quét zíc zắc, rồi mới thêm chính sách thích nghi hoặc học tăng cường.

## 🛠️ Dữ liệu và bảo trì

[catalog.json](catalog.json) là nguồn dữ liệu để chỉnh sửa. [catalog.csv](catalog.csv) phục vụ lọc bằng bảng tính. Mỗi hồ sơ có nguồn, khả năng, phần cần bổ sung, bài tập và giới hạn.

Từ thư mục repo, chạy bằng Python tiêu chuẩn:

```console
python scripts/build_catalog.py
```

Lệnh sinh lại README, CSV và hồ sơ từ JSON cùng [mẫu README](docs/README.template.md). Không cài thêm thư viện. Khi cập nhật nguồn, sửa ngày kiểm tra của từng mục và ghi rõ mức kiểm chứng. Không ghi kết quả benchmark khi chưa có log, cấu hình và commit nguồn.

Đóng góp theo [CONTRIBUTING.md](CONTRIBUTING.md). Repo này chứa mô tả và liên kết, không phân phối mã nguồn của các dự án được liệt kê. Giấy phép từng công cụ cần kiểm tra tại upstream và đúng commit sử dụng.
