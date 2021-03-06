import ezsheets
from player import Player

class Reader:

    def __init__(self):
        self.spreadsheet = ezsheets.Spreadsheet('1GgstXFHVyzD9WcK2F2mZrXmLohO8Ik3chzr8USl6nMY')[0]

    def get_data(self, row, column):
        return self.spreadsheet.get(column + row)

    def get_row(self, column):
        values = []
        for i in range(self.spreadsheet.rowCount):
            value = self.spreadsheet.get(i + 1, column + 1)
            if len(value) == 0:
                return values
            values.append(self.spreadsheet.get(i + 1, column + 1))
        return values

    def get_players(self):
        players = []
        for i in range(2, 72):
            players.append(Player(str(i), self.get_data))
        return players