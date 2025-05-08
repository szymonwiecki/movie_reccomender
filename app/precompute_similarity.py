import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD

similarity_cv = joblib.load('../artefacts/similarity_cv.pkl')
svd = TruncatedSVD(n_components=500)  # Redukcja wymiarów
reduced_similarity = svd.fit_transform(similarity_cv)
joblib.dump(reduced_similarity, '../artefacts/reduced_similarity_cv.pkl')

tfidf = joblib.load('../artefacts/tf_final_vec.pkl')
final_sim = cosine_similarity(tfidf)
joblib.dump(final_sim, '../artefacts/final_sim_matrix.pkl')
