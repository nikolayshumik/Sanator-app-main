document.addEventListener("DOMContentLoaded", function() {
  var menu = document.querySelector(".menu");
  var menuOpen = document.querySelector(".menuOpen");
  menu.addEventListener("click", function() {
    menuOpen.classList.toggle("show");
  });
});

