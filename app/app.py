from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS  # Importujemy CORS

app = Flask(__name__)
CORS(app)

app = Flask(__name__)

# Wczytanie danych
merged = pd.read_csv(r'C:\Users\szymo\PycharmProjects\PythonProject\data\merged.csv')
reduced_similarity_cv = joblib.load(r'C:\Users\szymo\PycharmProjects\PythonProject\artefacts\reduced_similarity_cv.pkl')
final_sim = joblib.load(r'C:\Users\szymo\PycharmProjects\PythonProject\artefacts\final_sim_matrix.pkl')

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

@app.route('/recommend', methods=['GET'])
def recommend():
    movie = request.args.get('movie')
    method = request.args.get('method')

    if not movie or not method:
        return jsonify({'error': 'Podaj tytuł filmu i metodę rekomendacji!'})

    if method == 'cv':
        recommendations = recommend_movie_cv(movie)
    elif method == 'tf':
        recommendations = recommend_tf(movie)
    else:
        return jsonify({'error': 'Niepoprawna metoda rekomendacji! Wybierz "cv" lub "tf".'})

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)