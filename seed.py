from models import db, Song, Playlist, PlaylistSong, connect_db
from app import app

connect_db(app)
db.drop_all()
db.create_all()


song1 = Song(title='I believe I can fly', artist='kelly')
song2 = Song(title='Right On', artist='Da Baby')
song3 = Song(title='Drive', artist='Clean bandit')
song4 = Song(title='Animal', artist='Steve Aoki')
song5 = Song(title='Just Got Paid', artist='IDK')


playlist1 = Playlist(name='favorite', description='myfavorite')
playlist2 = Playlist(name='Drive', description='for car ride')

db.session.add_all([song1, song2, song3, song4, song5])
db.session.add_all([playlist1, playlist2])

db.session.commit()
playlists_song1 = PlaylistSong(playlist_id=playlist1.id, song_id=song1.id)
playlists_song2 = PlaylistSong(playlist_id=playlist1.id, song_id=song2.id)
playlists_song3 = PlaylistSong(playlist_id=playlist1.id, song_id=song3.id)
playlists_song4 = PlaylistSong(playlist_id=playlist2.id, song_id=song4.id)
playlists_song5 = PlaylistSong(playlist_id=playlist2.id, song_id=song5.id)

db.session.add_all([playlists_song1, playlists_song2,
                   playlists_song3, playlists_song4, playlists_song5])
db.session.commit()
