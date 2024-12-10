export function initApiModal() {
    const modal = document.getElementById('apiModal');
    const closeButton = document.getElementById('closeApiModal');

    window.showApiModal = () => modal.classList.remove('hidden');
    window.closeApiModal = () => modal.classList.add('hidden');

    closeButton?.addEventListener('click', closeApiModal);

    window.onclick = (event) => {
        if (event.target === modal) {
             closeApiModal()
        }
    };
}