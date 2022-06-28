#Exercise 3
try:
    def make_album(artist, title, tracks=0):
        album_dict = {
            'artist': artist.title(),
            'title': title.title(),
            }
        if tracks:
            album_dict['tracks'] = tracks
        return album_dict

    album = make_album('One Direction', 'Up all Night')
    print(album)

    album = make_album('Debussy', 'Clair De Lune')
    print(album)

    album = make_album('BTS', 'Wings')
    print(album)

    album = make_album('BLACKPINK', 'THE ALBUM',tracks=8)
    print(album)

except:
    print('Error!.')
finally:
    print('\nThank you for using this program')