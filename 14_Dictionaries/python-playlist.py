playlist = {'title' : 'Patagonia',
            'author': 'Colt Steele',
            'songs' : [
                {'title' : 'Song1', 'Artist' : ['blue'],'Duration' : 2.5},
                {'title' : 'Song2', 'Artist' : ['blue' , 'kitty'],'Duration' : 5.25},
                {'title' : 'mewoew', 'Artist' : ['garfield'],'Duration' : 2.0}
            ]
        }

total_lenght = 0
for song in playlist['songs']:
    total_lenght += song['Duration']

print(total_lenght)