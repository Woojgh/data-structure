end = '$'


class TrieTree(object):

    def __init__(self):
        # import pdb; pdb.set_trace()
        """This will sety what wwe will be iterating through."""
        self.size = 0
        self.letters = 0
        self.roots = []

    def make_tree(self, *words):
        root = dict()
        for word in words:
            self.size + 1
            current_word = root
            for letter in word:
                self.letters + 1
                current_word = current_word.setdefault(letter, {})
            current_word[end] = end
        return root

    def insert(self, word):
        word_root = word[0]
        if word_root not in self.roots:
            self.roots.append(word_root)

    def search(self, word):
        """."""
        current_word_dict = self
        for letter in word:
            if letter in current_word_dict:
                current_word_dict = current_word_dict[letter]
            else:
                return False
        else:
            if end in current_word_dict:
                return True
            else:
                return False
