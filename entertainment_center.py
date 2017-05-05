import fresh_tomatoes
import media

# 6 different movies, each one has title, duration, storyline, poster and trailer
toy_story = media.Movie(
    "Toy Story",
    "1h21m",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie(
    "Avatar",
    "2h42m",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

jerry_maguire = media.Movie(
    "Jerry Maguire",
    "2h19m",
    "A man who work as a sports agent",
    "https://upload.wikimedia.org/wikipedia/en/e/ea"
    "/Jerry_Maguire_movie_poster.jpg",
    "https://www.youtube.com/watch?v=rCCaTPY-z4Q")

zootopia = media.Movie(
    "Zootopia",
    "1h50m",
    "Bunny and Fox must work together in a city of anthropomorphic animals",
    "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
    "https://www.youtube.com/watch?v=jWM0ct-OLsM")

trumbo = media.Movie(
    "Trumbo",
    "2h4m",
    "A Hollywood's top screenwriter story",
    "https://upload.wikimedia.org/wikipedia/en/9/96"
    "/Trumbo_%282015_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=n0dZ_2ICpJE")

jason_bourne = media.Movie(
    "Jason Bourne",
    "2h3m",
    "The CIA's most dangerous former operative "
    "is drawn out of hiding to uncover more explosive truths about his past",
    "https://upload.wikimedia.org/wikipedia/en/b/b2"
    "/Jason_Bourne_%28film%29.jpg",
    "https://www.youtube.com/watch?v=F4gJsKZvqE4")

movies = [toy_story, avatar, jerry_maguire, zootopia, trumbo, jason_bourne]
fresh_tomatoes.open_movies_page(movies)   # show movie trailer site on browser

#print(trumbo.title)
#print(trumbo.duration)
#print(trumbo.storyline)

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__bases__)
