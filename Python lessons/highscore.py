import json
import random

def play_game():
    hscore = load_scores()
    print(f"Highest score: {hscore[1]} by {hscore[0]}")

    player = []
    player.append(input("Your name: "))
    player.append(random.randrange(1000))

    if(player[1] > hscore[1]):
        print(f"Great {player[0]}! You achieved the highest score ever: {player[1]}")
        save_scores(player)
    else:
        print("Good try, but not this time...")

def save_scores(player):
    json_string = json.dumps(player)
    with open ("players.json", "w") as json_file:
        json_file.write(json_string)

def load_scores():
    with open ("players.json", "r") as json_file:
        file_text = json_file.read()
        try:
            data = json.loads(file_text)
            return data
        except:
            return ["...", 0]
        
play_game()
