songs = ["happy","sad","mad","crazy"]
theNewPlaylist = ["song", "song", "song", "song"]


def createPlaylist(songList,playlist):
    for i in songList: 
        speed = input("is " + i + " a slow song?")
        if speed == "yes" and playlist[0] == "song":
            playlist[0] = i

        elif speed == "yes" and playlist[0] != "song":
            playlist[2] = i
       
        elif speed == "no" and playlist[1] == "song":
            playlist[1] = i
         
        elif speed == "no" and playlist[1] != "song":
            playlist[3] = i
    print(playlist)
           
     

createPlaylist(songs,theNewPlaylist)


