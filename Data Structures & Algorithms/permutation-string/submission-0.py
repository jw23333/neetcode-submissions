from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = Counter(s1)
        cur_win = Counter(s2[:len(s1)])

        if cur_win == target:
            return True

        left = 0
        right = len(s1)

        while right < len(s2):
            # add new character on right
            cur_win[s2[right]] += 1

            # remove old character on left
            cur_win[s2[left]] -= 1

            left += 1
            right += 1

            if cur_win == target:
                return True

        return False