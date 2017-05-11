$(document).on("ready", function () {
  /* Init select */
  $('select').material_select();
  /* Init all aropdown */
  $(".dropdown-button").dropdown();
  /* Init button for mobile-devices */
  $(".button-collapse").sideNav();
  /* Init parallax */
  $('.parallax').parallax();
  /* Init tabs */
  $('ul.tabs').tabs({'swipeable':'true'});
  /* Init modals */
  // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
  $('.modal').modal();

  /* Update email form user */
  $('#new-email').click(function(e) {
    e.preventDefault();
    var email1 = $("input[id='email-1']");
    var email2 = $("input[id='email-2']");
    if (email1.val() == email2.val()) {
      console.log("iguales");
    }else {
      $(email1).addClass("invalid");
      $(email2).addClass("invalid");
      $("label[for='email-1']").attr("data-error", "Los correos no coinciden");
    }
  });

  /* Update user */
  $('#update-user').click(function (e) {
    e.preventDefault();
    var newUser = $("input[id='new-username']");//falta val
    console.log("Cambiar user");
  });

  /* Update user's password */
  $('#update-password').click(function (e) {
    e.preventDefault();
    var password1 = $("input[id='new-password']");
    var password2 = $("input[id='new-password-2']");
    if (password1.val() == password2.val()) {
      console.log("son iguales");
    }else {
      $(password1).addClass("invalid");
      $(password2).addClass("invalid");
      $("label[for='new-password']").attr("data-error", "Las contraseñas no coinciden");
    }
  });

  /* Update user's phone */
  $('#update-phone').click(function (e) {
    e.preventDefault();
    var newPhone = $("input[id='new-phone']");//falta val
    console.log('update phone');
  });

  /* Update user's address */
  $('#update-address').click(function (e) {
    e.preventDefault();
    var newAddress = $("input[id='new-address']");
    console.log("Update address");
  });

});

function ajaxGetPostCall(dataUrl, data) {

}
