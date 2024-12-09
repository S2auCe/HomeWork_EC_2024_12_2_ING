function showSection(id) {
    document.querySelectorAll('.content').forEach(el => el.classList.remove('active'));
    document.getElementById(id).classList.add('active');

    const csvFiles = {
        'section1': ".\\priceOfVegetables1.csv",
        'section2': ".\\priceOfVegetables.csv",
        'section3': ".\\asianStock.csv",
        'section4': ".\\EuroStock.csv",
        'section5': ".\\AmericaStock.csv"
    };

    if (csvFiles[id]) {
        loadCSV(csvFiles[id], id);
    }
}

function loadCSV(targetIndex, sectionId) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', targetIndex, true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            processCSV(xhr.responseText, sectionId);
        } else {
            console.error('Failed to load CSV file');
        }
    };
    xhr.send();
}

function processCSV(text, sectionId) {
    const rows = text.split('\n');
    const table = document.querySelector(`#${sectionId} table`);
    let html = '';

    const headers = {
        'section1': ['发布日期', '菜名', '价格(元/斤)'],
        'section2': ['名称', '高', '中', '低', '产地'],
        'section3': ['股票名称', '开盘价', '涨跌', '涨跌幅', '最高价', '最低价'],
        'section4': ['股票名称', '开盘价', '涨跌', '涨跌幅', '最高价', '最低价'],
        'section5': ['股票名称', '开盘价', '涨跌', '涨跌幅', '最高价', '最低价']
    };

    if (headers[sectionId]) {
        html += '<tr>';
        headers[sectionId].forEach(header => {
            html += `<th>${header}</th>`;
        });
        html += '</tr>';
    }

    rows.forEach((row, index) => {
        const cells = row.split(',');
        html += '<tr>';
        cells.forEach(cell => {
            html += `<td>${cell}</td>`;
        });
        html += '</tr>';
    });

    table.querySelector('tbody').innerHTML = html;
}
