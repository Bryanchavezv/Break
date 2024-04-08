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
  
   
    return true; // Retorna true para permitir el envío del formulario si todas las validaciones son exitosas
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

