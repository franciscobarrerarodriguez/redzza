// https://developer.mozilla.org/en-US/docs/Web/API

/* Menu variables */
var isOpen = false; //nav-menu status
var navButton = document.getElementById('nav-button');
var closeButton = document.getElementById('nav-close-button');
var buttonNotMember = document.getElementById('button-not-member');
var navMenu = document.getElementById('nav-menu');

var containerAll = document.getElementById('container-all');
var all = document.getElementById('all');

(function () {
  navButton.addEventListener('click', openMenu); // Listener open menu
  closeButton.addEventListener('click', closeMenu); // Close menu
  containerAll.addEventListener('click', function () { // Close menu when it's open
  if (isOpen) {
    closeMenu();
  }
});
})();

function openMenu() {
  navMenu.style.width = '250px';
  all.style.marginLeft = '250px';
  isOpen = true;
}

function closeMenu() {
  navMenu.style.width = '0';
  all.style.marginLeft = '0';
  document.body.style.backgroundColor = "white";
  isOpen = false;
}
