from collections import deque
import time

"""A simple music player implementation using the queue data structure. It plays songs from a playlist."""

class MusicPlayer:
    """
           Initialize a Music player object.

           Attributes - playlist: a queue to store the playlist.
                      - current_song: Song that's currently playing."""

    def __init__(self):
        self.playlist = deque()
        self.current_song = None

    def add_song(self, song):
        self.playlist.append(song)

    def play_song(self):

        while self.playlist:
            self.current_song = self.playlist.popleft()
            print(f"Currently playing: {self.current_song}")
            # Simulating song playing with a 3-second delay
            time.sleep(3)
        print("Playlist finished.")

    def skip_song(self):
        if self.playlist:
            self.current_song = self.playlist.popleft()
            print(f"Skipping: {self.current_song}")
        else:
            print("Playlist is empty.")

    def display_playlist(self):
        print("Current Playlist:")
        for song in self.playlist:
            print(song)

if __name__ == '__main__':
    # Create a Music player
    music_player = MusicPlayer()

    # Add songs
    music_player.add_song("Song 1")
    music_player.add_song("Song 2")
    music_player.add_song("Song 3")

    # Show the playlist
    music_player.display_playlist()

    music_player.play_song()

    music_player.skip_song()

    # Display the playlist again
    music_player.display_playlist()