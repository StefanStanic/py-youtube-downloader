import yt_dlp
import csv
import os

""" Uses either a list from a csv or from input to download youtube video to MP3 in HQ"""


#Debuggers and a custom hook
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass
    
    def error(self,msg):
        print(msg)

def done_hook(done):
    if done['status'] == 'finished':
        print('Done downloading, now need to convert... please hold')

#populate the list with urls from the actuall file
def populate_url_list(url_file):
    with open(url_file, 'r', encoding = 'utf-8', errors = 'ignore') as input:
        reader = csv.reader(input)
        return list(row[0] for row in reader)

#initiates a stream and downloads the yotube + converts to mp3
def yt_downloader(urls_to_download):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',    
        }],
        'autonumber_start': 216,
        'logger': MyLogger(),
        'progress_hooks': [done_hook],
        'outtmpl': os.getcwd() + '/mp3-files/%(autonumber)s-%(title)s.%(ext)s',
        'no_check_certificate': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls_to_download)


def main():
    urls_to_download = populate_url_list('youtube_url_list.csv')
    yt_downloader(urls_to_download)



if __name__ == "__main__":
    print("Youtube Downloader started")
    main()
