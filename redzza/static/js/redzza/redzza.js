// https://developer.mozilla.org/en-US/docs/Web/API
var generalSpeed = 1000;

$(document).ready(function () {
  /* Scroll to first section */
  $("#chev").click(function () {
    $("html, body").animate({
      scrollTop: $("#first").offset().top
    }, generalSpeed);
  });

  /* form-signup actions */
  $('#form_signup').submit(function (e) {
    e.preventDefault();
    var response = $("#signup_response");
    if ($('#terms-checkbox').is(":checked")) {
      var input = $("#signup_input");
      var url = input.attr("data-url") + "?email=" + input.val();
      $.get(url, function (data) {
        if (data.is_taken) {
          response.html("<p class='danger-alert'>Este correo ya tiene una cuenta asociada, prueba iniciando sesion.</p>");
        } else {
          sessionStorage.setItem("email", input.val());
          window.location.href = $("#form_signup").attr("data-url");
        }
      });
    } else {
      response.html("<p class='danger-alert'>Para registrarte debes aceptar nuestros terminos y condiciones.</p>");
    }
  });
  /* ./form_signup */

  /* form-login actions, if it's true redirect to home, if isn't rendering error */
  $('#form_login').submit(function (e) {
    e.preventDefault();
    var form = $(this);
    $.post(form.attr('data-url'), form.serialize(), function (response, status, jqXHR) {
      if (response.success) {
        window.location.href = response.url;
      }else{
        document.getElementById('login-response').innerHTML = `<p class="danger-alert">${response.errors.__all__[0]}</p>`
      }
    });
  });
  /* ./form_login */

});

/* Landing functions */
function notMember() {
  closeModal('modal-login');
  getModal('modal-signup');
}

/* Display de modal by id */
function getModal(modalId) {
  var modal = document.getElementById(modalId);
  modal.style.display = 'block';
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
}

/* Hidde modal by id */
function closeModal(modalId) {
  document.getElementById(modalId).style.display = 'none';
}
