//Typ liczbowy (Number)
const liczba = 24;
const liczba2 = 27.11;

//console.log(liczba - liczba2);

//Typ tekstowy (String)
const pierwszeImie = "Alicja";
const zwierze = 'Pies';

//console.log(pierwszeImie + " ma nowe zwierze, którym jest: " + zwierze)

//Typ logiczny 
const kobieta = false; 
const mezczyzna = true;

//Typ null
const kolor = null;

let imiePsa;


//Typ tablice
const przykladowaTablica = ["Alicja", "Tomasz", "Bartosz", 2, true];

//Typ Obiekt
const osoba = {
    imie: "Tomasz",
    wiek: 29,
    kolorOczu: "zielony",
    plec: "mężczyzna"
}

const zmiennaLiczbowa = "55";

//Zabaw z typami danych 
console.log(osoba.plec.length) // mierzenie długości danego typu danych 
console.log(przykladowaTablica[1].toUpperCase()) // przekształca nam string na duże litery
console.log(przykladowaTablica[1].toLowerCase()); // przekształca nam string na małe litery

const wynikDodawania = liczba + zwierze;

console.log(liczba2.toFixed(5)); // Zaokrągla nam wartość do okreslonych miejsc po przecinku
console.log(typeof(String(liczba)))
console.log(Number(zmiennaLiczbowa))