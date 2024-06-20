document.addEventListener('DOMContentLoaded', function() {
    const labelsMjeseciElement = document.getElementById('labels_mjeseci');
    const dataMjeseciElement = document.getElementById('data_mjeseci');

    if (labelsMjeseciElement && dataMjeseciElement) {
        const labelsMjeseci = JSON.parse(labelsMjeseciElement.textContent);
        const dataMjeseci = JSON.parse(dataMjeseciElement.textContent);

        var barCtx = document.getElementById('barChart').getContext('2d');
        var barChart = new Chart(barCtx, {
            type: 'bar',
            data: {
                labels: labelsMjeseci,
                datasets: [{
                    label: 'Reklamacije po mjesecima',
                    data: dataMjeseci,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Mjeseci'
                        }
                    },
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Broj reklamacija'
                        }
                    }
                }
            }
        });
    }

    const labelsStatusElement = document.getElementById('labels_status');
    const dataStatusElement = document.getElementById('data_status');

    if (labelsStatusElement && dataStatusElement) {
        var pieCtx = document.getElementById('pieChart').getContext('2d');
        var pieChart = new Chart(pieCtx, {
            type: 'pie',
            data: {
                labels: JSON.parse(labelsStatusElement.textContent),
                datasets: [{
                    label: 'Status reklamacija',
                    data: JSON.parse(dataStatusElement.textContent),
                    backgroundColor: [
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(255, 99, 132, 0.2)'
                    ],
                    borderColor: [
                        'rgba(75, 192, 192, 1)',
                        'rgba(255, 99, 132, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: true,
                        position: 'bottom'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(tooltipItem) {
                                return tooltipItem.label + ': ' + tooltipItem.raw;
                            }
                        }
                    }
                }
            }
        });
    }
});

function showAddForm() {
    document.getElementById('addForm').style.display = 'block';
}

function closeAddForm() {
    document.getElementById('addForm').style.display = 'none';
}

function showSearchForm() {
    document.getElementById('searchForm').style.display = 'block';
}

function closeSearchForm() {
    document.getElementById('searchForm').style.display = 'none';
}

function showEditForm() {
    document.getElementById('editForm').style.display = 'block';
}

function closeEditForm() {
    document.getElementById('editForm').style.display = 'none';
}

function editReklamacija(idReklamacije, brojNarudzbe, kupac, datumReklamacije, opis, status) {
    document.getElementById('edit_id_reklamacije').value = idReklamacije;
    document.getElementById('edit_broj_narudzbe').value = brojNarudzbe;
    document.getElementById('edit_kupac').value = kupac;
    document.getElementById('edit_datum_reklamacije').value = datumReklamacije;
    document.getElementById('edit_opis').value = opis;
    document.getElementById('edit_status').value = status;
    document.getElementById('editFormContainer').action = '/uredi/' + idReklamacije;
    showEditForm();
}

function sortReklamacije() {
    var sortValue = document.getElementById('sortSelect').value;
    window.location.href = '/reklamacije?sort=' + sortValue;
}

function confirmDelete(idReklamacije) {
    var confirmForm = document.getElementById('confirmDeleteForm');
    confirmForm.style.display = 'block';
    document.getElementById('confirmDeleteYes').onclick = function() {
        document.getElementById('deleteForm_' + idReklamacije).submit();
    };
    document.getElementById('confirmDeleteNo').onclick = function() {
        confirmForm.style.display = 'none';
    };
}

window.showAddForm = showAddForm;
window.closeAddForm = closeAddForm;
window.showSearchForm = showSearchForm;
window.closeSearchForm = closeSearchForm;
window.showEditForm = showEditForm;
window.closeEditForm = closeEditForm;
window.editReklamacija = editReklamacija;
window.sortReklamacije = sortReklamacije;
window.confirmDelete = confirmDelete;


