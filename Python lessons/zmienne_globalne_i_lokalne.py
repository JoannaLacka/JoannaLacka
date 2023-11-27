score = 0

def manage_points():
    global score
    score += 1
    print(score)

manage_points()

# zmienne lokalne są dostępne tylko wewnątrz funkcji
