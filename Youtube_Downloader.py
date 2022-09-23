from pytube import YouTube # here i am importint the library pytube
                           # joki humne pip ki help se cmd se install kiya tha baki aap mere
                           # how to import python libraries.txt file se instruction follow kar sakte h
                           # ki kaise install karte h libraries python ki  

link = "https://youtu.be/WKPeYsuBpm4"

Youtube_1 = YouTube(link) #yha Youtube_1 is variable and YouTube is libary which we import

print(Youtube_1.title) # Iss command se hum uper wali youtbe video ka tittle dekh sakte h

# print(Youtube_1.thumbnail_url) #iss line se hum uper wali yotube video ka thumbnail dekh ya download kar sakte h

video = Youtube_1.streams.all() #all is a function or yha per hum video kis kis quality me avialable h wo dekh rahe h

#video = Youtube_1.streams.filter(only_audio=True) #this code is for only audio download karne kiye h

vid = list(enumerate(video)) #yha vid ek variable h or
for i in vid:print(i) #hum yha per ek for loop chala rhe h

strm = int(input("enter : "))
video [strm].download() #download function
print("Sucsessfully")

#******For Playlist download***********

#from pytube import Playlist

#pl = Playlist("https://youtube.com/playlist?list=PLjVLYmrlmjGfpwYhVAbiGAhFl6h8XWDV_")
#print(f'Downloading : {pl.title}')

#for video in pl.videos:
#    video.streams.first().download()