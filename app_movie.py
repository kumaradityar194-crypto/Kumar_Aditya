import numpy as np
import pandas as pd
import ast
import difflib
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv(r"c:\Users\kumar\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\TempState\7A7D78A176B6E05ED93A1CA26C79C6EE\tmdb_5000_movies.csv")
credits = pd.read_csv(r"c:\Users\kumar\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\TempState\F47B4CD5A20FEDB42E52D55B305F6C57\tmdb_5000_credits.csv")

print("movies_shape", movies.shape)
print("credits_shape", credits.shape)

# Merge datasets on title
movies = movies.merge(credits, on='title')

# Keep only required columns
movies = movies[["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]]

# Drop rows with missing values
movies.dropna(inplace=True)

# Convert stringified lists to actual lists
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

def convert3(text):
    l = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            l.append(i["name"])
            counter += 1
        else:
            break
    return l

movies["cast"] = movies["cast"].apply(convert3)

def fetch_director(text):
    l = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            l.append(i['name'])
    return l

movies["crew"] = movies["crew"].apply(fetch_director)

# Remove spaces in words for tags
def collapse(l):
    l1 = []
    for i in l:
        l1.append(i.replace(" ", ""))
    return l1

movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)

# Split overview
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Create tags column
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# New dataframe with only id, title, and tags
new = movies.drop(columns=['overview', 'genres', 'keywords', 'cast', 'crew'])
new['tags'] = new['tags'].apply(lambda x: " ".join(x))

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(new["tags"]).toarray()

# Cosine similarity
similarity = cosine_similarity(vector)

# Save files using pickle
pickle.dump(new, open('movie_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

# Recommendation function with difflib for approximate matching
def recommend(movie):
    movie = movie.lower()

    # Approximate match using difflib
    matches = difflib.get_close_matches(movie, new['title'].str.lower().values, n=1, cutoff=0.6)

    if not matches:
        print("Movie not found in database!")
        return

    closest_match = matches[0]
    index = new[new['title'].str.lower() == closest_match].index[0]

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    print(f"\nShowing results for: {new.iloc[index].title}\n")

    for i in distances[1:6]:
        print(new.iloc[i[0]].title)

# Input from user
movie_name = input("Enter the movie name: ")
recommend(movie_name)


