//Zapisaywanie do localStorage
localStorage.setItem("Title", "Super gra");

// //Odczytywanie z localStorage
// const titleGame = localStorage.getItem("Title");
// console.log(titleGame);

// //Usuwanie elemnetu z localStorage
// localStorage.removeItem("Title");

// //Usuwanie wszsytkich elementów z localStorage
// localStorage.clear();

//Usuwanie danych przez wybór uzytkownika
if(confirm("Czy na pewno chcesz usunąć dane?")){
    localStorage.clear();
    alert("Wyczyszczono dane")
} else {
    alert("Nie udało się wyczyścić danych")
}
