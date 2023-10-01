class Samochod {
    constructor(marka, model, rok, kolor) {
        this.markaSamochodu = marka;
        this.modelSamochodu = model;
        this.rokSamochodu = rok;
        this.kolorSamochodu = kolor;
    }

    przywitajSie() {
        console.log(`Jestem samochodem ${this.markaSamochodu} modelu: ${this.modelSamochodu} z roku: ${this.rokSamochodu} i posiadam kolor: ${this.kolorSamochodu}`)
    }
    pokazRocznik() {
        console.log(`Rocznik samochodu to: ${this.rokSamochodu}`)
    }
}

const fiat = new Samochod("Fiat", "Punto", 2010, "niebieski");
const ford = new Samochod("Ford", "Mondeo", 1999, "zielony");
fiat.przywitajSie();
fiat.pokazRocznik();

ford.przywitajSie();
ford.pokazRocznik();
