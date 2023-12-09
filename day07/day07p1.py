# Global var
all_hands = []


class Hand:

    def __init__(self, hand_string: str, bid: int):
        self.bid = bid
        self.hand_list = list(hand_string)
        self.hand_list = [self.card_translate(i) for i in self.hand_list]
        self.hand_strength = self.hand_type()

    def __lt__(self, other):
        if isinstance(other, Hand):
            if self.hand_strength < other.hand_strength:
                return True
            elif self.hand_strength == other.hand_strength:
                for i in range(5):
                    if self.hand_list[i] < other.hand_list[i]:
                        return True
                    elif self.hand_list[i] == other.hand_list[i]:
                        continue
                    else:
                        return False
            else:
                return False
        else:
            return False

    @staticmethod
    def card_translate(card_string: str):
        card_dictionary = {
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }

        if card_string.isdigit():
            return int(card_string)
        else:
            return card_dictionary[card_string]

    def hand_type(self):
        hand_set = set(self.hand_list)
        hand_count = [self.hand_list.count(i) for i in hand_set]
        unique_card_count = len(hand_set)
        max_similar = max(hand_count)

        return self.hand_type_calculation(unique_card_count, max_similar)

    @staticmethod
    def hand_type_calculation(unique_card_count, max_similar):
        # 6 = Five of a kind
        if unique_card_count == 1:
            return 6
        # 5 = Four of a kind
        # 4 = Full house
        elif unique_card_count == 2:
            if max_similar == 4:
                return 5
            else:
                return 4
        # 3 = Three of a kind
        # 2 = Two pair
        elif unique_card_count == 3:
            if max_similar == 3:
                return 3
            else:
                return 2
        # 1 = One pair
        elif unique_card_count == 4:
            return 1
        # 0 = High card
        else:
            return 0


def get_input():
    file_location = "day07.txt"
    with (open(file_location, "r") as file):
        current_line = file.readline()
        while current_line != "":
            hand_string, bid = current_line.split()
            current_hand = Hand(hand_string, int(bid))
            all_hands.append(current_hand)

            current_line = file.readline()


if __name__ == "__main__":
    get_input()
    all_hands.sort()

    result = 0
    for rank, hand in enumerate(all_hands):
        result += (rank + 1) * hand.bid
    print(result)
