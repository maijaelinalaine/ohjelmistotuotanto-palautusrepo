class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self._is_tie():
            return self._get_tie_score()
        elif self._is_endgame():
            return self._get_endgame_score()
        else:
            return self._get_regular_score()

    def _is_tie(self):
        return self.player1_score == self.player2_score

    def _is_endgame(self):
        return self.player1_score >= 4 or self.player2_score >= 4

    def _get_tie_score(self):
        score_names = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All"
        }
        return score_names.get(self.player1_score, "Deuce")

    def _get_endgame_score(self):
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _get_regular_score(self):
        score_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

        player1_score = score_names[self.player1_score]
        player2_score = score_names[self.player2_score]

        return f"{player1_score}-{player2_score}"
