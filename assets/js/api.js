// Funcion de la API Noticias
function fetchNews() {
    const apiKey = "f0b00ca53b6e46cda812db9aef58b5d8";
    const url = `https://newsapi.org/v2/top-headlines?country=mx&apiKey=${apiKey}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            const newsTitle = document.getElementById("news-title");
            const newsDescription = document.getElementById("news-description");
            const newsLink = document.getElementById("news-link");
            const publishedAt = document.getElementById("published-at");
            const sourceInfo = document.getElementById("source-info");

            // Mostrar la primera noticia
            displayNews(data.articles[0]);

            // Actualizar las noticias en un intervalo
            let index = 1;
            setInterval(() => {
                if (index >= data.articles.length) {
                    index = 0;
                }
                displayNews(data.articles[index]);
                index++;
            }, 3000); // Cambiar cada 3 segundos
        })
        .catch(error => {
            console.error("Error al obtener las noticias:", error);
        });
}

// Función para mostrar las noticias en una card
function displayNews(article) {
    const newsTitle = document.getElementById("news-title");
    const newsDescription = document.getElementById("news-description");
    const newsLink = document.getElementById("news-link");
    const publishedAt = document.getElementById("published-at");
    const sourceInfo = document.getElementById("source-info");

    newsTitle.textContent = article.title;
    newsDescription.textContent = article.description ? article.description : '';
    newsLink.href = article.url;
    publishedAt.textContent = `Publicado el ${formatDate(article.publishedAt)}`;
    sourceInfo.innerHTML = `<i class="bi bi-person"></i> ${article.author ? article.author : 'Autor desconocido'} - <i class="bi bi-journal"></i> ${article.source.name}`;
}

// Función para el formato de  la fecha de noticia
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' });
}

// Llamar a la función fetchNews al cargar la página
window.onload = fetchNews;
