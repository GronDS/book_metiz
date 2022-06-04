'''8.8. Пользовательские альбомы: начните с программы из упражнения 8.7.
Напишите цикл while, в котором пользователь вводит исполнителя и название
альбома. Затем в цикле вызывается функция make_album() для введенных 
пользователей и выводится созданный словарь. Не забудьте предусмотреть
 признак завершения в цикле while.'''

def make_album(singer_name, album_name, tracks_num = None):
    album =  {'Singer' : singer_name.title(), 'Album' : album_name}
    if tracks_num:
        album['Tracks'] = tracks_num
    return album

print('\nEnter "q" at any time to quit\n')
while True:
    singer = input('Enter artist: ')
    if singer == 'q':
        break

    album_ = input('Enter album: ')
    if album_ == 'q':
        break

    tracks = input('Enter how many tracks is an album: ')
    if tracks == 'q':
        break

    print(make_album(singer,album_, tracks))