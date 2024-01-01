import datetime

aktualna_data_godzina = datetime.datetime.now()
print(aktualna_data_godzina)

data_urodzenia = datetime.datetime(2020, 7, 19, 18, 15)
# metoda strftime
print(data_urodzenia.strftime("%d %B %Y Dzień roku: %j"))
