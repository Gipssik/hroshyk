
window.onload = () => {
  const isIframe = window.location !== window.parent.location
  const containerBtn = document.querySelector("#main-wrapper > div > div.donation-page-form-container > form > div.submit-btn")
  const submitBtn = containerBtn.querySelector("button")
  if (isIframe) {
    const twitchBtn = document.createElement("div")
    twitchBtn.innerText = gettext('Send Hroshyk')  // gettext is a function from Django
    twitchBtn.classList.add("twitch-btn")
    submitBtn.remove()
    containerBtn.appendChild(twitchBtn)
  }
}