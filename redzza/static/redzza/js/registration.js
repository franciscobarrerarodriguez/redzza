$(document).ready(function() {
  /* Init AOS (animate on scroll) */
  AOS.init();
  /* Init parallax container */
  $('.parallax').parallax();

  /* Save info in sessionStorage and Redirect to step2 */
  $('#form_profile_info').submit(function (e) {
    e.preventDefault();
    var password1 = $("input[name=password]").val();
    var password2 = $("input[name=password_2]").val();
        if (password1 == password2) {
          if (password1.length >= 6) {
            sessionStorage.setItem('name', $("input[name='name']").val()); // Name
            sessionStorage.setItem('last_name', $("input[name='last_name']").val()); // Lastname
            sessionStorage.setItem('password', password1); // Password
            sessionStorage.setItem('place', $('#places').find(":selected").val()); // Place
            window.location.href = $(this).attr('data-url'); // Redirecting to step 2
          }else {
            $("input[name='password']").addClass("invalid");
            $("label[for='password']").attr("data-error", "La contraseña debe tener mínimo 6 caracteres");
          }
      } else {
        $("input[name='password']").addClass("invalid");
        $("input[name='password_2']").addClass("invalid");
        $("label[for='password']").attr("data-error", "Las contraseñas no coinciden");
      }
  });
  /* ./form-profile-info */

  /* Categories I search  and redirect to step 3 */
  $('#form_profile_info_2').submit(function (e) {
    e.preventDefault();
    var checked = $('#form_profile_info_2').find('input[type="checkbox"]:checked');
    if (checked.length > 0 && checked.length <= 5) {
      var aux = new Array();
      checked.each(function (checkbox) {
        aux.push({pk:$(this).attr('id')});
      });
      sessionStorage.setItem('i_search', JSON.stringify(aux));
      window.location.href = $('#form_profile_info_2').attr('data-url');
    } else {
      Materialize.toast('Debes seleccionar al menos una categoria y máximo 5, llevas ' + checked.length, 4000) // 4000 is the duration of the toast
    }
  });
  /* ./categories I search */

  /* Categories I have and redirect to home */
  $('#form_profile_info_3').submit(function (e) {
    e.preventDefault();
    var checked = $('#form_profile_info_3').find('input[type="checkbox"]:checked');
    var aux = new Array(); // I have categories
    if (checked.length > 0 && checked.length <= 5) {
      checked.each(function (checkbox) {
        aux.push({pk:$(this).attr("id")});
      });
      $.ajax({
        type: "POST",
        url: $(this).attr("data-url"),
        data: {
          userFacebook: sessionStorage.getItem("userFacebook"),
          email: sessionStorage.getItem("email"),
          name: sessionStorage.getItem("name"),
          last_name: sessionStorage.getItem("last_name"),
          password: sessionStorage.getItem("password"),
          place: sessionStorage.getItem('place'),
          i_search: sessionStorage.getItem('i_search'),
          i_have: JSON.stringify(aux),
          suggesting: $('#textarea1').val(),
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
      Materialize.toast('Debes seleccionar al menos una categoria y máximo 5, llevas ' + checked.length , 4000) // 4000 is the duration of the toast
    }
  });
  /* ./categories I have */

});

function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}
