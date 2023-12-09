from day07p1 import Hand

# Global var
all_hands = []


class Hand2(Hand):
    @staticmethod
    def card_translate(card_string: str):
        card_dictionary = {
            "T": 10,
            "J": 1,
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

        # Edge case: all Jokers (all 1s)
        if unique_card_count == 1 and 1 in hand_set:
            return 6

        # Handle Joker cards (1s)
        if 1 in hand_set:
            joker_count = self.hand_list.count(1)
            hand_set.remove(1)

            hand_count = [self.hand_list.count(i) for i in hand_set]
            unique_card_count = len(hand_set)
            max_similar = max(hand_count) + joker_count

        return self.hand_type_calculation(unique_card_count, max_similar)


def get_input():
    file_location = "day07.txt"
    with (open(file_location, "r") as file):
        current_line = file.readline()
        while current_line != "":
            hand_string, bid = current_line.split()
            current_hand = Hand2(hand_string, int(bid))
            all_hands.append(current_hand)

            current_line = file.readline()


if __name__ == "__main__":
    get_input()
    all_hands.sort()

    result = 0
    for rank, hand in enumerate(all_hands):
        result += (rank + 1) * hand.bid
        # print(hand.hand_list)
    print(result)
