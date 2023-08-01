const addToggleCollapseBtnEvent = () => {
    const collapseBtn = document.querySelector('.collapse-button')
    const arrow = document.querySelector('.arrow')
    if (!collapseBtn) {
        return
    }
    collapseBtn.addEventListener('click', (e) => {
        arrow.classList.toggle('down')
    })
}

const addClickEventToDropdownMenuOptions = () => {
    const dropdownMenuOption = document.querySelectorAll('.dropdown-btn')
    if (!dropdownMenuOption) {
        return
    }
    dropdownMenuOption.forEach((option) => {
        option.addEventListener('click', function() {
            this.classList.toggle('active')
            this.nextElementSibling.classList.toggle('open')
        })
    })
}

const highlightCurrentSidebarItem = () => {
    const sidebarItems = document.querySelectorAll('.sidebar-top a:not(.logo)')
    if (!sidebarItems) {
        return
    }
    sidebarItems.forEach((item) => {
        const dropdownBtn = item.parentElement.previousElementSibling
        if (window.location.href.split(/[#?]/)[0] !== item.href){
            item.classList.remove('current')
            if (dropdownBtn && dropdownBtn.classList.contains('dropdown-btn')){
                dropdownBtn.classList.remove('active')
                item.parentElement.classList.remove('open')
            }
            return
        }
        item.classList.add('current')
        if (dropdownBtn && dropdownBtn.classList.contains('dropdown-btn')){
            dropdownBtn.classList.add('active')
            item.parentElement.classList.add('open')
        }
    })
}

const updateLinkFieldInputs = () => {
    const linkFieldInputs = document.querySelectorAll('.copy-link-field-input')
    if (!linkFieldInputs) {
        return
    }
    linkFieldInputs.forEach((input) => {
        input.innerText = `${window.location.origin}${input.innerText.trim()}`
    })
}

const addClickEventToCopyLinkBtns = () => {
    const widgetInfoCopyLinkBtns = document.querySelectorAll('.widget-info .simple-btn')
    if (!widgetInfoCopyLinkBtns) {
        return
    }
    widgetInfoCopyLinkBtns.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            e.preventDefault()
            let {token} = btn.dataset
            copyWidgetLinkToClipboardFromButton(btn, token)
        })
    })
}

const copyLinkFieldToClipboard = (id) => {
    let copyText = document.getElementById(id)
    let range = document.createRange()
    range.selectNode(copyText)
    window.getSelection().removeAllRanges()
    window.getSelection().addRange(range)
    navigator.clipboard.writeText(window.location.origin + copyText.dataset.value)
    let btn = copyText.parentElement.parentElement.querySelector('.simple-btn')
    btn.style.maxWidth = `${btn.offsetWidth}px`
    let btnHtml = btn.innerHTML
    btn.innerText = 'Скопійовано!'
    setTimeout(() => {
        btn.style.maxWidth = 'initial'
        btn.innerHTML = btnHtml
    }, 3000)
}

const copyWidgetLinkToClipboardFromButton = (btn, token) => {
    let copyText = `${window.location.origin}/user-widgets/${token}`
    navigator.clipboard.writeText(copyText)
    btn.style.maxWidth = `${btn.offsetWidth}px`
    let btnHtml = btn.innerHTML
    btn.innerText = 'Скопійовано!'
    setTimeout(() => {
        btn.style.maxWidth = 'initial'
        btn.innerHTML = btnHtml
    }, 3000)
}

document.addEventListener('htmx:pushedIntoHistory', (event) => {
    addToggleCollapseBtnEvent()
    highlightCurrentSidebarItem()
    updateLinkFieldInputs()
    addClickEventToCopyLinkBtns()
})

addToggleCollapseBtnEvent()
addClickEventToDropdownMenuOptions()
highlightCurrentSidebarItem()
updateLinkFieldInputs()
addClickEventToCopyLinkBtns()
