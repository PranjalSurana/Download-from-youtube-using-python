from pytube import YouTube

l=[]
e=''

files=input("Enter the file : ")
f = open(files,'r')

for i in f:
    print(i)
    yt = YouTube(i)
    rt=yt.streams.get_by_itag('18')
    
    print(yt.title,end=' ')
    rt.download('C:\\Users\\Pranjal\\Documents\\Python\\Videos')
    print("Download complete")
    print()
    print()

            
