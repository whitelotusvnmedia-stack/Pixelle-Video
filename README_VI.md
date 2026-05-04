<h1 align="center">🎬 Pixelle-Video — Công Cụ Tạo Video Ngắn AI Tự Động</h1>

<p align="center"><a href="README_EN.md">English</a> | <a href="README.md">中文</a> | <b>Tiếng Việt</b></p>

<p align="center">
  <a href="https://github.com/whitelotusvnmedia-stack/Pixelle-Video/releases" target="_blank"><img src="https://img.shields.io/badge/📦 Windows-50C878" alt="Gói Windows"></a>
  <a href="https://github.com/whitelotusvnmedia-stack/Pixelle-Video/stargazers"><img src="https://img.shields.io/github/stars/whitelotusvnmedia-stack/Pixelle-Video.svg" alt="Stars"></a>
  <a href="https://github.com/whitelotusvnmedia-stack/Pixelle-Video/issues"><img src="https://img.shields.io/github/issues/whitelotusvnmedia-stack/Pixelle-Video.svg" alt="Issues"></a>
  <a href="https://github.com/whitelotusvnmedia-stack/Pixelle-Video/network/members"><img src="https://img.shields.io/github/forks/whitelotusvnmedia-stack/Pixelle-Video.svg" alt="Forks"></a>
  <a href="https://github.com/whitelotusvnmedia-stack/Pixelle-Video/blob/main/LICENSE"><img src="https://img.shields.io/github/license/whitelotusvnmedia-stack/Pixelle-Video.svg" alt="License"></a>
</p>

Chỉ cần nhập một **chủ đề**, Pixelle-Video sẽ tự động hoàn thành:
- ✍️ Viết kịch bản video
- 🎨 Tạo hình ảnh/video AI
- 🗣️ Tổng hợp giọng nói thuyết minh
- 🎵 Thêm nhạc nền
- 🎬 Ghép video chỉ với một cú nhấp

**Không cần kinh nghiệm, không cần kỹ năng chỉnh sửa** — Biến việc sáng tạo video thành chuyện đơn giản!


## 🖥️ Xem Trước Giao Diện Web

![Giao diện Web UI](resources/webui_en.png)


## 📋 Cập Nhật Gần Đây

- **2026-01-26**: Thêm module Chuyển Đổi Động Tác — tải lên video tham chiếu và hình ảnh để chuyển đổi động tác.
- **2026-01-14**: Thêm pipeline "Người Ảo" và "Ảnh Thành Video", hỗ trợ giọng TTS đa ngôn ngữ
- **2026-01-06**: Hỗ trợ máy RunningHub 48G VRAM
- **2025-12-28**: Giới hạn đồng thời RunningHub có thể cấu hình, cải thiện xử lý dữ liệu LLM
- **2025-12-17**: Thêm cấu hình API Key ComfyUI, hỗ trợ mô hình Nano Banana
- **2025-12-10**: FAQ tích hợp trong thanh bên, khắc phục sự cố TTS Edge
- **2025-12-08**: Hỗ trợ nhiều cách chia kịch bản (đoạn/dòng/câu)
- **2025-12-05**: Thêm gói Windows tích hợp, tối ưu luồng phân tích hình ảnh và video
- **2025-12-04**: Tính năng "Tùy Chỉnh Phương Tiện" mới - tải lên ảnh/video với phân tích AI
- **2025-11-18**: Xử lý song song RunningHub, trang lịch sử, tạo video hàng loạt


## ✨ Tính Năng Nổi Bật

- **Tạo Hoàn Toàn Tự Động** — Nhập chủ đề, tự động tạo video hoàn chỉnh
- **AI Viết Kịch Bản Thông Minh** — Tạo lời thoại dựa trên chủ đề, không cần tự viết
- **AI Tạo Hình Ảnh** — Mỗi câu đều có hình minh họa AI đẹp mắt
- **AI Tạo Video** — Hỗ trợ mô hình tạo video AI (như WAN 2.1) để tạo nội dung video động
- **AI Tạo Giọng Nói** — Hỗ trợ Edge-TTS, Index-TTS và nhiều giải pháp TTS phổ biến khác
- **Hỗ Trợ Tiếng Việt** — Giao diện hoàn toàn bằng tiếng Việt, giọng nói tiếng Việt (HoaiMy, NamMinh)
- **Nhạc Nền** — Thêm BGM cho video chuyên nghiệp hơn
- **Phong Cách Hình Ảnh** — Nhiều mẫu để lựa chọn
- **Kích Thước Linh Hoạt** — Hỗ trợ dọc, ngang và nhiều kích thước video
- **Nhiều Mô Hình AI** — Hỗ trợ GPT, Qwen, DeepSeek, Ollama và nhiều hơn
- **Kết Hợp Linh Hoạt** — Dựa trên kiến trúc ComfyUI, tùy chỉnh bất kỳ khả năng nào


