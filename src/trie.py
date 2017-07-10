end = '$'


class TrieTree(object):

    def __init__(self):
        # import pdb; pdb.set_trace()
        """This will sety what wwe will be iterating through."""
        self.size = 0
        self.root_set = []
        self.letter_sets = []

    def make_tree(self, *words):
        # new_dict = dict()
        for word in words:
            current_letter_set = []
            self.size = self.size + 1
            # word_dict = new_dict
            if self.letter_sets == []:
                self.letter_sets.append(word)
                self.root_set = self.letter_sets[0]
                return self.letter_sets
                break
            else:
                import pdb; pdb.set_trace()
                letter_check = ''
                for curr_set in self.letter_sets:
                    for letter in word:
                        letter_check = letter_check + letter
                        if letter_check in curr_set:
                            continue
                        elif :
                            current_letter_set = letter_check[:-1]
                            new_letter_set = []
                            old_letter_set = []
                            [new_letter_set.append(letter) for letter in word if letter not in current_letter_set]
                            new_group_set = ''.join(new_letter_set)
                            [old_letter_set.append(old) for old in self.letter_sets[0] if old not in current_letter_set]
                            old_group_set = ''.join(old_letter_set)
                            if current_letter_set in self.letter_sets and current_letter_set != '':
                                if current_letter_set == curr_set:
                                    tmp = []
                                    [tmp.append(letter) for letter in word if letter not in current_letter_set]
                                    tmp = ''.join(tmp)
                                    self.letter_sets.append(tmp)
                            else:
                                self.letter_sets.append(current_letter_set)
                            if new_group_set or old_group_set != '':
                                if self.root_set in self.letter_sets:
                                    self.letter_sets.remove(self.root_set)
                                    self.root_set = self.letter_sets
                                if old_group_set not in self.letter_sets:
                                    self.letter_sets.append(old_group_set)
                                if new_group_set not in self.letter_sets:
                                    self.letter_sets.append(new_group_set)
                            if '' in self.letter_sets:
                                self.letter_sets.remove('')
                            return self.letter_sets

    # def insert(self, word):
    #     for word in words:
    #         current_letter_set = []
    #         self.size = self.size + 1
    #         # word_dict = new_dict
    #         if self.letter_sets == []:
    #             self.letter_sets = [word]
    #             self.root_set = self.letter_sets
    #             return self.letter_sets
    #             break
    #         else:
    #             letter_check = ''
    #             for letter in word:
    #                 self.letters = self.letters + 1
    #                 letter_check = letter_check + letter
    #                 for lset in self.letter_sets:
    #                     if letter_check in lset:
    #                         good_group = letter_check
    #                         continue
    #                     else:
    #                         import pdb; pdb.set_trace()
    #                         current_letter_set = good_group
    #                         new_letter_set = []
    #                         old_letter_set = []
    #                         [new_letter_set.append(letter) for letter in word if letter not in current_letter_set]
    #                         new_group_set = ''.join(new_letter_set)
    #                         [old_letter_set.append(old) for old in self.letter_sets[0] if old not in good_group]
    #                         old_group_set = ''.join(old_letter_set)
    #                         self.letter_sets = [current_letter_set]
    #                         self.letter_sets.append(old_group_set)
    #                         self.letter_sets.append(new_group_set)
    #                         return self.letter_sets

    # def search(self, word):
    #     """."""
    #     current_word_dict = self
    #     for letter in word:
    #         if letter in current_word_dict:
    #             current_word_dict = current_word_dict[letter]
    #         else:
    #             return False
    #     else:
    #         if end in current_word_dict:
    #             return True
    #         else:
    #             return False
