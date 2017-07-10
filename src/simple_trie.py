test_list = ['mon', 'ta', 'read']


def compare(input_word, index=0, word_set=test_list):
    #if check_if_word_in_set(input_word, word_set):
        #return test_list
    while True:
        temp_list = list(filter(lambda x: input_word[0:index] == x[0:index], word_set))
        if temp_list:
            new_list = []
            for letter in input_word:
                new_list.append(letter)
                if new_list == temp_list:
                    [new_list.append(letter) for letter in input_word if letter not in temp_list]
            index += 1
            import pdb; pdb.set_trace()
            if index > len(input_word):
                word_set.remove(temp_list[0])
                word_set.append(input_word)
                word_set.append(temp_list[0][index-1:])
                return word_set
        else:
            word_set.append(input_word)
            return word_set

_end = '$'


def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
        import pdb; pdb.set_trace()
    return root

# test_list = ['mon', 'ta', 'read']


# class Node(object):
#     def __init__(self, entry, root=None, child=None, parent=None):
#         """Node for tree."""
#         self.val = entry
#         self.root = root
#         self.child = child
#         self.parent = parent


# class TrieTree(object):

#     def __init__(self, Node=None, iterable=None):
#         self.node = Node
#         self.itertable = iterable

#     def compare(self, input_word, index=0, word_set=test_list):
#         if self.check_if_word_in_set(input_word, word_set):
#             return test_list
#         while True:
#             temp_list = list(filter(lambda x: input_word[0:index] == x[0:index], word_set))
#             if temp_list:
#                 index += 1
#                 if index > len(input_word):
#                     word_set.remove(temp_list[0])
#                     word_set.append(input_word)
#                     word_set.append(temp_list[0][index-1:])
#                     return word_set
#             else:
#                 word_set.append(input_word)
#                 return word_set

#     def check_if_word_in_set(self, input_word, word_set=test_list):
#         if input_word in self.concat_words_in_set(word_set):
#             return True
#         return False

#     def concat_words_in_set(self, word_set):
#         """Will create a list of concatenated words based on the current set of words."""
#         concat_words = []
#         for word in word_set:
#             if word.parent:
#                 temp_word = word.parent + word
#                 while word.parent:
#                     temp_word = word.parent + temp_word
#                     concat_words.append(temp_word)
#             else:
#                 concat_words.append(word)
#         return concat_words
