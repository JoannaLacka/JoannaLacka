const h2Element = document.querySelector("div#band h2.w3-wide");
const navbar = document.querySelector("div.w3-bar");
let switchVariable = false;

// h2Element.addEventListener("click", function () {
//     console.log("Działa!")
// })

//Zmiana koloru h2 na czerwony i z powrotem
h2Element.addEventListener("click", function () {
    if(switchVariable === false) {
    this.style.color = "red";
    this.style.fontSize = "56px";
    } else {
    this.style.color = "black";
    this.style.fontSize = "22px";
    }
     //this.style = "text-decoration: uderline";
     switchVariable = !switchVariable;
})

//Zmiana koloru paska przy skrolowaniu 
// window.addEventListener("scroll", () => {
//     console.log(window.scrollY)
// })

window.addEventListener("scroll", () => {
    if(window.scrollY > 350) {
        navbar.style.background = "blue";
    } else {
        navbar.style.background = "black";
    }
})