import unittest
import flash as f
import os


class TestFlash(unittest.TestCase):

    def test_simplify_word(self):
        self.assertEqual(f.simplify_word('test'), 'test')
        self.assertEqual(f.simplify_word('23fF e'), '23ffe')
        self.assertEqual(f.simplify_word('()'), '')
        self.assertEqual(f.simplify_word('(asdf )  A'), 'a')
        self.assertEqual(f.simplify_word('(a)A (a) 3(rasdf adAA)'), 'a3')

    def test_match_card(self):
        c1 = f.Card('Mac(tm) released (1984) ', '')
        self.assertTrue(c1.match_word('macreleased'))
        self.assertTrue(c1.match_word('mA c ReLeAsEd (kekekek)'))
        self.assertTrue(c1.match_word('m A c R (asdf) elEas()ed'))
        self.assertTrue(c1.match_word('Mac(tm) released (1984) '))
        self.assertFalse(c1.match_word('Mac(tm) release (1984) '))
        self.assertFalse(c1.match_word('Mac(tm) released (1984) a'))
        self.assertFalse(c1.match_word('Mac(tm) released 1984'))

    def test_match_card_with_slashes(self):
        c1 = f.Card('Apple/Banana/Desu(/Kek)', '')
        self.assertTrue(c1.match_word('Apple/Banana/Desu(/Kek)'))
        self.assertTrue(c1.match_word('banana/apple/desu/desu'))
        self.assertTrue(c1.match_word('banana'))
        self.assertTrue(c1.match_word('desu/banana/apple'))
        self.assertTrue(c1.match_word('desu/aPpLe/BaNANA   ()()()'))
        self.assertFalse(c1.match_word('Apple/Banans'))
        self.assertFalse(c1.match_word('ppp/desu'))
        self.assertFalse(c1.match_word(''))

    def test_load_cards(self):
        with open('testme.txt', 'w') as file:
            contents = [
                "Root - Takahira Agreement(1908)",
                "US/Japan agreement: respect other's",
                "Pacific holdings and the Open Door Policy",
                "",
                "Col. George Washington Goethals",
                "Autocratic civil engineer that",
                "supervised construction over Panama Canal",
                "",
                "Open Door policy",
                "US policy that stated that China should be open to trade with all countries"
            ]
            for thing in contents:
                file.write(thing)
                file.write('\n')

            card1 = f.Card(contents[0], contents[1] + '\n' + contents[2])
            card2 = f.Card(contents[4], contents[5] + '\n' + contents[6])
            card3 = f.Card(contents[8], contents[9])
            file.flush()
            os.fsync(file.fileno())

        answer_list = [card1, card2, card3]
        test_list = f.load_cards('testme.txt')
        os.remove('testme.txt')
        self.assertEquals(answer_list, test_list)

    def test_load_cards2(self):
        def test_load_cards(self):
            with open('testme.txt', 'w') as file:
                contents = [
                    "Root - Takahira Agreement(1908)",
                    "US/Japan agreement: respect other's",
                    "Pacific holdings and the Open Door Policy",
                    "",
                    "Col. George Washington Goethals",
                    "Autocratic civil engineer that",
                    "supervised construction over Panama Canal",
                    "",
                    "Open Door policy",
                    "US policy that stated that China should be open to trade with all countries",
                    "",
                ]
                for thing in contents:
                    file.write(thing)
                    file.write('\n')

                card1 = f.Card(contents[0], contents[1] + '\n' + contents[2])
                card2 = f.Card(contents[4], contents[5] + '\n' + contents[6])
                card3 = f.Card(contents[8], contents[9])
                file.flush()
                os.fsync(file.fileno())

            answer_list = [card1, card2, card3]
            test_list = f.load_cards('testme.txt')
            os.remove('testme.txt')
            self.assertEquals(answer_list, test_list)

if __name__ == '__main__':
    unittest.main()
