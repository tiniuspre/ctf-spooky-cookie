document.addEventListener('DOMContentLoaded', () => {
    const ghost = document.getElementById('ghostImg');

    ghost.addEventListener('click', () => {
        window.location.href = "/treasure";
    });
});
