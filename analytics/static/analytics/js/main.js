import { initCharts } from './charts.js';
import { initFileUpload } from './file-upload.js';
import { initApiModal } from './api-modal.js';

document.addEventListener('DOMContentLoaded', () => {
    initCharts();
    initFileUpload();
    initApiModal();
});