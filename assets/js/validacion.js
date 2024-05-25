/**
 * Validar formulario de registro
 */
function validateForm() {
  const email = document.getElementById('formEmail').value;
  const password = document.getElementById('formContraseña').value;
  const rol = document.getElementById('formRol').value;
  

  if (!validateEmail(email)) {
    alert('Por favor, ingresa un correo electrónico válido.');
    return false; 
  }

  if (!validatePassword(password)) {
    alert('La contraseña debe tener al menos 8 caracteres, incluyendo letras mayúsculas, minúsculas, números y caracteres especiales.');
    return false; 
  }

  // Redirige a inicio.html solo después de que se completen las validaciones
  window.location.href = "inicio.html";
  return false; 
}


  function validateEmail(email) {
   
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
  
  function validatePassword(password) {
    
    const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;
    return passwordRegex.test(password);
  }

/**
 * Validar formulario de login
 */
function validateLoginForm() {
  const email = document.getElementById('formEmaillogin').value; 
  const password = document.getElementById('formContraseñalogin').value; 

  if (!validateEmail(email)) {
    alert('Por favor, ingresa un correo electrónico válido.');
    return false; 
  }

  if (!validatePassword(password)) {
    alert('La contraseña debe tener al menos 8 caracteres, incluyendo letras mayúsculas, minúsculas, números y caracteres especiales.');
    return false; 
  }

  // Si las validaciones son exitosas, permitir el envío del formulario y redirigir a inicio.html
  window.location.href = "inicio.html";
  return false; 
}


function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function validatePassword(password) {
  const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;
  return passwordRegex.test(password);
}
