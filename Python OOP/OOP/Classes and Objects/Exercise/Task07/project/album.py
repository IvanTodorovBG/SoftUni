from project.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.args = args
        self.published = False
        self.songs = []
        self.songs = [current_song for current_song in self.args]

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        elif song in self.songs:
            return "Song is already in the album."
        elif song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        for current_song in self.songs:
            if current_song.name == song_name and self.published is True:
                return f"Cannot remove songs. Album is published."
            elif current_song.name == song_name and self.published is False:
                self.songs.remove(current_song)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return f"Album {self.name}\n" + '\n'.join([f"== {current_song.get_info()}"for current_song in self.songs])






