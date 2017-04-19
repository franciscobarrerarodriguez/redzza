$(document).ready(function() {
  /* Init AOS (animate on scroll) */
  AOS.init();
  /* Init parallax container */
  $('.parallax').parallax();
  /* Load all places */
  if ($("#places").length) {
    $.get($("#places").attr("data-url"), function (json) {
      var places = JSON.parse(json);
      places.map(function (place, index) {
        $("#places").append(`<option value="${place.pk}">${capitalize(place.fields.name)}</option>`);
        /* Init select for places */
        $("#places").material_select();
      });
    });
  }
  /* Save info in sessionStorage and Redirect to step2 */
  $('#form_profile_info').submit(function (e) {
    e.preventDefault();
    if ($("input[name='password']").val() == $("input[name='password_2']").val()) {
      sessionStorage.setItem('name', $("input[name='name']").val()); // Name
      sessionStorage.setItem('last_name', $("input[name='last_name']").val()); // Lastname
      sessionStorage.setItem('password', $("input[name='password']").val()); // Password
      sessionStorage.setItem('place', $('#places').find(":selected").val()); // Place
      window.location.href = $(this).attr('data-url'); // Redirecting to step 2
    } else {
      $("input[name='password']").addClass("invalid");
      $("input[name='password_2']").addClass("invalid");
      $("label[for='password']").attr("data-error", "Las contraseñas no coinciden");
    }
  });
  /* ./form-profile-info */

  /* Load all categories */
  if($("#categories").length){
    $.get($("#categories").attr("data-url"), function (json) {
      var categories = JSON.parse(json);
      categories.map(function (categorie, index) {
        $("#categories").append(`<p><input type="checkbox" id="${categorie.pk}"/><label for="${categorie.pk}">${categorie.fields.name}</label></p>`);
      });
    });
  }
  /* ./load all categories */

  /* Categories I search  and redirect to step 3 */
  $('#form_profile_info_2').submit(function (e) {
    e.preventDefault();
    var checked = $('#form_profile_info_2').find('input[type="checkbox"]:checked');
    if (checked.length > 0) {
      var aux = new Array();
      checked.each(function (checkbox) {
        aux.push({pk:$(this).attr('id')});
      });
      sessionStorage.setItem('i_search', JSON.stringify(aux));
      window.location.href = $('#form_profile_info_2').attr('data-url');
    } else {
      Materialize.toast('Debes seleccionar al menos una categoria', 4000) // 4000 is the duration of the toast
    }
  });
  /* ./categories I search */

  /* Categories I have and redirect to home */
  $('#form_profile_info_3').submit(function (e) {
    e.preventDefault();
    var checked = $('#form_profile_info_3').find('input[type="checkbox"]:checked');
    var aux = new Array(); // I have categories
    if (checked.length > 0) {
      checked.each(function (checkbox) {
        aux.push({pk:$(this).attr("id")});
      });
      $.ajax({
        type: "POST",
        url: $(this).attr("data-url"),
        data: {
          email: sessionStorage.getItem("email"),
          name: sessionStorage.getItem("name"),
          last_name: sessionStorage.getItem("last_name"),
          password: sessionStorage.getItem("password"),
          place: sessionStorage.getItem('place'),
          i_search: sessionStorage.getItem('i_search'),
          i_have: JSON.stringify(aux),
          csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function (response) {
          if (response.success) {
            window.location.href = response.url;
          } else {
            console.log(response.err);
            // window.location.href = "/";
          }
        }
      });
    } else {
      Materialize.toast('Debes seleccionar al menos una categoria', 4000) // 4000 is the duration of the toast
    }
  });
  /* ./categories I have */

});

function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}
