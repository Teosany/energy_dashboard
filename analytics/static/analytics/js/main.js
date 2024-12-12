import {initCharts} from './charts.js';
import {initFileUpload} from './file-upload.js';
import {initApiModal} from './api-modal.js';
import { initPagination } from './pagination.js';

document.addEventListener('DOMContentLoaded', () => {
    initCharts();
    initFileUpload();
    initApiModal();
    initPagination();
});