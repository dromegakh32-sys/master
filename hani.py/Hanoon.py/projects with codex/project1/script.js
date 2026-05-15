const emailInput = document.getElementById("email");
const accountPreview = document.getElementById("accountPreview");

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

function isCompletedEmail(value) {
    const text = value.trim();

    if (!text || text.includes("..")) {
        return false;
    }

    return emailPattern.test(text);
}

emailInput.addEventListener("input", () => {
    const showImage = isCompletedEmail(emailInput.value);
    accountPreview.classList.toggle("show", showImage);
});

