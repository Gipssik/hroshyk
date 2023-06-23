let collapseBtn = document.querySelector('.collapse-button');
let arrow = document.querySelector('.arrow');
let clickableRows = document.querySelectorAll('.clickable-row');
let dropdownMenuOption = document.querySelectorAll(".dropdown-btn");
let linkFieldInputs = document.querySelectorAll('.copy-link-field-input');

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

for (let d of dropdownMenuOption) {
    d.addEventListener("click", function() {
        this.classList.toggle("active");
        this.nextElementSibling.classList.toggle("open");
    });
}

if (linkFieldInputs) {
    linkFieldInputs.forEach((input) => {
        input.innerText = `${window.location.origin}/${input.innerText.trim()}`;
    });
}

const copyLinkToClipboard = (id) => {
    let copyText = document.getElementById(id);
    let range = document.createRange();
    range.selectNode(copyText);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    navigator.clipboard.writeText(copyText.innerText);
    let btn = copyText.parentElement.parentElement.querySelector('.simple-btn');
    btn.style.maxWidth = `${btn.offsetWidth}px`;
    btn.innerText = 'Скопійовано!';
    setTimeout(() => {
        btn.style.maxWidth = 'initial';
        btn.innerText = 'Копіювати';
    }, 3000);
}