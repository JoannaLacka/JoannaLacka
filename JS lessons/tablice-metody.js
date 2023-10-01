const tablica = ["Klaudia", 2, 5.35, true, {name: "Tomasz", age: 24}]
const liczby = [1,6,4,9,2,4];


//Weryfikacja długości tablicy
//console.log(tablica.length)
//console.log(liczby.length)

//Dodawanie elementów do tablicy na sam koniec
tablica.push("Wojtek");
//console.log(tablica);

//Usuwaniem elementu z końca tablicy
tablica.pop();
liczby.pop();
// console.log(tablica)
// console.log(liczby)

//Usuwaniem elementu z początku tablicy
tablica.shift();
//console.log(tablica)

//Znajdowanie elementu w tablicy po jej wartości
const indexElement = liczby.indexOf(6)
const indexElement2 = tablica.indexOf("Klaudia")
//console.log(indexElement);
//console.log(indexElement2)

//Usuwanie elementu z tablicy
liczby.splice(indexElement, 2)
//console.log(liczby)


//Przekształcenie tablicy na strina 
const imiona = ["Rafał", "Krzyś", "Ola", "Ania"]
const string = liczby.join(" ");
//console.log(string);
const stringImiona = imiona.join("-");
//console.log(stringImiona)

//Odwrócenie tablicy
//imiona.reverse();

//Sortowanie tablicy
imiona.sort();
//console.log(imiona)

//Łączenie tablic
const superTablica = liczby.concat(imiona);
console.log(superTablica)