class Solution:
    def encode(self, strs: list[str]) -> str:
        parts = []

        for word in strs:
            parts.append(str(len(word)) + "#" + word)

        return "".join(parts)

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0

        while i < len(s):
            # Find the separator after the length
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # The word begins just after "#"
            start = j + 1
            end = start + length

            result.append(s[start:end])

            # Move to the next length prefix
            i = end

        return result
