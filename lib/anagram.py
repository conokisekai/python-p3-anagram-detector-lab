# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert word to lowercase for case-insensitive comparison

    def match(self, candidates):
        # Convert the word to a sorted list of characters for easier comparison
        sorted_word = sorted(self.word)

        # Initialize an empty list to store matching anagrams
        matches = []

        # Iterate through the candidates
        for candidate in candidates:
            candidate_lower = candidate.lower()  # Convert candidate word to lowercase
            if candidate_lower != self.word:  # Ensure the candidate is not the same as the word
                sorted_candidate = sorted(candidate_lower)
                if sorted_candidate == sorted_word:  # Compare sorted characters
                    matches.append(candidate)

        return matches
