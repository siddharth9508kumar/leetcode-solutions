class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        # Mapping from digits 2-9 to their corresponding letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def backtrack(index: int, current: list[str]):
            # Base case: if the combination length matches the digits length
            if index == len(digits):
                result.append("".join(current))
                return

            # Get letters for the current digit and explore each choice
            digit = digits[index]
            for letter in phone_map[digit]:
                current.append(letter) 
                backtrack(index + 1, current) 
                current.pop() 
        backtrack(0, [])
        return result