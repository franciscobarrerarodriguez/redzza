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
  /* Init date picker
  https://www.theinvestmentassociation.org/assets/components/ima_circularwizard/js/pickadate/docs.htm#formats
  */
  $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year
    format: 'mmm/dd/yyyy'
  });
  /* Init modals */
  // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
  $('.modal').modal();

  /* Update email form user */
  $('#new-email').submit(function (e) {
    e.preventDefault();
    var email1 = $("input[id='email-1']");
    var email2 = $("input[id='email-2']");
    if (email1.val() == email2.val()) {
      var response = ajaxPostCall($(this).attr('data-url'), $(this).serialize());
      if (response.success == true) {
        $('#modal1').modal('close');
      }
      Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
    }else {
      $(email1).addClass("invalid");
      $(email2).addClass("invalid");
      $("label[for='email-1']").attr("data-error", "Los correos no coinciden");
    }
  });

  /* Update user */
  $('#update-user').submit(function (e) {
    e.preventDefault();
    // var newUser = $("input[id='new-username']");//falta val
    var response = ajaxPostCall($(this).attr('data-url'), $(this).serialize());
    if (response.success == true) {
      $('#modal2').modal('close');
    }
    Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
  });

  /* Update user's password */
  $('#update-password').submit(function (e) {
    e.preventDefault();
    var password1 = $("input[id='new-password']");
    var password2 = $("input[id='new-password-2']");
    if (password1.val() == password2.val()) {
      var response = ajaxPostCall($(this).attr('data-url'), $(this).serialize());
      if (response.success == true) {
        $('#modal3').modal('close');
      }
      Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast

    }else {
      $(password1).addClass("invalid");
      $(password2).addClass("invalid");
      $("label[for='new-password']").attr("data-error", "Las contraseñas no coinciden");
    }
  });

  /* Update user's phone */
  $('#update-phone').submit(function (e) {
    e.preventDefault();
    // var newPhone = $("input[id='new-phone']");//falta val
    var response = ajaxPostCall($(this).attr('data-url'), $(this).serialize());
    if (response.success == true) {
      $('#modal5').modal('close');
    }
    Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
  });

  /* Update user's address */
  $('#update-address').submit(function (e) {
    e.preventDefault();
    // var newAddress = $("input[id='new-address']");//Direccion o ubicacion preguntar a Larry?
    var response = ajaxPostCall($(this).attr('data-url'), $(this).serialize());
    if (response.success == true) {
      $('#modal6').modal('close');
    }
    Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
  });

});

function ajaxPostCall(dataUrl, data) {
  var json;
  $.post(dataUrl, data, function (response) {
    json = response;
  });
  return json;
}
