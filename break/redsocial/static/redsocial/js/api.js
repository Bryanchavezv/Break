document.addEventListener("DOMContentLoaded", () => {
    const apiUrl = '/noticias'; // URL de tu vista Django
    const newsContainer = document.getElementById('news-list');

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }
            return response.json();
        })
        .then(data => {
            // Verifica si la respuesta es válida
            if (data.status === 'ok' && Array.isArray(data.articles)) {
                newsContainer.innerHTML = ''; // Limpiar cualquier contenido previo

                // Recorre las noticias y crea elementos para cada una
                data.articles.forEach((article, index) => {
                    // Crear un contenedor para cada noticia
                    const articleDiv = document.createElement('div');
                    articleDiv.className = 'carousel-item';
                    if (index === 0) {
                        articleDiv.classList.add('active'); // Marcar el primer artículo como activo
                    }

                    // Añadir imagen (si está disponible)
                    const image = document.createElement('img');
                    image.className = 'd-block w-100';
                    image.src = article.urlToImage || 'https://via.placeholder.com/800x400'; // Imagen placeholder si no hay imagen
                    image.alt = article.title || 'News Image';

                    // Crear contenedor del texto
                    const textDiv = document.createElement('div');
                    textDiv.className = 'carousel-caption d-none d-md-block';

                    // Añadir título
                    const title = document.createElement('h5');
                    title.textContent = article.title || 'No Title';
                    textDiv.appendChild(title);

                    // Añadir descripción (manejar null o vacío)
                    const description = document.createElement('p');
                    description.textContent = article.description || 'No description available';
                    textDiv.appendChild(description);

                    // Añadir enlace
                    const link = document.createElement('a');
                    link.href = article.url || '#';
                    link.textContent = 'Leer más';
                    link.target = '_blank';
                    textDiv.appendChild(link);

                    // Añadir todos los elementos al contenedor de la noticia
                    articleDiv.appendChild(image);
                    articleDiv.appendChild(textDiv);

                    // Añadir la noticia al carrusel
                    newsContainer.appendChild(articleDiv);
                });
            } else {
                // Maneja el caso cuando no hay noticias disponibles
                newsContainer.innerHTML = '<p>No news available.</p>';
            }
        })
        .catch(error => {
            console.error('Error fetching news:', error);
            // Mostrar un mensaje de error en la página
            newsContainer.innerHTML = '<p>Error fetching news.</p>';
        });
});
