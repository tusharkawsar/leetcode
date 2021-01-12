class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smallest = None
        for item in letters:
            if item > target:
                smallest = item
                break # Stops because the first match from the left is our answer
        if smallest == None:
            smallest = letters[0]
        return smallest
        
        
        
