export function initFileUpload() {
    const form = document.getElementById('uploadForm');
    const dropZone = document.querySelector('.border-dashed');
    const fileInput = document.getElementById('file-upload');

    if (!form || !fileInput) return;

    fileInput.addEventListener('change', () => form.submit());

    if (dropZone) {
        dropZone.addEventListener('dragover', e => e.preventDefault());
        dropZone.addEventListener('drop', e => {
            e.preventDefault();
            fileInput.files = e.dataTransfer.files;
            form.submit();
        });
    }
}