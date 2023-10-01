const stanSwiatla = true; //True / False

switch(stanSwiatla) {
    case true:
        console.log("Światło zostało włączone")
        break;
    case false: 
        console.log("Światło zostało wyłączone")
        break;
    default:
        console.log("Obecnie jest awaria!")
}

const imie = "Alicja";

switch(imie) {
    case 'Alicja':
        console.log("Imię to " + imie)
        break;
    default:
        console.log("Takie imienia nie mamy w bazie")
}