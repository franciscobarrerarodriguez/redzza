// https://developer.mozilla.org/en-US/docs/Web/API
(function () {
  /* form-login actions */
  $('#form-login').submit(function (e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
      url: form.attr('data-url'),
      data: form.serialize(),
      dataType: 'json',
      success: function (json) {
        alert(json);/*Falta terminar*/
      }
    });
  });

  /* form-signup actions */
  $('#form-signup').submit(function (e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
      url: form.attr('data-url'),
      data: form.serialize(),
      dataType: 'json',
      success: function (json) {
        alert(json);/*Falta terminar*/
      }
    });
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
