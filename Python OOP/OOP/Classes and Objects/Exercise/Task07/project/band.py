from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for current_album in self.albums:
            if current_album.name == album_name and current_album.published is True:
                return "Album has been published. It cannot be removed."
            elif current_album.name == album_name and current_album.published is False:
                self.albums.remove(current_album)
                return f"Album {current_album.name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        return f"Band {self.name}\n" + '\n'.join([current_album.details() for current_album in self.albums])

