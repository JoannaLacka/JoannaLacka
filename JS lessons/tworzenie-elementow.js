//Tworzenie nowego elementu
const form = document.querySelector("form");
const divElement = document.createElement("div");
const boxBand = document.querySelector("div#band");
const p = document.createElement("p");
divElement.style.width = "100px";
divElement.style.height = "100px";
divElement.style.background = "red";

p.innerText = "nowy super paragraf";
form.appendChild(divElement)
boxBand.appendChild(p)



console.log(divElement)
console.log(p)
