let licznik = 0;

function wyswietlTekst () {
    licznik++;
    if(licznik === 8) {
        clearInterval(start)
    } 
        console.log("Test")
}

const start = setInterval(wyswietlTekst,2000);
