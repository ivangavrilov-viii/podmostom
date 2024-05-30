function clickToRent() {
    const scroll_to = document.getElementById('rent').offsetTop;
    window.scrollTo({top: scroll_to, behavior: "smooth",});
}

function redirectToFootball() {
    window.location = '/football/'
}

function redirectToBasketball() {
    window.location = '/basketball/'
}

function redirectToHistory() {
    window.location = '/history/'
}
