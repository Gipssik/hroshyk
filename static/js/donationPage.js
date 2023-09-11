var formMappings = {
    'title': ["#main-wrapper > div > div.donation-page-title-block > h1"],
    'title_subtext': ["#main-wrapper > div > div.donation-page-title-block > p"],
    'nickname_placeholder': ["#id_nickname", 'placeholder'],
    'nickname_min_length': ["#id_nickname", 'minlength'],
    'nickname_max_length': ["#id_nickname", 'maxlength'],
    'amount_placeholder': ["#id_amount", 'placeholder'],
    'amount_min': ["#id_amount", 'min'],
    'amount_max': ["#id_amount", 'max'],
    'message_placeholder': ["#id_message", 'placeholder'],
    'message_min_length': ["#id_message", 'minlength'],
    'message_max_length': ["#id_message", 'maxlength'],
    'donate_button_text': ["#main-wrapper > div > div.donation-page-form-container.container > form > div.submit-btn > div"],
    'target_title': ['#main-wrapper > div > div.donation-page-form-container.container > form > div.donation-page-progress-bar > h5'],
    'target_amount': ['#main-wrapper > div > div.donation-page-form-container.container > form > div.donation-page-progress-bar > div > span.progress-bar-target'],
}

var addEventListenersToFields = () => {
    const form = document.querySelector('.form-with-preview form')
    if (!form) {
        return
    }
    for (const [key, value] of Object.entries(formMappings)) {
        const input = form.querySelector(`#id_${key}`)
        const element = document.querySelector(value[0])
        const attribute = value[1] || 'innerText'
        input.addEventListener('input', (event) => {
            if (event.target.value === '') {
                return
            }
            if (attribute === 'innerText') {
                element[attribute] = event.target.value
            }
            else{
                element.setAttribute(attribute, event.target.value)
            }
            if (key === 'target_amount'){
                processTargetAmount(event)
            }
        })
    }
}

var processTargetAmount = (event) => {
    const progressBarContainer = document.querySelector("#main-wrapper > div > div.donation-page-form-container.container > form > div.donation-page-progress-bar > div")
    const progressBar = progressBarContainer.querySelector('.progress-bar')
    const current = progressBarContainer.querySelector('.progress-bar-current')
    const regex = /(\d+).*\((\d+\.\d)%\)/
    const matches = current.innerText.match(regex)
    const [_, currentAmount, currentPercentage] = matches
    const targetAmount = event.target.value
    const targetPercentage = ((currentAmount / targetAmount) * 100).toFixed(1)
    progressBar.style.width = `${targetPercentage}%`
    current.innerText = `${currentAmount} грн (${targetPercentage}%)`
}

document.addEventListener('htmx:pushedIntoHistory', (event) => {
    addEventListenersToFields()
})

addEventListenersToFields()



