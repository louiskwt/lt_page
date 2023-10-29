// Init
window.onload = () => {
  const toogleNavBtn = document.getElementById("toggle-nav-btn");
  const sideNav = document.getElementById("side-nav");
  const closeNavBtn = document.getElementById("close-nav-btn");

  toogleNavBtn.addEventListener("click", () => {
    sideNav.classList.replace("translate-x-full", "translate-x-0");
  });

  closeNavBtn.addEventListener("click", () => {
    sideNav.classList.replace("translate-x-0", "translate-x-full");
  });
};
