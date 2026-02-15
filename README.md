# Video to Text

A simple Python tool that downloads audio from YouTube videos and generates a transcribed text summary using OpenAI's Whisper model.

## Description

This project automates the process of converting YouTube video content into written text. It utilizes `yt-dlp` to extract high-quality audio and `openai-whisper` for accurate speech-to-text transcription. The output is formatted into multiple lines and saved to a local file for easy reading.

## Installation

### Prerequisites

- Python 3.8 or higher
- [FFmpeg](https://ffmpeg.org/) installed on your system (required for audio processing)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd video-to-text
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install yt-dlp openai-whisper torch
   ```

## Usage

Run the script by providing a YouTube URL as a command-line argument:

```bash
python main.py "https://www.youtube.com/watch?v=x7X9w_GIm1s"
```

### Model Options

By default, the tool uses the "base" model, which offers a good balance of speed and accuracy. However, you can modify `main.py` to use other models depending on your needs:

- `tiny`: Fastest, lowest accuracy, ~39M parameters.
- `base`: Fast, good accuracy, ~74M parameters (default).
- `small`: Slower, better accuracy, ~244M parameters.
- `medium`: Slow, high accuracy, ~769M parameters.
- `large`: Slowest, best accuracy, ~1550M parameters.

### Expected Outcome

- The script will download the audio in MP3 format.
- Whisper will process the audio (this may take a moment depending on your hardware and video length).
- A file named `summary.txt` will be created in the project directory containing the transcribed text split into lines.
- The temporary audio file will be automatically deleted after transcription.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Tests

Currently, this project uses manual verification. To test the installation, run the usage command with the provided example video and verify that `summary.txt` is generated with the expected content.
