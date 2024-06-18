class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def exists(self, word):
        current = self.root:
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current

    def words_with_prefix(self, prefix):
        words = []
        current = self.root
        for char in prefix:
            if char not in current:
                return []
            current = current[char]
        self.search_level(current, prefix, words)
        return words

    def search_level(self, cur, cur_prefix, words):
        if self.end_symbol in cur:
            words.append(cur_prefix)
        for key in cur.keys():
            if key != self.end_symbol:
                self.search_level(cur[key], cur_prefix + key, words)
        return words
    
    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches
    
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            if self.end_symbol in current:
                return prefix
            if len(current) == 1:
                letter = list(current.keys())[0]
                prefix += letter
                current = current[letter]
            else:
                return prefix
            
    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch in variations:
                    ch = variations[ch]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches
        