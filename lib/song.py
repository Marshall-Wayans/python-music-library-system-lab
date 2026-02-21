class Song:
    #These are the class attributes to track the global info across all songs
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        #Update all the class level statistics
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    #Increment the total song count
    def add_song_to_count(self):
        Song.count += 1

    #Add genre if it is new
    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
    
    #Add artist if it is new
    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    #Update genre_count dictionary
    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    #Update the artist_count in the dictionary
    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

    
    pass
