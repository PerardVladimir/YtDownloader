from pytube import YouTube

# link = input("Insert the link of the video : ")
url = input("Enter the video Url : ")

yt = YouTube(url)

# print(yt.title)
# Title of the video 
print("Title : " , yt.title)

# Number of view of the video 
print("View : ", yt.views) 

# Lenght of the video 
print("Lenght of video : ", yt.length)

# Description of the video 
print("Description : ", yt.length)

# Link for thumnail 
print("Thumbnail Link : ", yt.thumbnail_url)


# Rating 
print("Rating : ", yt.rating)

# Printing all the Audio Streams available
print(yt.streams.filter(only_audio=True))

# Printing all the Video Streams available
print(yt.streams.filter(only_video=True))

# Print only progressive streams
print(yt.streams.filter(progressive=True))

 # Get the highest progressive resolution
ys = yt.streams.get_highest_resolution()
ys.download() 
 