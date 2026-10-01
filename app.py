
#Importing required modules
from flask import Flask, render_template, url_for, request, redirect
import yt_dlp
import os

app = Flask(__name__)

# It creates a folder named 'Downloads' if it doesnot exist in pc
os.makedirs('Downloads', exist_ok=True)

#Home page of video downloader
@app.route('/', methods=['GET','POST'])
def video_home():
    if request.method == 'POST':
        video_url = request.form.get('input', '').strip()

        #If there is an input it takes to video_quality.html
        if video_url:
            return video_quality()
    #If there is no input it stays/come at the home page
    return render_template('video_home.html')

#Home page for video downloader
@app.route('/audio', methods=['GET','POST'])
def audio_home():
    if request.method == 'POST':
        video_url = request.form.get('input', '').strip()

        #If there is an input it takes to audio_download.html
        if video_url:
            return audio_download()
    #If there is no input it stays/come at the home page
    return render_template('audio_home.html')

@app.route('/video/quality', methods=['GET','POST'])
def video_quality():
    """
    Fetches video metadata or downloads the video file bases pn requested quality.
    """
    message = ""
    thumbnail_url = None
    title = None
    video_url = ""
    quality = "720"

    if request.method == 'POST':
        #Taking inputs
        video_url = request.form.get('input', '').strip()
        quality = request.form.get('quality', '720')
        action = request.form.get('action', 'fetch')

        if not video_url:
            message = "Please enter a valid link"
        else:
            #Takes the input and fetch the required things without downloading
            if action == 'fetch':
                ydl_opts = {
                    #Skips downloading
                    'skip_download': True,
                    #Set ffmpeg location to the local folder
                    'ffmpeg_location': '.',
                    }
                try: 
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info_dict = ydl.extract_info(video_url, download=False)
                        if info_dict:
                            #Shows the title and thumbnail in webpage without downloading
                            title = info_dict.get('title', '')
                            thumbnail_url = info_dict.get('thumbnail', '')
                            message = "Ready to download!"
                except Exception as e:
                    message = f"Error fetching info: {str(e)}"

            elif action == 'download':
                ydl_opts = {
                    #Set the path of downloads
                    'outtmpl': 'Downloads/%(title)s.%(ext)s',
                    #Fetches the quality as per selected in the webpage and merge using ffmpeg
                    'format' : f'bestvideo[height<={quality}] + bestaudio/best',
                    #Set the format to mp4
                    'merge_output_format': 'mp4',
                    #Stops multiple downloads
                    'noplaylist': True,
                    'ffmpeg_location': '.',
                }

                try: 
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        #Extract the video from url
                        info_dict = ydl.extract_info(video_url, download=False)
                        if info_dict:
                            title = info_dict.get('title', '')
                            thumbnail_url = info_dict.get('thumbnail', '')

                        ydl.download([video_url])
                        message = "video downloaded successfully!"
                except yt_dlp.utils.DownloadError:
                    message = "Invalid URL or video not found. please check your link and try again."
                except Exception as e:
                    message = f"An error occured: {str(e)}"

    return render_template(
        'video_quality.html', 
        status = message, 
        thumbnail = thumbnail_url, 
        video_title = title, 
        video_url = video_url, 
        quality = quality
    )

@app.route('/audio/download', methods=['GET','POST'])
def audio_download():
    """
    Fetches audio metadata or extracts and converts YouTube audio to mp3
    format using FFmpeg postprocessing.
    """
    message = ""
    thumbnail_url = None
    title = None
    video_url = ""

    if request.method == 'POST':
        #Taking inputs
        video_url = request.form.get('input', '').strip()
        action = request.form.get('action', 'fetch')

        if not video_url:
            message = "Please enter a valid link"
        else:
            #Takes the input and fetch the required things without downloading 
            if action == 'fetch':
                ydl_opts = {
                    'skip_download': True,
                    'ffmpeg_location': '.',
                    }
                try: 
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info_dict = ydl.extract_info(video_url, download=False)
                        if info_dict:
                            #Shows the title and thumbnail and title in webpage without downloading
                            title = info_dict.get('title', '')
                            thumbnail_url = info_dict.get('thumbnail', '')
                            message = "Ready to download!"
                except Exception as e:
                    message = f"Error fetching info: {str(e)}"

            elif action == 'download':
                ydl_opts = {
                    #Sets path of downloads
                    'outtmpl': 'Downloads/%(title)s.%(ext)s',
                    'format' : 'bestaudio/best',
                    #Uses ffmpeg to extract audio and sets its format to mp3
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'ffmpeg_location': '.',
                }

            try: 
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    #Extract the video info from url
                    info_dict = ydl.extract_info(video_url, download=False)
                    if info_dict:
                        title = info_dict.get('title', '')
                        thumbnail_url = info_dict.get('thumbnail', '')
                        ydl.download([video_url])
            except yt_dlp.utils.DownloadError:
                message = "Invalid URL or video not found. please check your link and try again."
            except Exception as e:
                message = f"An error occured: {str(e)}"
           
        return render_template(
            'audio_download.html',
            status = message, 
            thumbnail = thumbnail_url, 
            video_title = title, 
            video_url = video_url
        )
           

if __name__ == "__main__":
    app.run(debug=True)
