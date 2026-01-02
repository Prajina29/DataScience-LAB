# 1. Movie Ratings Analyzer
# Ask the user to input a list of movies with ratings like [("Titanic", 8), ("Inception", 9), ...]. Compute
# the average rating, find the highest-rated movie, and list all movies with rating above the
# average.

def movie_analyzer():
    
    
    print("Enter movies and ratings like: Avatar-9,Matrix-8,Joker-9")
   
    while True:
        user_input = input("Enter movies and ratings: ").strip()
        
        if user_input == "":
            print("No more input. Exiting...")
            break

        movies = []
        movie_entries = user_input.split(",")

        for entry in movie_entries:
            try:
                name, rating = entry.split("-")
                name = name.strip()
                rating = float(rating.strip())
                movies.append((name, rating)) 
            except:
                print(f"Invalid format for '{entry.strip()}'. Use Movie-Rating (Example: Titanic-8)")
                continue

        if not movies:
            print("No valid movies entered in this line.")
            continue

        # Calculate average rating
        ratings = []
        for movie in movies:
            ratings.append(movie[1])
        avg_rating = sum(ratings) / len(ratings)

        # Find highest rated movie
        highest_movie = movies[0]
        for movie in movies[1:]:
            if movie[1] > highest_movie[1]:
                highest_movie = movie

        # Movies above average
        above_avg = []
        for movie in movies:
            if movie[1] > avg_rating:
                above_avg.append(movie[0])

        # Movies below average
        below_avg = []
        for movie in movies:
            if movie[1] < avg_rating:
                below_avg.append(movie[0])

        # Print results 
        print("\nOutput ")
        print("Average rating:", round(avg_rating, 2))
        print("Highest rated movie:", highest_movie[0])

        if len(above_avg) == 0:
            print("Movies above average: None")
        else:
            print("Movies above average:", *above_avg, sep=", ")

        if len(below_avg) == 0:
            print("Movies below average: None")
        else:
            print("Movies below average:", *below_avg, sep=", ")
        print()  # blank line for next input

movie_analyzer()