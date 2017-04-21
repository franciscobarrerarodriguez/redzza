$(document).on("ready", function () {
  // Init all aropdown
  $(".dropdown-button").dropdown();
  /* Init button for mobile-devices */
  $(".button-collapse").sideNav();
  /* Init parallax */
  $('.parallax').parallax();
/* Init tabs */
$('ul.tabs').tabs({'swipeable':'true'});
});
