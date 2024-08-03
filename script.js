function searchLyrics() {
    const query = document.getElementById('search-box').value;
    fetch(`/search?query=${query}`)
        .then(response => response.json())
        .then(data => {
            const results = document.getElementById('results');
            results.innerHTML = '';
            data.response.hits.forEach(hit => {
                const song = hit.result;
                const songElement = document.createElement('div');
                songElement.className = 'song';
                songElement.innerHTML = `<h2>${song.full_title}</h2>`;
                songElement.addEventListener('click', () => {
                    getLyrics(song.id);
                });
                results.appendChild(songElement);
            });
        });
}

function getLyrics(songId) {
    fetch(`/lyrics?song_id=${songId}`)
        .then(response => response.json())
        .then(data => {
            const results = document.getElementById('results');
            results.innerHTML = `<h2>${data.response.song.full_title}</h2><p>${data.response.song.lyrics}</p>`;
        });
}
