import unittest
from collections import defaultdict
from typing import List

"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winner defeated player loser in a match.

Return a list answer of size 2 where:

    answer[0] is a list of all players that have not lost any matches.
    answer[1] is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.

Note:

    You should only consider the players that have played at least one match.
    The testcases will be generated such that no two matches will have the same outcome.



Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

"""


def find_winners(matches: List[List[int]]) -> List[List[int]]:
    lose_count = defaultdict(int)

    for match in matches:
        lose_count[match[1]] += 1
        if match[0] not in lose_count:
            lose_count[match[0]] = 0

    one_loss, zero_loss = [], []
    for player, loss in lose_count.items():
        if loss == 0:
            zero_loss.append(player)
        elif loss == 1:
            one_loss.append(player)
    return [sorted(zero_loss), sorted(one_loss)]


# Time Complexity O(NlogN)
# Space Complexity O(N)


class TestFindWinners(unittest.TestCase):
    def test_empty_matches(self):
        self.assertEqual(find_winners([]), [[], []])

    def test_single_match(self):
        self.assertEqual(find_winners([[1, 2]]), [[1], [2]])

    def test_multiple_matches(self):
        matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
        expected_output = [[1, 2, 10], [4, 5, 7, 8]]
        self.assertEqual(find_winners(matches), expected_output)

    def test_no_undefeated_players(self):
        matches = [[1, 2], [2, 3], [3, 1]]
        self.assertEqual(find_winners(matches), [[], [1, 2, 3]])

    def test_all_undefeated_players(self):
        matches = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(find_winners(matches), [[1, 3, 5], [2, 4, 6]])

    def test_non_consecutive_player_numbers(self):
        matches = [[10, 20], [30, 40], [20, 30], [40, 50]]
        self.assertEqual(find_winners(matches), [[10], [20, 30, 40, 50]])


if __name__ == '__main__':
    unittest.main()
