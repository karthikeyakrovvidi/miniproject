class MovieRecommendationSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, rating):
        movie = {'title': title, 'genre': genre, 'rating': rating}
        self.movies.append(movie)
        print(f"Added '{title}' to the movie database.")

    def search_movie(self, keyword):
        found_movies = []
        for movie in self.movies:
            if keyword.lower() in movie['title'].lower() or keyword.lower() in movie['genre'].lower():
                found_movies.append(movie)
        return found_movies

    def recommend_top_movies(self, n):
        sorted_movies = sorted(self.movies, key=lambda x: x['rating'], reverse=True)
        return sorted_movies[:n]

    def delete_movie(self, title):
        for movie in self.movies:
            if movie['title'].lower() == title.lower():
                self.movies.remove(movie)
                print(f"'{title}' has been deleted from the movie database.")
                return
        print(f"'{title}' not found in the movie database.")
def get_input():
    title = input("Enter the title of the movie: ")
    genre = input("Enter the genre of the movie: ")
    rating = float(input("Enter the rating of the movie: "))
    return title, genre, rating
movie_system = MovieRecommendationSystem()
while True:
    print("\n1. Add a new movie")
    print("2. Search for a movie")
    print("3. Recommend top movies")
    print("4. Delete a movie")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        title, genre, rating = get_input()
        movie_system.add_movie(title, genre, rating)
    elif choice == '2':
        keyword = input("Enter keyword to search: ")
        search_results = movie_system.search_movie(keyword)
        print("Search results:")
        for movie in search_results:
            print(movie)
    elif choice == '3':
        n = int(input("Enter the number of top movies to recommend: "))
        top_movies = movie_system.recommend_top_movies(n)
        print("\nTop recommended movies:")
        for movie in top_movies:
            print(movie)
    elif choice == '4':
        title = input("Enter the title of the movie to delete: ")
        movie_system.delete_movie(title)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
