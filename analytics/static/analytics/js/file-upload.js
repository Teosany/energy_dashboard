export function initFileUpload() {
    let form = document.getElementById('uploadForm');
    let drop = document.querySelector('.border-dashed');
    let input = document.getElementById('file-upload');

    if (!form || !input) return;

    input.onchange = () => form.submit();

    if (drop) {
        drop.ondragover = e => e.preventDefault();
        drop.ondrop = e => {
            e.preventDefault();
            input.files = e.dataTransfer.files;
            form.submit();
        };
    }
}