(function() {
  "use strict";

  /**
   * Función  selección fácil
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)] // Selecciona todos los elementos que coincidan con el selector
    } else {
      return document.querySelector(el) // Selecciona el primer elemento que coincida con el selector
    }
  }

  /**
   * Función de eventos de desplazamiento fácil
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener) // Añade un event listener de scroll al elemento especificado
  }



  /**
   * Botón de "volver arriba"
   */
  let backtotop = select('.back-to-top') // Selecciona el elemento con la clase .back-to-top
  if (backtotop) { // Verifica si el elemento existe
    const toggleBacktotop = () => {
      if (window.scrollY > 100) { // Verifica si la posición de desplazamiento es mayor que 100 píxeles
        backtotop.classList.add('active') // Añade la clase 'active' al elemento
      } else {
        backtotop.classList.remove('active') // Elimina la clase 'active' del elemento
      }
    }
    window.addEventListener('load', toggleBacktotop) // Añade un event listener al evento 'load' que activa/desactiva el botón
    onscroll(document, toggleBacktotop) // Añade un event listener de scroll al documento que activa/desactiva el botón
  }






  
  
  /**
   * Animación al desplazarse
   */
  window.addEventListener('load', () => { // Añade un event listener al evento 'load'
    AOS.init({ // Inicializa la librería de animaciones AOS
      duration: 1500, // Duración de la animación (en milisegundos)
      easing: "ease-in-out", // Tipo de easing
      once: true, // Si la animación se ejecuta solo una vez
      mirror: false // Si se debe invertir la dirección de la animación en función del scroll
    });
  });

})()

console.clear();

const loginBtn = document.getElementById('login');
const signupBtn = document.getElementById('signup');

loginBtn.addEventListener('click', (e) => {
  let parent = e.target.parentNode.parentNode;
  Array.from(e.target.parentNode.parentNode.classList).find((element) => {
    if(element !== "slide-up") {
      parent.classList.add('slide-up')
    }else{
      signupBtn.parentNode.classList.add('slide-up')
      parent.classList.remove('slide-up')
    }
  });
});

signupBtn.addEventListener('click', (e) => {
  let parent = e.target.parentNode;
  Array.from(e.target.parentNode.classList).find((element) => {
    if(element !== "slide-up") {
      parent.classList.add('slide-up')
    }else{
      loginBtn.parentNode.parentNode.classList.add('slide-up')
      parent.classList.remove('slide-up')
    }
  });
});