import unittest
from statistics_service import StatisticsService
from player_reader_stub import PlayerReaderStub

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_search_finds_player(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")
    
    def test_search_returns_none_for_nonexistent_player(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)
    
    def test_team_returns_correct_players(self):
        team = self.stats.team("EDM")
        self.assertEqual(len(team), 3)
        player_names = [player.name for player in team]
        self.assertIn("Semenko", player_names)
        self.assertIn("Kurri", player_names)
        self.assertIn("Gretzky", player_names)
    
    def test_top_scorers_returns_correct_order(self):
        top_scorers = self.stats.top_scorers(3)
        self.assertEqual(len(top_scorers), 3)
        self.assertEqual(top_scorers[0].name, "Gretzky")  # 35+89=124
        self.assertEqual(top_scorers[1].name, "Lemieux")  # 45+54=99
        self.assertEqual(top_scorers[2].name, "Yzerman")  # 42+56=98