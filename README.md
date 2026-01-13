## Hệ thống bài tập & tài liệu môn Phát triển Hệ thống Thông minh

Repository này lưu toàn bộ bài tập, case study và tài liệu tham khảo trong học phần **Phát triển Hệ thống Thông minh / Machine Learning & Deep Learning**.

### Nội dung chính

- **assignment_1 → assignment_6**: Các bài tập về:
  - **Machine Learning cơ bản** (hồi quy, phân lớp, đánh giá mô hình, xử lý dữ liệu dạng bảng).
  - **Deep Learning** với `tensorflow` / `keras` (mạng neuron, CNN, RNN, v.v.).
  - Ứng dụng trên nhiều bộ dữ liệu: `BostonHousing`, `titanic`, `diabetes`, dữ liệu review, churn, thời tiết, v.v.
- **cuoiKi-onTap**: Các case study ôn tập cuối kỳ (ảnh, âm thanh, văn bản, v.v.) và mô hình đã huấn luyện.
- **BTL_Chapter4**, `ktra1`, `ktra2`, `ktra3`: Bài thực hành/bài kiểm tra theo từng chương, gồm notebook và dữ liệu đi kèm.
- **duBao.py**: Mã Python dự đoán (prediction) minh họa cách sử dụng mô hình đã huấn luyện.

Các file `*.ipynb` là notebook Jupyter minh họa toàn bộ quy trình: chuẩn bị dữ liệu, xây dựng mô hình, huấn luyện, đánh giá và lưu mô hình.

### Yêu cầu môi trường

Project dùng Python (khuyến nghị **Python 3.9+**).

Các thư viện chính (xem chi tiết trong `requirements.txt`):

- `tensorflow`, `keras`
- `numpy`, `pandas`, `scikit-learn`
- `matplotlib`, `seaborn`
- `Pillow`
- `librosa`
- `transformers`
- `streamlit`
- `joblib`

### Cài đặt

1. **Clone hoặc copy project về máy**

   - Nếu dùng Git:

   ```bash
   git clone <link_repo_cua_ban>
   cd IntSys
   ```

   - Nếu tải ZIP: giải nén thư mục `IntSys` về máy.

2. **(Khuyến nghị) Tạo môi trường ảo**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Cài đặt thư viện**

   ```bash
   pip install -r requirements.txt
   ```

### Chạy notebook (.ipynb)

1. Cài Jupyter nếu chưa có:

   ```bash
   pip install jupyter
   ```

2. Chạy Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Mở các file trong từng thư mục, ví dụ:
   - `assignment_1/B22DCCN476_Đỗ_Ngọc_Lâm.ipynb`
   - `assignment_2/Đỗ_Ngọc_Lâm_B22DCCN476.ipynb`
   - `assignment_3/assign_3_LamDN-B22DCCN476.ipynb`
   - `assignment_4/assign4_03cq.01_lamdn.ipynb`, `assign4.2_03cq.01_lamdn.ipynb`
   - `assignment_5/assign5_03cq.01_lamdn.ipynb`
   - `assignment_6/assign6.v1_03cq.01_lamdn.ipynb`

   Sau đó chạy lần lượt các ô (cell) để xem lại toàn bộ pipeline xử lý.

### Chạy script Python (ví dụ `duBao.py`)

1. Đảm bảo đã:
   - Kích hoạt môi trường ảo (nếu dùng).
   - Cài đặt đúng `requirements.txt`.

2. Chạy script:

   ```bash
   python duBao.py
   ```

   Tùy nội dung file, script có thể:
   - Tải dữ liệu,
   - Load mô hình đã huấn luyện (`.pkl`, `.keras`, `.h5`),
   - Thực hiện dự đoán và in kết quả.

### Gợi ý cấu trúc thư mục

- **assignment_x**: Mỗi thư mục là một bài tập/bài lab riêng, gồm:
  - Notebook `.ipynb`
  - File đề bài `.pdf` / `.docx`
  - Dữ liệu `.csv`, `.jpg`, `.wav`, ...
- **cuoiKi-onTap**: Tập hợp các case study lớn với dữ liệu thực tế (ảnh, audio, text) và mô hình đã train.
- **flowers_dataset_5_labels**, `ktra1`, `ktra2`, `ktra3`, `BTL_Chapter4`: Bộ dữ liệu và notebook phục vụ bài tập, kiểm tra, bài tiểu luận.

### Góp ý & chỉnh sửa

README này mang tính **tổng quan**. Bạn có thể:

- Bổ sung mô tả chi tiết cho từng case study / assignment.
- Ghi rõ cách chạy thêm nếu có app `streamlit` hoặc script nào khác.

Nếu bạn cho mình biết file nào là sản phẩm chính (ví dụ app demo, mô hình quan trọng nhất), mình có thể chỉnh lại README chi tiết hơn cho phần đó. 


