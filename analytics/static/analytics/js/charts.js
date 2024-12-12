export function initCharts() {
    const chart = document.getElementById('energyChart');
    if (!chart || window.currentChart) return;

    let chartData = {
        region: {
            labels: JSON.parse(chart.dataset.regionLabels || '[]'),
            values: JSON.parse(chart.dataset.regionValues || '[]')
        },
        year: {
            labels: JSON.parse(chart.dataset.yearLabels || '[]'),
            values: JSON.parse(chart.dataset.yearValues || '[]')
        }
    };

    let config = {
        responsive: true,
        maintainAspectRatio: false,
        animation: true,
        plugins: { legend: { position: 'top' } },
        scales: {
            x: { ticks: { maxRotation: 45, minRotation: 45 } },
            y: {
                beginAtZero: true,
                title: { display: true, text: 'TWh' }
            }
        }
    };

    function makeChart(type) {
        if (window.currentChart) {
            window.currentChart.destroy();
        }

        let ctx = chart.getContext('2d');
        let isYears = type === 'years';

        window.currentChart = new Chart(ctx, {
            type: isYears ? 'line' : 'bar',
            options: config,
            data: {
                labels: chartData[isYears ? 'year' : 'region'].labels,
                datasets: [{
                    label: 'Consommation (TWh)',
                    data: chartData[isYears ? 'year' : 'region'].values,
                    backgroundColor: '#3b82f6',
                    borderColor: isYears ? '#3b82f6' : undefined,
                    fill: !isYears
                }]
            }
        });
    }

    let buttons = document.querySelectorAll('[data-view]');
    buttons.forEach(btn => {
        btn.onclick = (e) => {
            buttons.forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            makeChart(e.target.dataset.view);
        };
    });

    makeChart('regions');
}