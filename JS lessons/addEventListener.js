const h2Band = document.querySelector("div#band h2");
const p = document.querySelector("p.w3-justify");
const buyTicketBtn = document.querySelector("#buy-ticket");
const formContact = document.querySelector("form");
const link = document.querySelector(`div.w3-top div.w3-bar a[href="#contact"]`);
const inputName = document.querySelector(`input[name="Name"]`);


//Zdarzenie kliknięcie

function showText() {
    console.log("Kliknełam w nagłówek")
}

h2Band.addEventListener("click", showText)

//const h2Band = document.querySelector("div#band h2");
// h2Band.addEventListener("click", () =>{
//     console.log("Kliknełam w nagłówek")
// })

//Słówko this zamiennie z const p 
p.addEventListener("click", function () {
    console.log(this)
})

//p.addEventListener("click", () => {
  //  console.log(this)
//})  // NIE DZIAŁA przy f.strzałkowej

//Event

// p.addEventListener("click", e => {
//   console.log(e.clientX)
// })

// p.addEventListener("click", e => {
//   if(e.clientX > 500) {
//     console.log("Wartość większa niż 500 i wynosi: " + e.clientX)
//   } else {
//     console.log("Wartość mniejsza niż 500 i wynosi: " + e.clientX)
//   }
// })

//Mouseover i mouseout

buyTicketBtn.addEventListener("mouseover", () => {
console.log("Zadziało się")
})

buyTicketBtn.addEventListener("mouseout", () => {
  console.log("Zadziało się2")
  })

  //Prevent Default

formContact.addEventListener("submit", e => {
  e.preventDefault();
})

link.addEventListener("click", event => {
  event.preventDefault();
})

//Keydown, keyup

inputName.addEventListener("keydown", () => {
  console.log("Uruchomiono zdarzenie KEYDOWN")
})

inputName.addEventListener("keyup", () => {
  console.log("Uruchomiono zdarzenie KEYUP")
})

inputName.addEventListener("keydown", e => {
  console.log(e.key)
})

//Scroll
window.addEventListener("scroll", () => {
   console.log("SCROLL")
})

window.addEventListener("scroll", e => {
  console.log(e)
})

window.addEventListener("scroll", e => {
  console.log(window.scrollY)
})

// Wykonanie zdarzenia po wczytanie się w pełni DOM

window.addEventListener("DOMContentLoaded", () => {
  console.log("DOM wczytał się poprawnie")
})
