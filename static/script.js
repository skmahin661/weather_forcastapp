document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", () => {
            const btn = document.querySelector("button");

            if (btn) {
                btn.innerHTML = "⏳ Predicting...";
                btn.disabled = true;
            }
        });
    }

    const result = document.querySelector(".prediction h2");

    if (result) {
        if (result.innerText.includes("Sunny")) {
            document.body.style.background =
                "linear-gradient(135deg,#FFD54F,#FF9800,#4FC3F7,#29B6F6)";
        } else {
            document.body.style.background =
                "linear-gradient(135deg,#607D8B,#455A64,#90A4AE,#78909C)";
        }

        document.body.style.backgroundSize = "400% 400%";
    }
});