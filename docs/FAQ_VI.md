# 🙋‍♀️ Pixelle-Video - Câu Hỏi Thường Gặp

### Cách tích hợp luồng công việc (workflow) tùy chỉnh cục bộ?

Nếu bạn muốn tích hợp luồng công việc ComfyUI của riêng mình, vui lòng tuân theo các quy cách sau:

1.  **Chạy cục bộ trước**: Đảm bảo luồng công việc chạy đúng trong ComfyUI cục bộ của bạn.
2.  **Gán tham số**: Tìm node Text (CLIP Text Encode hoặc node nhập văn bản tương tự) nơi cần truyền prompt từ chương trình.
    -   Chỉnh sửa **Tiêu đề** của node đó.
    -   Đổi tiêu đề thành `$prompt.text!` hoặc `$prompt.value!` (tùy thuộc vào loại đầu vào node chấp nhận).
     <img src="https://github.com/user-attachments/assets/ddb1962c-9272-486f-84ab-8019c3fb5bf4" width="600" alt="Ví dụ gán tham số" />

    -   *Tham khảo: Xem cách chỉnh sửa các file JSON có sẵn trong thư mục `workflows/selfhost/`.*
3.  **Định dạng xuất**: Xuất luồng công việc đã chỉnh sửa ở **Định dạng API** (Save (API Format)).
4.  **Quy tắc đặt tên**: Đặt file JSON đã xuất vào thư mục `workflows/` với tiền tố sau:
    -   **Luồng hình ảnh**: Tiền tố phải là `image_` (ví dụ: `image_my_style.json`)
    -   **Luồng video**: Tiền tố phải là `video_`
    -   **Luồng TTS**: Tiền tố phải là `tts_`

### Cách debug luồng công việc RunningHub ở cục bộ?

Nếu bạn muốn thử nghiệm cục bộ các luồng công việc vốn dành cho RunningHub đám mây:

1.  **Lấy ID**: Mở file luồng công việc RunningHub và tìm ID.
2.  **Tải luồng**: Dán ID vào cuối URL RunningHub (ví dụ: https://www.runninghub.ai/workflow/1983513964837543938) để vào trang luồng công việc.
  <img src="https://github.com/user-attachments/assets/e5330b3a-5475-44f2-81e4-057d33fdf71b" width="600" alt="Ví dụ gán tham số" />


3.  **Tải về cục bộ**: Tải luồng công việc dưới dạng file JSON từ bàn làm việc.
4.  **Thử nghiệm cục bộ**: Kéo file đã tải vào canvas ComfyUI cục bộ để thử nghiệm và debug.

### Lỗi Thường Gặp và Giải Pháp

#### 1. Lỗi TTS (Chuyển Văn Bản Thành Giọng Nói)
-   **Nguyên nhân**: Edge-TTS mặc định gọi giao diện miễn phí của Microsoft, có thể thất bại thường xuyên do mạng không ổn định.
-   **Giải pháp**:
    -   Kiểm tra kết nối mạng của bạn.
    -   Khuyến nghị chuyển sang luồng **ComfyUI TTS** (chọn luồng có tiền tố `tts_`) để ổn định hơn.

#### 2. Lỗi LLM (Mô Hình Ngôn Ngữ Lớn)
-   **Các bước khắc phục**:
    1.  Kiểm tra **Base URL** có đúng không (đảm bảo không có khoảng trắng hoặc hậu tố sai).
    2.  Kiểm tra **API Key** có hợp lệ và còn số dư không.
    3.  Kiểm tra **Tên mô hình** có viết đúng không.
    -   *Mẹo: Vui lòng tham khảo tài liệu API chính thức của nhà cung cấp mô hình (ví dụ: OpenAI, DeepSeek, Alibaba Cloud, v.v.) để cấu hình chính xác.*

#### 3. Thông báo lỗi "Could not find a Chrome executable..."
-   **Nguyên nhân**: Hệ thống máy tính thiếu trình duyệt Chrome, gây ra lỗi cho các tính năng phụ thuộc vào trình duyệt.
-   **Giải pháp**: Vui lòng tải và cài đặt trình duyệt Google Chrome.

### Video đã tạo được lưu ở đâu?

Tất cả video đã tạo tự động được lưu trong thư mục `output/` bên trong thư mục dự án. Sau khi hoàn thành, giao diện sẽ hiển thị thời lượng video, kích thước file, số cảnh và liên kết tải xuống.

### Tài Nguyên Cộng Đồng

-   **Kho lưu trữ GitHub**: https://github.com/whitelotusvnmedia-stack/Pixelle-Video
-   **Báo lỗi**: Gửi lỗi hoặc yêu cầu tính năng qua GitHub Issues.
-   **Hỗ trợ cộng đồng**: Tham gia nhóm thảo luận để được trợ giúp và chia sẻ kinh nghiệm.
-   **Đóng góp**: Dự án theo giấy phép Apache 2.0, hoan nghênh mọi đóng góp.

💡 **Mẹo**: Nếu bạn không tìm thấy câu trả lời cần thiết trong FAQ này, vui lòng gửi issue trên GitHub hoặc tham gia thảo luận cộng đồng. Chúng tôi sẽ tiếp tục cập nhật FAQ này dựa trên phản hồi của người dùng!
