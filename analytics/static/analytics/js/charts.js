export function initCharts() {
    const chartElement = document.getElementById('energyChart');
    if (!chartElement) return;

    const data = {
        region: {
            labels: JSON.parse(chartElement.dataset.regionLabels || '[]'),
            values: JSON.parse(chartElement.dataset.regionValues || '[]')
        },
        year: {
            labels: JSON.parse(chartElement.dataset.yearLabels || '[]'),
            values: JSON.parse(chartElement.dataset.yearValues || '[]')
        }
    };

    let chart = null;

    const baseConfig = {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
            legend: { position: 'top' }
        },
        scales: {
            x: {
                ticks: { maxRotation: 45, minRotation: 45 }
            },
            y: {
                beginAtZero: true,
                title: { display: true, text: 'TWh' }
            }
        }
    };

    function createChart(type) {
        const ctx = chartElement.getContext('2d');
        if (chart) chart.destroy();

        chart = new Chart(ctx, {
            options: baseConfig,
            type: type === 'years' ? 'line' : 'bar',
            data: {
                labels: data[type === 'years' ? 'year' : 'region'].labels,
                datasets: [{
                    label: 'Consommation (TWh)',
                    data: data[type === 'years' ? 'year' : 'region'].values,
                    backgroundColor: '#3b82f6',
                    borderColor: type === 'years' ? '#3b82f6' : undefined,
                    fill: type === 'years' ? false : true
                }]
            }
        });
    }

    document.querySelectorAll('[data-view]').forEach(button => {
        button.addEventListener('click', (e) => {
            const buttons = document.querySelectorAll('[data-view]');
            buttons.forEach(btn => {
                btn.className = 'px-4 py-2 rounded-md hover:bg-gray-100';
            });
            e.target.className = 'px-4 py-2 rounded-md bg-blue-500 text-white hover:bg-blue-600';
            createChart(e.target.dataset.view);
        });
    });

    createChart('regions');
}