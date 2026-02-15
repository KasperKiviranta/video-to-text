import yt_dlp
import whisper
import os
import sys

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'audio.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "audio.mp3"

def transcribe_audio(file_path):
    # Available models: "tiny", "base", "small", "medium", "large"
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return "\n".join([segment['text'].strip() for segment in result['segments']])

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <youtube_url>")
        sys.exit(1)

    url = sys.argv[1]
    audio_file = None

    try:
        print(f"Downloading audio from {url}...")
        audio_file = download_audio(url)
        
        print("Transcribing audio...")
        text = transcribe_audio(audio_file)
        
        print("Saving transcription to summary.txt...")
        with open("summary.txt", "w") as f:
            f.write(text.strip())
            
        print("Done!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if audio_file and os.path.exists(audio_file):
            print(f"Deleting {audio_file}...")
            os.remove(audio_file)

if __name__ == "__main__":
    main()
