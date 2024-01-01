# def say_hello():
    # print("Hello")

# say_hello()

# funkcje return
# funkcje mogą zwracać wartości, które można wykorzystać wewnątz innych funkcji lub przypisać je do zmiennych.
# Wewnątrz innych funkcji należy podać słowo kluczowe return, które określa co powinno być zwrócone.
# Instrukcja return kończy działanie całej funkcji i powoduje wyjście do bloku zewnętrznego.

def zwroc_pole_trojkata(podstawa, wysokosc):
    return podstawa*wysokosc*0.5

print("Pole trójkata wynosi:", zwroc_pole_trojkata(6,4))

