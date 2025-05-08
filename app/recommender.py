import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

merged = pd.read_csv('../data/merged.csv')

reduced_similarity_cv = joblib.load('../artefacts/reduced_similarity_cv.pkl')
final_sim = joblib.load('../artefacts/final_sim_matrix.pkl')

def recommend_movie_cv(movie):
    idx = merged[merged['title'] == movie].index[0]
    similar_list = reduced_similarity_cv[idx]

    movie_list = sorted(list(enumerate(similar_list)), reverse=True, key=lambda x:x[1])[:10]
    return [merged['title'][i[0]] for i in movie_list]


def recommend_tf(movie):
    idx = merged[merged['title'] == movie].index[0]
    similar_list = final_sim[idx]

    movie_list = sorted(list(enumerate(similar_list)), reverse=True, key=lambda x:x[1])[:10]
    return [merged['title'][i[0]] for i in movie_list]