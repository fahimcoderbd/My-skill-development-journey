''''
Next Easy Real-World Array Problem

🎵 Music Playlist Manager

songs = ["Believer", "Shape of You", "Faded", "Believer", "Alone"]

Tasks:

Total songs count করো।
"Believer" কতবার আছে বের করো।
Playlist-এ duplicate song আছে কিনা বের করো।
Longest song name বের করো।
Alphabetically sort করে print করো।
'''
#Amar code

""" def get_dict_el(data):
    for key,value in dict.items(data):
        return key,value

#playsit manager system
def playlist_manager(arr):
    if not arr:
        return None
    
    total_songs = len(arr)
    sorted_songs = sorted(arr)
    longest_song_name = max(arr, key=len)
    believer_count = 0
    duplicate_songs = {}

    #finding how many times believer appear
    for song in arr:
        if song == "Believer":
            believer_count += 1

    #returning final data
    return (
        f"Total songs: {total_songs} \n"
        f"Believer Appeared: {believer_count} times \n"
        f"Duplicate songs: {get_dict_el(duplicate_songs)} \n"
        f"Longest song: {longest_song_name} \n"
        f"Sorted songs: {sorted_songs}"
    ) """

#Optimized better code (Production level)
from collections import Counter

def playlist_manager(songs):
    if not songs:
        return "Playlist is empty!"

    frequency = Counter(songs)

    duplicates = {
        song: count
        for song, count in frequency.items()
        if count > 1
    }

    return {
        "total_songs": len(songs),
        "believer_count": frequency["Believer"],
        "duplicates": duplicates,
        "longest_song": max(songs, key=len),
        "sorted_songs": sorted(songs)
    }

#testing code
songs = ["Believer", "Shape of You", "Faded", "Believer", "Alone"]
print(playlist_manager(songs))

        





    