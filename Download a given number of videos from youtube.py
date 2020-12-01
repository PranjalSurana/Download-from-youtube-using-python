from pytube import YouTube

n=int(input("No of videos - "))


for i in range(n):
    yt = YouTube(input("Enter the link of YouTube video : "))
    rt=yt.streams.get_by_itag('18')
    locn=input("Enter the destination : ")
    rt.download(locn)
    print('FileSize : ' + str(round(rt.filesize/(1024*1024))) + 'MB')
    print("Download complete")

print("Completed")
