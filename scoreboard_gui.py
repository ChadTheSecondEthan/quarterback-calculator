import matplotlib.pyplot as plt

colors = ['black', 'red', 'green', 'blue', 'cyan', 'purple', 'yellow', 'orange']

class ScoreboardGUI: 
    def __init__(self, players, preferences, amount):
        for player in players:
            player.calc_rating(preferences)
        players.sort(key=lambda player: player.rating)
        players = players[-amount:]
        players.reverse()

        letters = [chr(ord('A') + i) for i in range(amount)]
        names = []
        ratings = []

        for player in players:
            names.append(player.name.split(' ')[-1])
            ratings.append(player.rating)

        bars = plt.bar(letters, ratings, color=colors)
        plt.legend(bars, names)
        plt.title("Player Ratings")
        plt.show()