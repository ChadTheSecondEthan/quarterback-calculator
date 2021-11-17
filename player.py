class Player:
    def __init__(self, row, get_data):
        self.name = get_data(row, 'b').split('\\')[0]
        self.passing_yards = get_data(row, 'k')
        self.tds = get_data(row, 'l')

    def calc_rating(self):
        pass

    def __str__(self):
        return f'{self.name}: {self.tds} TD\'s, {self.passing_yards} Yds'