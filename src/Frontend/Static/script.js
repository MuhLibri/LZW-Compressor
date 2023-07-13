const backendUrl = 'https://lzw-compressor13521047-production.up.railway.app'

fetchHistory();
const myForm = document.getElementById('form1');

myForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);

    fetch(backendUrl, {
        method: 'post',
        body: formData
    })
        .then(response => response.json())
        .then(response => {displayData(response);
    })
    .catch(function (error) {
        console.log(error);
    })
    fetchHistory();
})

function displayData(response) {
    console.log(response);

    const element1 = document.getElementById('ans1');
    element1.textContent = response['enc_result'];

    const element2 = document.getElementById('ans2');
    element2.textContent = response['dec_result'];

}

function fetchHistory() {
    fetch(backendUrl + '/history', {
    method: 'get',
    })
    .then(response => response.json())
    .then(response => {
        displayHistoryTable(response);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayHistoryTable(response) {
    console.log(response)

    const tableBody = document.querySelector("#history_table tbody");
    tableBody.innerHTML = '';

    response.forEach(response => {
        const row = document.createElement("tr");
        row.innerHTML = `<td>${response.name}</td><td>${response.user_input}</td><td>${response.output}</td>`;
        tableBody.appendChild(row);
    });
}