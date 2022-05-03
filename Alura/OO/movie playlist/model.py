from film import Film
from serie import Serie
from playlist import Playlist


def main():
    avengers = Film('vingadores - guerra infinita', 2018, 160)
    the_suits = Serie('the suits', 2014, 9)
    tmep = Film('Todo mundo em pânico', 1999, 100)
    demolidor = Serie('Demolidor', 2016, 2)

    avengers.add_likes()
    tmep.add_likes()
    tmep.add_likes()
    tmep.add_likes()
    tmep.add_likes()
    demolidor.add_likes()
    demolidor.add_likes()
    the_suits.add_likes()
    the_suits.add_likes()
    the_suits.add_likes()


    film_and_series = [avengers, the_suits, demolidor, tmep]
    playlist_weekend = Playlist('Fim de semana', film_and_series)

    print(f'Tamanho da playlist: {len(playlist_weekend)}')

    print(playlist_weekend[0])

    print('Minha lista de programas:')
    for program in playlist_weekend:
        print(program)


if __name__ == "__main__":
    main()
