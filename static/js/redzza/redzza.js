// https://developer.mozilla.org/en-US/docs/Web/API

// var buttonNotMember = document.getElementById('button-not-member');

/* Body variables */
var all = document.getElementById('all');

(function () {
  // buttonNotMember.addEventListener('click', function () { // Listener button Not Member
  //   closeModal('modal-login');
  //   getModal('modal-signup');
  // });

  /* form-login actions */
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
    //Estado del checkbox
    var url = $('#signup-input').attr('data-url') + "?email=" + $('#signup-input').val();
    $.get(url, function (data) {
      if (data.is_taken) {
        document.getElementById('signup-response').innerHTML = `<p>Este correo ya tiene una cuenta asociada, prueba iniciando sesion.</p>`;
      }else{
        localStorage.setItem('email', $('#signup-input').val()); // Save email in localStorage
        window.location.href = $('#form-signup').attr('data-url'); // Redirecting to step1
      }
    });
  });

  $('#form-profile-info').submit(function (e) {
    e.preventDefault();
    localStorage.setItem('name', document.getElementById('form-profile-info')[0].value); // Name
    localStorage.setItem('lastname', document.getElementById('form-profile-info')[1].value); // Lastname
    localStorage.setItem('place', document.getElementById('form-profile-info')[2].value); // Place
    window.location.href = $('#form-profile-info').attr('data-url'); // Redirecting to step1
  });
})();

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
