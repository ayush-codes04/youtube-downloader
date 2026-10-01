# 🎥 YouTube Video & Audio Downloader

A web application built with Python and Flask that enables users to download YouTube videos locally in high quality. The app uses `yt-dlp` for media retrieval and `FFmpeg` for media processing and format conversion.

---

## 🛠️ Tech Stack & Prerequisites

- **Backend:** Python 3, Flask
- **Core Processing:** `yt-dlp`, FFmpeg
- **JS Runtime** Node.js (used by 'yt-dlp' to execute YouTube JavaScript challenges)
- **Frontend:** HTML5, CSS3

---

## ⚙️ Prerequisites & FFmpeg Setup

This application requires **FFmpeg** to merge audio/video streams and process high-resolution downloads.

### 1. Node.js (Recomended)
'yt-dlp' requires a JavaScript runtime like **Node.js** to solve YouTube's signature deciphering and bot-detection challenges.
- Download and install Node.js from [nodejs.org](https://nodejs.org/).

### 2. FFmpeg setup
This application requires **FFmpeg** to merge separate audio/video streams into single MP4 files and convert extracted audio into high-quality MP3.

#### Windows
1. Download FFmpeg from the official release page: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract the zip file.
3. Place `ffmpeg.exe` inside your project root folder **OR** add the FFmpeg `bin` directory to your system's `PATH` environment variable.

#### macOS
Install via Homebrew:
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update && sudo apt install ffmpeg
```

---

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ayush-codes04/youtube-downloader.git](https://github.com/ayush-codes04/youtube-downloader.git)
   cd youtube-downloader
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows:
   venv\Scripts\activate
   
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your web browser.

---

## 🔎 Troubleshooting

1. **yt-dlp JS Player/Extractor Errors**:
   YouTube updateas its challenge scripts regularly. Ensure **Node.js** is installed on your machine so **yt-dlp** can execute JS deciphering seamlessly.

2. FFmpeg Missing;
   If HD videos fail to merge or MP3 conversion throws errors, verify that **ffmpeg.exe** is located in the project root directory or added to your system **PATH**.

3. Outdated **yt-dlp** Library:
   If downloads stop working unexpectedly, update **yt-dlp** to the latest version:
   ```bash
      pip install --upgrade yt-dlp
   ```
---

## ⚖️ Disclaimer

This project was built **strictly for educational purposes** to explore Python web frameworks, asynchronous request processing, and multimedia handling. 

- The author does not host or distribute copyrighted media.
- Users are responsible for complying with local copyright laws and YouTube's Terms of Service.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.