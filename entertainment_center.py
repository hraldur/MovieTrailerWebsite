import fresh_tomatoes
import media

#Create objects of movies
toy_Story = media.Movie("Toy Story", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
finding_Nemo = media.Movie("Finding Nemo", "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg", "https://www.youtube.com/watch?v=wZdpNglLbt8")
the_Incredibles = media.Movie("The Incredibles", "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg", "https://www.youtube.com/watch?v=eZbzbC9285I")
up = media.Movie("Up", "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg", "https://www.youtube.com/watch?v=pkqzFUhGPJg")
monsters = media.Movie("Monsters, Inc", "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG", "https://www.youtube.com/watch?v=cvOQeozL4S0")
the_Lego_Movie = media.Movie("The Lego Movie", "https://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg", "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

#Create a list with all  the movies objects
movies = [toy_Story, finding_Nemo, the_Incredibles, up, monsters, the_Lego_Movie]
#Call function from fresh_tomatoes to create the movie page
fresh_tomatoes.open_movies_page(movies)