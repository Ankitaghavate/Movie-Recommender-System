import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    """Fetch the movie poster from TMDB API using the movie_id."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3ea0f26d0e4a7c346eac11981c6c5697&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/500"  # Placeholder image if no poster is found


def recommend(movie):
    """Recommend movies based on similarity scores."""
    if movie not in movies['title'].values:
        st.error("Selected movie not found in dataset.")
        return [], []

    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:  # Get top 5 recommendations
        movie_id = movies.iloc[i[0]]['movie_id']  # Ensure 'movie_id' column exists
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]]['title'])

    return recommended_movie_names, recommended_movie_posters


# 🎬 Streamlit UI
st.header('🎥 Movie Recommender System')

# ✅ Load movie data and similarity matrix
try:
    movies = pickle.load(open('movie.pkl', 'rb'))  # Load the DataFrame
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    # Check if movies DataFrame contains the required columns
    if 'title' not in movies.columns or 'movie_id' not in movies.columns:
        raise ValueError("Movies DataFrame is missing required columns ('title', 'movie_id').")

except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])