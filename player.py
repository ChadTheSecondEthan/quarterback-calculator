class Player:
    def __init__(self, row, get_data):
        self.data = {
            "Passing Yards": int(get_data(row, 'k')),
            "Touchdowns": int(get_data(row, 'l')),
            "Interceptions" : int(get_data(row, 'n')),
        }
        self.name = get_data(row, 'b').split('\\')[0]
        self.rating = 0

    def calc_rating(self, preferences):
        self.rating = 0
        for p in preferences:
            self.rating += self.data[p.get_type()] * float(p.get_weight())

    def __repr__(self):
        return self.name