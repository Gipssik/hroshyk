const isIframe = window.location !== window.parent.location
window.onload = () => {
  const containerBtn = document.querySelector(".donation-page-form-container.container > form > .submit-btn")
  const submitBtn = containerBtn.querySelector("button")
  if (isIframe) {
    const twitchBtn = document.createElement("div")
    twitchBtn.innerText = "Скинути грошик"
    twitchBtn.classList.add("twitch-btn")
    submitBtn.remove()
    containerBtn.appendChild(twitchBtn)
  }
}