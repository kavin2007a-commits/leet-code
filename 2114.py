from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # Count the number of spaces + 1 for each sentence and return the maximum
        return max(s.count(' ') + 1 for s in sentences)