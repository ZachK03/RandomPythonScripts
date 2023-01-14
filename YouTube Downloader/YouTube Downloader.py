import os
from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

titleVid = yt.title
lengthVid = yt.length
if lengthVid >= 60:
    minutesVid = int(lengthVid/60)
    secondsVid = int(lengthVid-(minutesVid*60))
    outputText = "{} {}:{}".format(titleVid,minutesVid,secondsVid)
else:
    outputText = "{} 0:{}".format(titleVid,lengthVid)

print(outputText)
print("Is this the video you're looking for? Y/N")
confirm = input()
if confirm.lower() == "y":
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download(output_path=str(os.path.dirname(os.path.realpath(__file__))))
    print("Download complete")
    print("Saved to the same folder as this file")
else:
    quit()