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
      $.post($(this).attr('data-url'), $(this).serialize(), function (response) {
        if (response.success == true) {
          $('#modal1').modal('close');
          $('#new-email').trigger('reset');
          Materialize.toast(response.msg, 4000)
        } else if (response.success == false) {
          Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
        }
      });
    } else {
      $(email1).addClass("invalid");
      $(email2).addClass("invalid");
      $("label[for='email-1']").attr("data-error", "Los correos no coinciden");
    }
  });

  /* Update user */
  $('#update-user').submit(function (e) {
    e.preventDefault();
    $.post($(this).attr('data-url'), $(this).serialize(), function (response) {
      if (response.success == true) {
        $('#modal2').modal('close');
        $('#update-user').trigger('reset');
        Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
      } else if (response.success == false) {
        Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
        console.log("paila");
      }
    });
  });

  /* Update user's password */
  $('#update-password').submit(function (e) {
    e.preventDefault();
    var password1 = $("input[id='new-password']");
    var password2 = $("input[id='new-password-2']");
    if (password1.val() == password2.val()) {
      $.post($(this).attr('data-url'), $(this).serialize(), function (response) {
        if (response.success == true) {
          $('#modal3').modal('close');
          $('#update-password').trigger('reset');
          Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
        } else if (response.success == false){
          Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
        }
      });
    }else {
      $(password1).addClass("invalid");
      $(password2).addClass("invalid");
      $("label[for='new-password']").attr("data-error", "Las contraseñas no coinciden");
    }
  });

  /* Update user's gender */
  $('#update-gender').submit(function (_evt) {
    _evt.preventDefault();
    $.post($(this).attr('data-url'), $(this).serialize(), function (response) {
      if (response.success == true) {
        Materialize.toast("Guardado", 4000) // 4000 is the duration of the toast
      } else if (response.success == false) {
        Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
              }
    });
  });

  /* Update user's phone */
  $('#update-phone').submit(function (e) {
    e.preventDefault();
    // var newPhone = $("input[id='new-phone']");//falta val
    $.post($(this).attr('data-url'), $(this).serialize(), function (response) {
      if (response.success == true) {
        $('#modal5').modal('close');
        $('#update-phone').trigger('reset');
        Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
      } else if (response.success == false) {
        Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
      }
    });
  });

  /* Update user's address */
  $('#update-location').submit(function (e) {
    e.preventDefault();
    // var newAddress = $("input[id='new-address']");//Direccion o ubicacion preguntar a Larry?
    $.post($(this).attr('data-url'), $(this).serialize(), function (response) {
      if (response.success == true) {
        $('#modal6').modal('close');
        $('#update-address').trigger('reset');
        Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
      } else if (response.success == false) {
        Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
      }
    });
  });

  /* Update user's bio */
  $('#update-bio').submit(function (_evt) {
    _evt.preventDefault();
    $.post($(this).attr('data-url'), $(this).serialize(), function (response) {
      if (response.success == true) {
        $('#modal7').modal('close');
        $('#update-bio').trigger('reset');
        Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
      } else if (response.success == false) {
        Materialize.toast(response.msg, 4000) // 4000 is the duration of the toast
      }
    });
  });

  /* Post */
  $('#product-post').click(function (e) {
    e.preventDefault();
    sessionStorage.setItem('thing', 'P');
    window.location.href = $(this).attr('data-url');
  });

  $('#service-post').click(function (e) {
    e.preventDefault();
    sessionStorage.setItem('thing', 'S');
    window.location.href = $(this).attr('data-url');
  });

  if ($('#post-prefer').length) {
    var postPrefer = $('#post-prefer');
    $.get(postPrefer.attr('data-url'), function (json) {
      var categories = JSON.parse(json);
      categories.map(function (categorie, index) {
        $(postPrefer).append(`<option value="${categorie.pk}">${capitalize(categorie.fields.name)}</option>`);
        /* Init select for places */
        $(postPrefer).material_select();
      });
    });
  }
  /*Load post place*/
  if ($("#post-place").length) {
    loadPlaces("#post-place");
  }
  /*Load post place ad*/
  if ($("#post-place-ad").length) {
    loadPlaces("#post-place-ad");
  }

  $("#post-step1").click(function (e) {
    e.preventDefault();
    $("#row-1").addClass("hide");
    $("#row-2").removeClass("hide");
  });

  $("#back-step1").click(function (e) {
    e.preventDefault();
    $("#row-2").addClass("hide");
    $("#row-1").removeClass("hide");
  });

  $("#post-step2").click(function (e) {
    e.preventDefault();
    $("#row-2").addClass("hide");
    $("#row-3").removeClass("hide");
  });

  $("#back-step2").click(function (e) {
    e.preventDefault();
    $("#row-3").addClass("hide");
    $("#row-2").removeClass("hide");
  });

  $("#end-post").click(function (e) {
    e.preventDefault();
    alert("post");
  });
  /* ./post */
});

/* Load all places */
function loadPlaces(tag) {
  $.get($(tag).attr("data-url"), function (json) {
    var places = JSON.parse(json);
    places.map(function (place, index) {
      $(tag).append(`<option value="${place.pk}">${capitalize(place.fields.name)}</option>`);
      /* Init select for places */
      $(tag).material_select();
    });
  });
}

function ajaxPostCall(dataUrl, data) {
  var json;
  $.post(dataUrl, data, function (response) {
    json = response;
  });
  return json;
}

function capitalize(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}
