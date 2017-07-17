import re, random


def main():
    path = input('What is the name of the file? >')
    cards = load_cards(path)
    learn(cards)

class Card:
    def __init__(self, word, definition):
        self.word : str = word
        self.definition = definition

    def match_word(self, answer : str) -> bool:
        """Determine if the answer given matches the word based on
        simplify_word. If the word contains parts separated by forward slashes,
        then any combination in any order of the parts need to match."""
        if answer.lower() == self.word.lower():
            return True
        simp_word = simplify_word(self.word)
        simp_ans = simplify_word(answer)
        if simp_word == simp_ans:
            return True

        for s in simp_ans.split('/'):
            if s not in simp_word.split('/'):
                return False

        return True

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not __eq__(other)


def simplify_word(word: str) -> str:
    """Transform the word into one that is more easily matched. It lowercases
    the word, removes any whitespace, and removes any parenthetical parts.
    If the word has nested parentheses, the behavior is undefined.
    """

    word = word.lower().replace(' ', '')
    word = re.sub('\(.*?\)', '', word)
    return word


def load_cards(path) -> list:
    """File formated like so:
    word (1 line only)
    def
    (def cont.)
    ...
    (def end)

    word
    etc.
    """

    with open(path) as f:
        result = []

        term = ''
        defin = ''
        for line in f:
            if line == '\n':
                if term == '' or defin == '':
                    break
                result.append(Card(term[:-1], defin[:-1]))
                # get rid of last \n
                term, defin = '', ''
            elif term == '':
                term = line
            else:
                defin += line
        result.append(Card(term[:-1], defin[:-1]))
    return result


def learn(cards):
    to_learn = list(cards)
    while len(to_learn) > 0:
        current_cards: list[Card] = random.sample(
            to_learn,
            7 if len(to_learn) > 7 else len(to_learn)
        )
        while len(current_cards) > 0:
            for card in current_cards:
                print(card.definition)
                ans: str = input('Term? >')
                if card.match_word(ans):
                    print(f"Yes, it is {card.word}")
                    to_learn.remove(card)
                    current_cards.remove(card)
                else:
                    print(f"No, it is {card.word}")
            print('\n\nGoing over wrong cards:')
        print('Round done!')


if __name__ == '__main__':
    main()