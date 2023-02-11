import sys
from pytube import YouTube

#handle invalid URL or no stream found: forward error to c++ program
#tell c++ program done
#success or fail signal
def main(urlName):
    yt = YouTube(urlName)
    st = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    if st == None:
        print("No stream found.")
        exit(1)
    location = st.download(output_path="temp\\", timeout=10)
    print("File Saved at: ", location)
    if location == "":
        print("Unable to download")
        exit (-1)
    exit(0)

if __name__ == "__main__":
    numArgs = len(sys.argv)
    if numArgs != 2:
        print("Incorrect usage!! Exmaple: python main.py {url}")
        exit(-1)
    urlName = sys.argv[1]
    print("Getting: ", urlName)
    main(urlName)
