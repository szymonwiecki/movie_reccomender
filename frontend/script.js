async function recommend(method) {
    const movieTitle = encodeURIComponent(document.getElementById('movieInput').value);
    if (!movieTitle) {
        alert("Podaj tytuł filmu!");
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:5000/recommend?movie=${movieTitle}&method=${method}`);

        console.log("Status odpowiedzi:", response.status);

        if (!response.ok) {
            throw new Error(`Błąd: ${response.status}`);
        }

        const data = await response.json();
        console.log("Otrzymane dane:", data);

        const recommendationsList = document.getElementById('recommendations');
        recommendationsList.innerHTML = ""; // Czyszczenie listy przed dodaniem nowych elementów

        if (Array.isArray(data)) {  // 🔥 Sprawdzenie, czy `data` to tablica!
            data.forEach(movie => {
                const li = document.createElement("li");
                li.textContent = movie;
                recommendationsList.appendChild(li);
            });
        } else {
            console.error("Niepoprawny format danych:", data);
            alert("Niepoprawne dane z backendu!");
        }
    } catch (error) {
        console.error("Błąd w komunikacji:", error);
        alert("Nie udało się pobrać rekomendacji!");
    }
}
