document.addEventListener("DOMContentLoaded", () => {

    // ============================
    // Dashboard Fade-in Animation
    // ============================

    const dashboard = document.querySelector(".dashboard");

    if (dashboard) {
        dashboard.style.opacity = "0";
        dashboard.style.transform = "translateY(30px)";

        setTimeout(() => {
            dashboard.style.transition = "all 0.8s ease";
            dashboard.style.opacity = "1";
            dashboard.style.transform = "translateY(0)";
        }, 150);
    }

    // ============================
    // Animate Progress Bars
    // ============================

    const progressBars = document.querySelectorAll(".progress");

    progressBars.forEach(bar => {

        const targetWidth = bar.style.width;

        bar.style.width = "0%";

        setTimeout(() => {
            bar.style.transition = "width 1.5s ease";
            bar.style.width = targetWidth;
        }, 300);

    });

    // ============================
    // Animate Weather Cards
    // ============================

    const cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";
        card.style.transform = "translateY(25px)";

        setTimeout(() => {

            card.style.transition = "all 0.6s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";

        }, 150 * (index + 1));

    });

    // ============================
    // Floating Weather Icon
    // ============================

    const icon = document.querySelector(".icon");

    if (icon) {

        setInterval(() => {

            icon.animate(
                [
                    { transform: "translateY(0px)" },
                    { transform: "translateY(-8px)" },
                    { transform: "translateY(0px)" }
                ],
                {
                    duration: 2200,
                    iterations: 1
                }
            );

        }, 2200);

    }

    // ============================
    // Button Hover Effect
    // ============================

    const buttons = document.querySelectorAll(".btn");

    buttons.forEach(button => {

        button.addEventListener("mouseenter", () => {

            button.style.transform = "translateY(-4px) scale(1.03)";

        });

        button.addEventListener("mouseleave", () => {

            button.style.transform = "translateY(0) scale(1)";

        });

    });

    // ============================
    // Print Report
    // ============================

    const printButton = document.querySelector(".btn.primary");

    if (printButton) {

        printButton.addEventListener("click", () => {

            window.print();

        });

    }

    // ============================
    // Add Current Date & Time
    // ============================

    const footer = document.querySelector("footer");

    if (footer) {

        const now = new Date();

        footer.innerHTML +=
            "<br><small>Generated on: " +
            now.toLocaleString() +
            "</small>";

    }

    // ============================
    // Smooth Scroll (if needed)
    // ============================

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

});