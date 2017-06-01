$(document).ready(function () {
  $('#product-post, #service-post').hover(function () {
    $(this).addClass('z-depth-5');
  }, function () {
    $(this).removeClass('z-depth-5');
  });
});
