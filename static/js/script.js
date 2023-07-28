let collapseBtn = document.querySelector('.collapse-button');
let arrow = document.querySelector('.arrow');
let clickableRows = document.querySelectorAll('.clickable-row');
let dropdownMenuOption = document.querySelectorAll(".dropdown-btn");
let sidebarItems = document.querySelectorAll('.sidebar-top a:not(.logo)');
let linkFieldInputs = document.querySelectorAll('.copy-link-field-input');
let widgetInfoCopyLinkBtns = document.querySelectorAll('.widget-info .simple-btn');

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

if (dropdownMenuOption) {
    dropdownMenuOption.forEach((option) => {
        option.addEventListener("click", function() {
            this.classList.toggle("active");
            this.nextElementSibling.classList.toggle("open");
        });
    });
}

if (sidebarItems) {
    sidebarItems.forEach((item) => {
        if (window.location.href !== item.href.split('#')[0]){
            return;
        }
        item.classList.toggle('current');
        let dropdownBtn = item.parentElement.previousElementSibling;
        if (dropdownBtn && dropdownBtn.classList.contains('dropdown-btn')){
            dropdownBtn.classList.toggle('active');
            item.parentElement.classList.toggle('open');
        }
    });
}

if (linkFieldInputs) {
    linkFieldInputs.forEach((input) => {
        input.innerText = `${window.location.origin}${input.innerText.trim()}`;
    });
}

if (widgetInfoCopyLinkBtns) {
    widgetInfoCopyLinkBtns.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            let {token} = btn.dataset;
            copyWidgetLinkToClipboardFromButton(btn, token);
        });
    });
}

const copyLinkFieldToClipboard = (id) => {
    let copyText = document.getElementById(id);
    let range = document.createRange();
    range.selectNode(copyText);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    navigator.clipboard.writeText(window.location.origin + copyText.dataset.value);
    let btn = copyText.parentElement.parentElement.querySelector('.simple-btn');
    btn.style.maxWidth = `${btn.offsetWidth}px`;
    let btnHtml = btn.innerHTML;
    btn.innerText = 'Скопійовано!';
    setTimeout(() => {
        btn.style.maxWidth = 'initial';
        btn.innerHTML = btnHtml;
    }, 3000);
}

const copyWidgetLinkToClipboardFromButton = (btn, token) => {
    let copyText = `${window.location.origin}/user-widgets/${token}`;
    navigator.clipboard.writeText(copyText);
    btn.style.maxWidth = `${btn.offsetWidth}px`;
    let btnHtml = btn.innerHTML;
    btn.innerText = 'Скопійовано!';
    setTimeout(() => {
        btn.style.maxWidth = 'initial';
        btn.innerHTML = btnHtml;
    }, 3000);
}
