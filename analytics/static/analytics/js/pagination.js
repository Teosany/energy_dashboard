export function initPagination() {
    function loadPage(page) {
        fetch(`?page=${page}`, {
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
        })
        .then(response => {
            if (!response.ok) throw new Error('Network error');
            return response.json();
        })
        .then(data => {
            const content = document.getElementById('table-content');
            const pagination = document.getElementById('pagination');

            if (content) {
                content.innerHTML = data.html;
            }

            if (pagination && pagination.parentNode) {
                const temp = document.createElement('div');
                temp.innerHTML = data.pagination_html;
                pagination.parentNode.replaceChild(temp.firstElementChild, pagination);
            }

            setupButtons();
            history.pushState({}, '', `?page=${page}`);
        })
        .catch(err => console.error('Error:', err));
    }

    function setupButtons() {
        document.querySelectorAll('.pagination-btn').forEach(btn => {
            if (!btn.disabled) {
                btn.onclick = (e) => {
                    e.preventDefault();
                    loadPage(btn.dataset.page);
                };
            }
        });
    }

    setupButtons();
}