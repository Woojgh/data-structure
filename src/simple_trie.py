
_end = '$'


class TrieTree(Object):
    def __init__(self, words):

    def make_trie(*words):
        root = dict()
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = _end
            # import pdb; pdb.set_trace()
        return root
