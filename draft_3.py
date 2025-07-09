quantity = 0
movies = []

def menu():
    print("\n---Movies---")
    print("1) Save movie(s)")
    print("2) Show movie(s)")
    print("3) Delete movie(s)")
    print("4) Search movie(s)")
    print("5) Quit")

while True:
    
    menu()
    
    opt = int(input("Insert an option: "))
    
    if opt == 1:
        
        print("Save")
        quantity = int(input("Insert how many movies do you want to save: "))
        for i in range (1,quantity+1):
            print(f"-----Save movie number {i}-----")
            name = input("Insert a movie: ")
            year = int(input("Insert the year of the movie: "))
            movies.append({
                "name": name,
                "year": year
            })
            
    elif opt == 2:
        
        print("Show")
        for index,movie in enumerate(movies):
            print(f"{index+1} - {movie['name']} - {movie['year']}" )
            
    elif opt == 3:
        
        print("Delete")
        for index, movie in enumerate(movies):
            print(f"{index+1} - {movie['name']} - {movie['year']}")
            to_delete = int(input("Enter the number of the movie to delete: "))
            if 1 <= to_delete <= len(movies):
                deleted = movies.pop(to_delete - 1)
                print(f"Deleted: {deleted['name']}")
            else:
                print("Invalid number.")
                
    elif opt == 4:
        print("Search")
        search_name = input("Enter the name of the movie to search: ").lower()
        found = False
        for movie in movies:
            if search_name in movie['name'].lower():
                print(f"{movie['name']} - {movie['year']}")
                found = True
            if not found:
                print("Movie not found.")
        
    elif opt == 5:
        print("Quit")
        break
    else:
        print("Invalid option, try again.")