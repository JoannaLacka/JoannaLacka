const form = document.querySelector("form");
const boxBand = document.querySelector("div#band");

//Tworzenie nowego elementu
const divElement = document.createElement("div");
divElement.style.width = "100px";
divElement.style.height = "100px";
divElement.style.backgroundColor = "red";

const p = document.createElement("p");
p.innerText = "Nowy super paragraf!";

console.log(divElement)
console.log(p);

//Wstawanie elementu do HTML (DOM)
form.appendChild(divElement)
boxBand.appendChild(p)