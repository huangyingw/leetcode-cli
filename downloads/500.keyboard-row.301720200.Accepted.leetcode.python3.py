class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = {'Q': 1, 'W': 1, 'E': 1, 'R': 1, 'T': 1, 'Y': 1, 'U': 1, 'I': 1, 'O': 1, 'P': 1,
                'A': 2, 'S': 2, 'D': 2, 'F': 2, 'G': 2, 'H': 2, 'J': 2, 'K': 2, 'L': 2,
                'Z': 3, 'X': 3, 'C': 3, 'V': 3, 'B': 3, 'N': 3, 'M': 3}
        res = []
        for word in words:
            row, inrow = rows[word[0].upper()], True
            for ch in word:
                if rows[ch.upper()] != row:
                    inrow = False
                    break
            if inrow:
                res.append(word)
        return res

