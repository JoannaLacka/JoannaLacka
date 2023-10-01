// function wyswietltekst() {
//     console.log("As")
// }
// setTimeout(wyswietltekst, 2000);

const h2Element = document.querySelector("#band h2");
const colors = ["blue", "pink", "yellow", "red", "green"];

function changeColor () {
    const randomValue = Math.round(Math.random() * ((colors.length - 1) -0) + 0);
    h2Element.style.color = colors[randomValue];
}

h2Element.addEventListener("click", function(){
    setTimeout(changeColor, 2000);
})
