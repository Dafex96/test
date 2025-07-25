#albums = {album_id: [title, artist, genre, release_year,format_]}

albums = {
    'ALB001': ['A Night at the Opera', 'Queen', 'Rock', 1975, 'Vinyl'],
    'ALB002': ['Thriller', 'Michael Jackson', 'Pop', 1982, 'CD'],
    'ALB003': ['Dark Side of the Moon', 'Pink Floyd', 'Rock', 1973, 'Vinyl'],
    'ALB004': ['21', 'Adele', 'Pop', 2011, 'Digital'],
    'ALB005': ['Back in Black', 'AC/DC', 'Rock', 1980, 'CD'],
    'ALB006': ['Abbey Road', 'The Beatles', 'Rock', 1980, 'CD'],
    'ALB007': ['GNX', 'Kendrick Lamar', 'Rap', 2024, 'Digital'],
    'ALB008': ['Make it Big', 'Wham!', 'Pop', 1984, 'Vinyl'],
}

#inventory = {album_id: [price, stock]}

inventory = {
    'ALN001': [6],
    'ALN002': [7],
    'ALN003': [8],
    'ALN004': [9],
    'ALN005': [10],
    'ALN006': [0],
    'ALN007': [11],
    'ALN008': [12],
}

def music_menu():
    print("\n--Digital Melody's--")
    print("1) Stock by genre.")
    print("2) Search by release year.")
    print("3) Update stock.")
    print("4) Quit.")

def genre_menu():
    print("\n--Genre Menu--")
    print("1) Rock")
    print("2) Pop")
    print("3) Rap")

while True:
    try:
        music_menu()
        
        opt = int(input("Insert an option: "))
        
        
        
        
        
        
    except ValueError:
        print("Invalid option, try again.")