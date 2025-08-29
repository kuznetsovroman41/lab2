function getCookie(name) {
    const cookies = document.cookie ? document.cookie.split(';') : [];
    for (let i = 0; i < cookies.length; i++) {
        const [key, ...valParts] = cookies[i].split('=');
        const cookieName = key.trim();
        const value = valParts.join('=');
        if (cookieName === name) return decodeURIComponent(value);
    }
    return null;
}


document.addEventListener('DOMContentLoaded', () => {
    const token = getCookie('auth_token');
    if (!token) return;

    document.querySelectorAll('.like-btn').forEach(btn => {
        btn.onclick = async () => {
            const postId = btn.dataset.id;
            const action = btn.textContent === 'Лайк' ? 'like' : 'unlike';
            const res = await fetch(`/api_v1/posts/${postId}/${action}/`, {
                method: 'POST',
                headers: { 'Authorization': `Token ${token}` }
            });

            if (!res.ok) {
                alert('Ошибка при отправке запроса');
                return;
            }

            const data = await res.json();
            btn.textContent = action === 'like' ? 'Убрать лайк' : 'Лайк';
            document.querySelector(`#likes-count-${postId}`).textContent = data.likes_count;
        };
    });
});
