from recommender import recommend_movie_cv, recommend_tf

if __name__ == '__main__':
    print("=== System rekomendacji filmów ===")
    while True:
        print("\nWybierz metodę:")
        print("  1) CountVectorizer")
        print("  2) TF-IDF")
        print("  q) Wyjście")
        choice = input("> ").strip().lower()

        if choice == 'q':
            print("Do zobaczenia!")
            break
        movie = input("Podaj tytuł filmu: ").strip()

        try:
            if choice == '1':
                recs = recommend_movie_cv(movie)
            elif choice == '2':
                recs = recommend_tf(movie)
            else:
                print("Niepoprawny wybór, spróbuj ponownie.")
                continue

            print("\nRekomendacje:")
            for r in recs:
                print(f" - {r}")
        except ValueError as e:
            print(f"Błąd: {e}")