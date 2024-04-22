const navbar = ocument.querySelector(".navbar");
const menuButton = document.querySelector(".menu-button");

menuButton.addEventListener("click", ()=> {
    navbar.classList.toggle("show-menu");
});
