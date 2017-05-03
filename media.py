import webbrowser

# Parent class
class Video():
     def __init__(self, title, duration):
         # Create instance variables 
         self.title = title
         self.duration = duration

# Child class
class Movie(Video):
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  # Movie rating
    
    def __init__(self, title, duration, movie_storyline, poster_image, trailer_youtube):
        # Inheritance from Video class 
        Video.__init__(self, title, duration)
        # Create instance variables
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        # Extract the youtube trailer
        webbrowser.open(self.trailer_youtube_url)
        webbrowser.open(self.poster_image_url)
        
        
class TvShow(Video):
    def __init__(self, season, episode, tv_station):
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self, actor, actress, plot):
        self.actor = actor
        self.actress = actress
        self.plot = plot
