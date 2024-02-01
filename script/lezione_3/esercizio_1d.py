def build_playlist_dict(a_txt):
    result_dict = {}
    songs = a_txt.split(" ;; ")
    for a_song in songs:
        song_parts = a_song.split("::")
        album = song_parts[0]
        song_name = song_parts[1]
        if album not in result_dict:
            result_dict[album] = []
        result_dict[album].append(song_name)
    return result_dict

playlist_txt = "el camino::lonely boy ;; el camino::little black submarine ;; el camino::gold on the ceiling ;; turn blue::fever ;; turn blue::gotta get away ;; brothers::howlin for you ;; brothers::tighten up ;; turn blue::it is up to you now"
playlist_dict = build_playlist_dict(playlist_txt)
print(playlist_dict)