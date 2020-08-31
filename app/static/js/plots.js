function createUsualPlot(fetchedData) {
    const usualPlot = {
        x: fetchedData.timeline.map(obj => obj.date),
        y: fetchedData.timeline.map(obj => obj.value),
        type: 'scatter'
    };

    const data = [usualPlot];

    const layout = {
        title: 'Usual plot, made with: ' +
            '/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=usual&Grouping=monthly&stars=5'
    };

    Plotly.newPlot('usualPlotContainer', data, layout);
}

function createCumulativePlot(fetchedData) {
    const cumulativePlot = {
        x: fetchedData.timeline.map(obj => obj.date),
        y: fetchedData.timeline.map(obj => obj.value),
        type: 'scatter'
    };

    const data = [cumulativePlot];

    const layout = {
        title: 'Cumulative plot, made with: ' +
            '/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=cumulative&Grouping=monthly&stars=5'
    };


    Plotly.newPlot('cumulativePlotContainer', data, layout);
}


function main() {
    fetch("/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=usual&Grouping=monthly&stars=5")
        .then(response => response.json())
        .then(data => createUsualPlot(data))
        .catch(err => console.error(err))

    fetch("/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=cumulative&Grouping=monthly&stars=5")
        .then(response => response.json())
        .then(data => createCumulativePlot(data))
        .catch(err => console.error(err))
}

window.onload = main
