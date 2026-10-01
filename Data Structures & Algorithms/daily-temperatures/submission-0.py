class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        seen = []

        for index, temp in enumerate(temperatures):

            while seen and temp > seen[-1][0]:
                old_temp, old_index = seen.pop()
                result[old_index] = index - old_index

            seen.append((temp, index))

        return result