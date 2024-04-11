/**
 * Validar formulario de registro
 */
function validateForm() {
  const email = document.getElementById('formEmail').value;
  const password = document.getElementById('formContraseña').value;
  const rol = document.getElementById('formRol').value;
  

  if (!validateEmail(email)) {
    alert('Por favor, ingresa un correo electrónico válido.');
    return false; // Debes retornar false para evitar que se envíe el formulario si hay errores
  }

  if (!validatePassword(password)) {
    alert('La contraseña debe tener al menos 8 caracteres, incluyendo letras mayúsculas, minúsculas, números y caracteres especiales.');
    return false; // Debes retornar false para evitar que se envíe el formulario si hay errores
  }

  // Redirige a inicio.html solo después de que se completen las validaciones
  window.location.href = "inicio.html";
  return false; // Debes retornar false para evitar que se envíe el formulario después de la redirección
}


  function validateEmail(email) {
    // Expresión regular para validar el formato de correo electrónico
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
  
  function validatePassword(password) {
    // Expresión regular para validar la contraseña
    const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;
    return passwordRegex.test(password);
  }

/**
 * Validar formulario de login
 */
function validateLoginForm() {
  const email = document.getElementById('formEmaillogin').value; // Obtener el valor del campo de correo electrónico
  const password = document.getElementById('formContraseñalogin').value; // Obtener el valor del campo de contraseña

  if (!validateEmail(email)) {
    alert('Por favor, ingresa un correo electrónico válido.');
    return false; // Retornar false para evitar el envío del formulario si el correo electrónico no es válido
  }

  if (!validatePassword(password)) {
    alert('La contraseña debe tener al menos 8 caracteres, incluyendo letras mayúsculas, minúsculas, números y caracteres especiales.');
    return false; // Retornar false para evitar el envío del formulario si la contraseña no es válida
  }

  // Si las validaciones son exitosas, permitir el envío del formulario y redirigir a inicio.html
  window.location.href = "inicio.html";
  return false; // Retornar false para evitar el envío del formulario después de la redirección
}

// Las funciones de validación de email y contraseña se pueden mantener sin cambios
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function validatePassword(password) {
  const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;
  return passwordRegex.test(password);
}
