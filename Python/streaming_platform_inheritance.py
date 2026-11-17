# Inheritance in Python OOP - Streaming Platform System


# Base Class (Parent)
class MediaContent:
    def __init__(self, title, release_year, genre, rating):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.rating = rating
        self.is_playing = False

    def play(self):
        self.is_playing = True
        print(f"▶️ Now playing: '{self.title}' ({self.release_year}) | Genre: {self.genre}")

    def pause(self):
        self.is_playing = False
        print(f"⏸️ Paused: '{self.title}'")

    def show_details(self):
        print(f"Title: {self.title} | Year: {self.release_year} | Genre: {self.genre} | Rating: {self.rating}/10")


# Child Class 1: Single Inheritance from MediaContent
class Movie(MediaContent):
    def __init__(self, title, release_year, genre, rating, duration_mins, director):
        super().__init__(title, release_year, genre, rating)
        self.duration_mins = duration_mins
        self.director = director

    def show_details(self):
        super().show_details()
        print(f"   Director: {self.director} | Duration: {self.duration_mins} mins\n")


# Child Class 2: Hierarchical Inheritance from MediaContent
class TVSeries(MediaContent):
    def __init__(self, title, release_year, genre, rating, seasons, episodes_per_season):
        super().__init__(title, release_year, genre, rating)
        self.seasons = seasons
        self.episodes_per_season = episodes_per_season

    def show_details(self):
        super().show_details()
        total_episodes = self.seasons * self.episodes_per_season
        print(f"   Seasons: {self.seasons} | Total Episodes: {total_episodes}\n")


# Child Class 3: Multilevel Inheritance (AnimeSeries -> TVSeries -> MediaContent)
class AnimeSeries(TVSeries):
    def __init__(self, title, release_year, genre, rating, seasons, episodes_per_season, studio, audio_language):
        super().__init__(title, release_year, genre, rating, seasons, episodes_per_season)
        self.studio = studio
        self.audio_language = audio_language

    def show_details(self):
        super().show_details()
        print(f"   Animation Studio: {self.studio} | Original Audio: {self.audio_language}\n")


# Creating objects from different child classes
movie1 = Movie("Inception", 2010, "Sci-Fi Thriller", 8.8, 148, "Christopher Nolan")
series1 = TVSeries("Stranger Things", 2016, "Sci-Fi Horror", 8.7, 4, 8)
anime1 = AnimeSeries("Attack on Titan", 2013, "Dark Fantasy", 9.1, 4, 22, "MAPPA / Wit Studio", "Japanese")

# Demonstrating inherited and overridden methods
print("--- STREAMING LIBRARY ---")
for item in (movie1, series1, anime1):
    item.show_details()

print("--- PLAYBACK CONTROLS ---")
movie1.play()
anime1.play()
movie1.pause()
