export function initApiModal() {
    const modal = document.getElementById('apiModal');

    window.showApiModal = () => modal.classList.remove('hidden');
    window.closeApiModal = () => modal.classList.add('hidden');

    window.onclick = (event) => {
        if (event.target === modal) {
            modal.classList.add('hidden');
        }
    };
}