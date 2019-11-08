import io
import unittest.mock

from katas import goosegame
from katas.goosegame import GooseGame


class MyTestCase(unittest.TestCase):

    def test_addplayerReturnscorrctlistwhenplayeradded(self):
        game = GooseGame([]);
        self.assertEqual(["Anna"], self.game.addplayer("Anna"))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_doesNotAddDuplicatePlayers(self, mock_stdout):
        game = GooseGame(["Anna"]);
        self.assertEqual(["Anna"], game.addplayer("Anna"))
        assert mock_stdout.getvalue() == 'Anna: already existing player\n'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_doesNotAddMoreThanTwoPlayers(self, mock_stdout):
        game = GooseGame(["Anna", "Mitchell"]);
        self.assertEqual(["Anna", "Mitchell"], game.addplayer("Joe"))
        assert mock_stdout.getvalue() == 'Already at Max number of Players\n'


if __name__ == '__main__':
    unittest.main()