## 📊 Quy Trình Tạo Video

Pixelle-Video áp dụng thiết kế module, quy trình tạo video rõ ràng và đơn giản:

![Quy trình tạo video](resources/flow_en.png)

Từ nhập văn bản đến xuất video cuối: **Tạo kịch bản → Lên kế hoạch hình ảnh → Xử lý từng khung hình → Ghép video**

Mỗi bước hỗ trợ tùy chỉnh linh hoạt, cho phép bạn chọn các mô hình AI, engine âm thanh, phong cách hình ảnh khác nhau.


## 🚀 Bắt Đầu Nhanh

### 🪟 Gói Windows Tích Hợp (Khuyến nghị cho người dùng Windows)

**Không cần cài đặt Python, uv hay ffmpeg, sẵn sàng sử dụng ngay!**

👉 **[Tải Gói Windows Tích Hợp](https://github.com/whitelotusvnmedia-stack/Pixelle-Video/releases/latest)**

1. Tải gói Windows mới nhất và giải nén
2. Nhấp đúp chạy `start.bat` để khởi động giao diện Web
3. Trình duyệt sẽ tự động mở http://localhost:8501
4. Cấu hình LLM API và dịch vụ tạo hình ảnh trong "⚙️ Cấu Hình Hệ Thống"
5. Bắt đầu tạo video!

> 💡 **Mẹo**: Gói tích hợp đã bao gồm tất cả dependencies, không cần cài đặt thủ công. Lần đầu chỉ cần cấu hình API Key.


### Cài Đặt Từ Mã Nguồn (Dành cho macOS / Linux hoặc người dùng muốn tùy chỉnh)

#### Yêu Cầu Môi Trường

Trước khi bắt đầu, cần cài đặt trình quản lý gói Python `uv` và công cụ xử lý video `ffmpeg`:

##### Cài đặt uv

Truy cập tài liệu chính thức uv để xem hướng dẫn cài đặt phù hợp hệ thống:
👉 **[Hướng dẫn cài đặt uv](https://docs.astral.sh/uv/getting-started/installation/)**

Sau khi cài, chạy `uv --version` trong terminal để xác nhận.

##### Cài đặt ffmpeg

**macOS**
```bash
brew install ffmpeg
```

**Ubuntu / Debian**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows**
- Tải tại: https://ffmpeg.org/download.html
- Giải nén và thêm thư mục `bin` vào biến môi trường PATH

Sau khi cài, chạy `ffmpeg -version` trong terminal để xác nhận.


#### Bước 1: Tải Dự Án

```bash
git clone https://github.com/whitelotusvnmedia-stack/Pixelle-Video.git
cd Pixelle-Video
```

#### Bước 2: Khởi Động Giao Diện Web

```bash
# Sử dụng uv để chạy (khuyến nghị, tự động cài dependencies)
uv run streamlit run web/app.py
```

Trình duyệt sẽ tự động mở http://localhost:8501

#### Bước 3: Cấu Hình Trên Giao Diện Web

Lần đầu sử dụng, mở rộng panel "⚙️ Cấu Hình Hệ Thống", điền:
- **Cấu hình LLM**: Chọn mô hình AI (như Qwen, GPT, v.v.) và nhập API Key
- **Cấu hình hình ảnh**: Nếu cần tạo hình, cấu hình địa chỉ ComfyUI hoặc RunningHub API Key

Sau khi cấu hình, nhấp "Lưu Cấu Hình" và bắt đầu tạo video!


## 💻 Hướng Dẫn Sử Dụng

Mở giao diện Web, bạn sẽ thấy bố cục ba cột:


### ⚙️ Cấu Hình Hệ Thống (Bắt buộc lần đầu)

#### 1. Cấu Hình LLM (Mô Hình Ngôn Ngữ Lớn)
Dùng để tạo kịch bản video AI.

**Chọn nhanh**
- Chọn mô hình từ menu thả xuống (Qwen, GPT-4o, DeepSeek, v.v.)
- Tự động điền base_url và model
- Nhấp "🔑 Lấy API Key" để đăng ký và lấy khóa

**Cấu hình thủ công**
- API Key: Nhập khóa của bạn
- Base URL: Địa chỉ API
- Model: Tên mô hình

#### 2. Cấu Hình Hình Ảnh

**Triển khai cục bộ (Khuyến nghị)**
- ComfyUI URL: Địa chỉ ComfyUI cục bộ (mặc định http://127.0.0.1:8188)
- Nhấp "Kiểm Tra Kết Nối" để xác nhận

**Triển khai đám mây**
- RunningHub API Key: Khóa dịch vụ tạo hình ảnh đám mây


### 📝 Nhập Nội Dung (Cột trái)

#### Chế Độ Tạo
- **AI Sáng Tạo**: Nhập chủ đề, AI tự động viết kịch bản
- **Tự Viết Kịch Bản**: Nhập kịch bản hoàn chỉnh, bỏ qua AI viết

#### Nhạc Nền (BGM)
- **Không BGM**: Chỉ giọng thuyết minh
- **Nhạc có sẵn**: Chọn nhạc nền có sẵn
- **Nhạc tùy chỉnh**: Đặt file nhạc (MP3/WAV) vào thư mục `bgm/`


### 🎤 Cài Đặt Giọng Nói (Cột giữa)

#### Luồng TTS
- Chọn luồng TTS từ menu thả xuống (Edge-TTS, Index-TTS, v.v.)
- **Giọng tiếng Việt**: HoaiMy (nữ) và NamMinh (nam) được đặt ưu tiên đầu
- Hệ thống tự động quét thư mục `workflows/` cho luồng TTS

#### Âm Thanh Tham Chiếu (Tùy chọn)
- Tải lên file âm thanh để sao chép giọng (MP3/WAV/FLAC)
- Áp dụng cho luồng TTS hỗ trợ sao chép giọng (như Index-TTS)


### 🎨 Cài Đặt Hình Ảnh (Cột giữa)

#### Tạo Hình Ảnh
- Chọn luồng tạo hình ảnh từ menu thả xuống
- Hỗ trợ cục bộ (selfhost) và đám mây (RunningHub)
- Tiền tố gợi ý để kiểm soát phong cách hình ảnh

#### Mẫu Video
- `static_*.html`: Mẫu tĩnh (không cần AI tạo media)
- `image_*.html`: Mẫu hình ảnh (sử dụng hình AI)
- `video_*.html`: Mẫu video (sử dụng video AI)


### 🎬 Tạo Video (Cột phải)

- Cấu hình xong tất cả, nhấp "🎬 Tạo Video"
- Hiển thị tiến độ thời gian thực
- Video lưu trong thư mục `output/`


### ❓ Câu Hỏi Thường Gặp

**H: Lần đầu sử dụng mất bao lâu?**
Đ: Thời gian tùy thuộc vào số cảnh, mạng và tốc độ AI, thường vài phút.

**H: Chi phí khoảng bao nhiêu?**
Đ: **Dự án hoàn toàn hỗ trợ chạy miễn phí!**

- **Hoàn toàn miễn phí**: LLM dùng Ollama (chạy cục bộ) + ComfyUI cục bộ = 0 đồng
- **Khuyến nghị**: LLM dùng Qwen (chi phí rất thấp) + ComfyUI cục bộ
- **Đám mây**: LLM dùng OpenAI + RunningHub (chi phí cao nhưng không cần môi trường cục bộ)


## 🤝 Dự Án Tham Khảo

- [Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP) - Máy chủ MCP ComfyUI
- [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) - Công cụ tạo video
- [NarratoAI](https://github.com/linyqh/NarratoAI) - Tự động hóa giải thuyết phim
- [ComfyKit](https://github.com/puke3615/ComfyKit) - Thư viện luồng công việc ComfyUI

Cảm ơn tinh thần mã nguồn mở của các dự án này! 🙏


## 📢 Phản Hồi & Hỗ Trợ

- 🐛 **Gặp vấn đề**: Gửi [Issue](https://github.com/whitelotusvnmedia-stack/Pixelle-Video/issues)
- 💡 **Đề xuất tính năng**: Gửi [Feature Request](https://github.com/whitelotusvnmedia-stack/Pixelle-Video/issues)
- ⭐ **Cho Star**: Nếu dự án hữu ích, hãy cho một Star ủng hộ!


## 📝 Giấy Phép

Dự án sử dụng giấy phép Apache 2.0, xem chi tiết tại file [LICENSE](LICENSE).
