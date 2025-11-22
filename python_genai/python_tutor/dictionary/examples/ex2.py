players = {}
for i in range(5):
    name = input("Enter player name: ")
    score = int(input("Enter player score: "))
    players[name] = score


print("Player Scores: ")
for name, score in players.items():
    print(f"{name}: {score}")
    