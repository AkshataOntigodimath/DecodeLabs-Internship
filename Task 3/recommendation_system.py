# AI Recommendation System
# DecodeLabs Artificial Intelligence Internship - Project 3

movies = [
    {"name": "Inception", "genres": ["Action", "Sci-Fi", "Thriller"]},
    {"name": "Interstellar", "genres": ["Sci-Fi", "Adventure", "Drama"]},
    {"name": "The Dark Knight", "genres": ["Action", "Crime", "Drama"]},
    {"name": "Avengers: Endgame", "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"name": "Titanic", "genres": ["Romance", "Drama"]},
    {"name": "The Conjuring", "genres": ["Horror", "Thriller"]},
    {"name": "Toy Story", "genres": ["Animation", "Comedy", "Adventure"]},
    {"name": "Finding Nemo", "genres": ["Animation", "Adventure", "Comedy"]}
]


def recommend_movies(user_preferences):
    recommendations = []

    for movie in movies:
        matching_genres = set(user_preferences).intersection(movie["genres"])
        similarity_score = len(matching_genres)

        if similarity_score > 0:
            recommendations.append({
                "name": movie["name"],
                "genres": movie["genres"],
                "score": similarity_score
            })

    recommendations.sort(key=lambda x: x["score"], reverse=True)

    return recommendations


# Test the recommendation system
if __name__ == "__main__":

    user_preferences = ["Action", "Sci-Fi"]

    recommendations = recommend_movies(user_preferences)

    print("\nYour Preferred Genres:", ", ".join(user_preferences))
    print("\nRecommended Movies:")

    for movie in recommendations:
        print(
            f"{movie['name']} | "
            f"Genres: {', '.join(movie['genres'])} | "
            f"Match Score: {movie['score']}"
        )