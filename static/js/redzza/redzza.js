// https://developer.mozilla.org/en-US/docs/Web/API

/* Body variables */
var all = document.getElementById('all');

(function () {
  /* form-login actions, if it's true redirect to home, if isn't rendering error */
  $('#form-login').submit(function (e) {
    e.preventDefault();
    var form = $(this);
    $.post(form.attr('data-url'), form.serialize(), function (response, status, jqXHR) {
      if (response.success) {
        window.location.href = response.url;
      }else{
        document.getElementById('login-response').innerHTML = `<p>${response.errors.__all__[0]}</p>`
      }
    });
  });

  /* form-signup actions */
  $('#form-signup').submit(function (e) {
    e.preventDefault();
    var response =  document.getElementById('signup-response');
    if(document.getElementById('terms').checked) {
      var url = $('#signup-input').attr('data-url') + "?email=" + $('#signup-input').val();
      $.get(url, function (data) {
        if (data.is_taken) {
          response.innerHTML = `<p>Este correo ya tiene una cuenta asociada, prueba iniciando sesion.</p>`;
        }else{
          sessionStorage.setItem('email', $('#signup-input').val()); // Save email in sessionStorage
          window.location.href = $('#form-signup').attr('data-url'); // Redirecting to step1
        }
      });
    }else{
      response.innerHTML = `<p>Para iniciar sesión debes aceptar nuestros terminos y condiciones.</p>`;
    }
  });

  /* Save info in sessionStorage and Redirect to step2 */
  $('#form-profile-info').submit(function (e) {
    e.preventDefault();
    var password1 = document.getElementById('form-profile-info')[2].value; // Password
    var password2 = document.getElementById('form-profile-info')[3].value; // Retype Password
    if (password1 == password2) {
      sessionStorage.setItem('name', document.getElementById('form-profile-info')[0].value); // Name
      sessionStorage.setItem('lastname', document.getElementById('form-profile-info')[1].value); // Lastname
      sessionStorage.setItem('password', document.getElementById('form-profile-info')[2].value); // Password
      sessionStorage.setItem('place', document.getElementById('form-profile-info')[4].value); // Place
      window.location.href = $('#form-profile-info').attr('data-url'); // Redirecting to step1
    }else {
      document.getElementById('response').innerHTML = `<p>Las contraseñas no coinciden</p>`;
    }
  });

})();

/* Landing functions */
function notMember() {
  closeModal('modal-login');
  getModal('modal-signup');
}

/* === Modal actions
* Display de modal by id */
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
