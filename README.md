# 🎬 Movie Recommender System  

A **Movie Recommender System** built using **Machine Learning, Streamlit, and TMDB API**. This application suggests movies based on user input, displaying posters for better visualization.  

## 🚀 Features  
- 🔍 Search for a movie and get **5 similar recommendations**  
- 📌 Movie posters fetched from **TMDB API**  
- 🎭 Interactive UI built with **Streamlit**  
- 🧠 ML model trained on **movie similarity data**  

## 🛠️ Tech Stack  
- **Python** (pandas, numpy, scikit-learn)  
- **Streamlit** (for UI)  
- **TMDB API** (for fetching posters)  
- **Pickle** (to save ML model)  

## 🎯 How to Run Locally
```bash
# Clone the repository
git clone https://github.com/your-username/Movie-Recommender-System.git
cd Movie-Recommender-System


# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows
env\Scripts\activate
# On macOS/Linux
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
