let collapseBtn = document.querySelector('.collapse-button');
let arrow = document.querySelector('.arrow');
let clickableRows = document.querySelectorAll('.clickable-row');

if (collapseBtn) {
    collapseBtn.addEventListener('click', (e) => {
        arrow.classList.toggle('down');
    });
}

if (clickableRows) {
    clickableRows.forEach((row) => {
        row.addEventListener('click', (e) => {
            window.location = row.dataset.href;
        });
    });
}