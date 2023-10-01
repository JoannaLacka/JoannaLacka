const p = document.querySelector("p.w3-justify");
const h2Band = document.querySelector("h2.w3-wide");
const pWeLoveMusic = document.querySelector("p.w3-opacity");


const value = p.innerText;


// console.log(h2Band.innerText)
// console.log(value)
//console.log(pWeLoveMusic.innerText)

//pobieranie wartości src
const img = document.querySelector("img.w3-image");

// console.log(img.getAttribute("src"))
// console.log(img.style.width)

//Pobieranie tekstów z dynamicznych elementów np input

const inputName = document.querySelector(`input[name="Name"]`);
//console.log(inputName.value)
inputName.addEventListener("keyup", () => {
    console.log(inputName.value)
})