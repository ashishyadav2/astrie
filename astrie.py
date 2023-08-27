from typing import List

class TrieNode:
    def __init__(self) -> None:
        # Dictionary to store child nodes for each character
        self.links = {}
        # Count of words that are exactly equal to the path from the root to this node
        self.equalto = 0
        # Count of words that start with the path from the root to this node
        self.startswith = 0

class AsTrie:
    def __init__(self) -> None:
        # Initialize the root node of the Trie and unique word count
        self.root = TrieNode()
        self.uniquecount = 0

    def add(self, word: str) -> None:
        # Add a word to the Trie
        node = self.root
        for char in word:
            if char not in node.links:
                # Create a new TrieNode for the character
                node.links[char] = TrieNode()
            node = node.links[char]
            # Increment the starts_with count for nodes along the path
            node.startswith += 1
        # If this is a new word, increase unique word count
        if node.equalto == 0:
            self.uniquecount += 1
        # Increment the equalto count for the last node
        node.equalto += 1

    def add_many(self, word_list: List[str]) -> None:
        # Add multiple words to the Trie
        for word in word_list:
            self.add(word)

    def remove(self, word: str) -> None:
        # Remove a word from the Trie
        node = self.root
        for char in word:
            if char not in node.links:
                return  # Word not found
            node = node.links[char]
            node.startswith -= 1
        if node.equalto > 0:
            node.equalto -= 1

    def remove_many(self, word_list: List[str]) -> None:
        # Remove multiple words from the Trie
        for word in word_list:
            self.remove(word)

    def clear(self) -> None:
        # Clear the Trie by resetting root and unique count
        self.root = TrieNode()
        self.uniquecount = 0

    def has(self, word: str) -> bool:
        # Check if a word exists in the Trie
        node = self.root
        for char in word:
            if char not in node.links:
                return False
            node = node.links[char]
        return node.equalto > 0

    def starts_with(self, prefix: str) -> bool:
        # Check if any word in the Trie starts with a given prefix
        node = self.root
        for char in prefix:
            if char not in node.links:
                return False
            node = node.links[char]
        return True

    def starts_with_count(self, prefix: str) -> int:
        # Count the number of words that start with a given prefix
        node = self.root
        for char in prefix:
            if char not in node.links:
                return 0
            node = node.links[char]
        return node.startswith

    def count_equals(self, word: str) -> int:
        # Count the number of times a specific word appears in the Trie
        node = self.root
        for char in word:
            if char not in node.links:
                return 0
            node = node.links[char]
        return node.equalto

    def unique_count(self) -> int:
        # Get the count of unique words in the Trie
        return self.uniquecount

    def all_words(self):
        # Get a generator that yields all words in the Trie
        return self._get_words_helper(self.root, "")

    def _get_words_helper(self, node, current_word):
        # Recursive helper function to yield words stored in the Trie
        if node.equalto > 0:
            yield current_word

        for char, child in node.links.items():
            # Recurse with child node and updated current word
            yield from self._get_words_helper(child, current_word + char)

    def words_starts_with(self, prefix: str):
        # Get a generator that yields words starting with a given prefix
        node = self.root
        for char in prefix:
            if char not in node.links:
                return
            node = node.links[char]
        yield from self._get_words_helper(node, prefix)