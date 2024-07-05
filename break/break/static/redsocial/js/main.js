(function() {
  "use strict";

  /**
   * Función  animacion index
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)] 
    } else {
      return document.querySelector(el) 
    }
  }

  /**
   * Función de desplazamiento fácil
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener) 
  }



  /**
   * Botón de "volver arriba"
   */
  let backtotop = select('.back-to-top') 
  if (backtotop) { 
    const toggleBacktotop = () => {
      if (window.scrollY > 100) { 
        backtotop.classList.add('active') 
      } else {
        backtotop.classList.remove('active') 
      }
    }
    window.addEventListener('load', toggleBacktotop) 
    onscroll(document, toggleBacktotop) 
  }



  
  /*** Animación al desplazarse  ***/
  window.addEventListener('load', () => { 
    AOS.init({ 
      duration: 1500, 
      easing: "ease-in-out", 
      once: true, 
      mirror: false 
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