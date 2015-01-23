__author__ = 'rsukla'

from movie_website import Mymovie
import fresh_tomatoes

the_imitation_game = Mymovie('The Imitation Game', 'Movie based on Alan Turing life',
                             'http://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg',
                           'https://www.youtube.com/watch?v=S5CjKEFb-sM')

Gone_Girl = Mymovie('The Gone Girl', 'David Fincher ',
                    'http://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg',
                    'https://www.youtube.com/watch?v=Ym3LB0lOJ0o')

American_Sniper = Mymovie('American Sniper', 'Based on life American Sniper',
                          'http://upload.wikimedia.org/wikipedia/en/1/10/American_Sniper_poster.jpg',
                        'https://www.youtube.com/watch?v=5bP1f_1o-zo')

Interstellar = Mymovie('Interstellar', 'Transcend the Universe',
                          'http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg',
                        'https://www.youtube.com/watch?v=0vxOhd4qlnA')

Hunger_Games = Mymovie('Hunger Games', 'Jennifer Aniston',
                          'http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
                        'https://www.youtube.com/watch?v=FovFG3N_RSU')

Captain_America = Mymovie('Captain America', 'Captain America',
                          'http://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg',
                        'https://www.youtube.com/watch?v=7SlILk2WMTI')

movie_l = [the_imitation_game, Gone_Girl, American_Sniper, Interstellar, Hunger_Games, Captain_America]

fresh_tomatoes.open_movies_page(movie_l)
