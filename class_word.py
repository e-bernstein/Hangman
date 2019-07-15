from class_char import class_char
from text_elements import t_cheat, t_empty_string, t_blank, t_underscore

class class_word:
    def __init__(self):
        self._word = t_empty_string
        self.char_list = []
        self.attempts_left = 10
    
    
    def new_word(self, i_word):
        l_list = []
        self.attempts_left = 10
        for e in i_word:
            v1 = class_char(i_char=e)
            l_list.append(v1)
        self.char_list = l_list
    
    
    def guess_char(self, i_char):
        is_word = True
        if i_char != t_cheat:
            if len(i_char) > len(self.char_list):
                self.attempts_left -= 1
                return False, self.attempts_left
            elif len(i_char) == len(self.char_list):
                for e in range(0, len(i_char)):
                    if (self.char_list[e].char != i_char[e].upper() and self.char_list[e].char != i_char[e].lower()):
                        is_word = False
            else:
                is_word = False
        if is_word:
            for i in self.char_list:
                self.activate_same_chars(i.char)
            return True, self.attempts_left
        is_Found = self.activate_same_chars(i_char)
        if not is_Found:
            self.attempts_left -= 1
        return is_Found, self.attempts_left
    
    
    def get_word(self):
        self._word, is_Finished = self.build_Word()
        return self._word, is_Finished
    
    
    def build_Word(self):
        l_word = t_empty_string
        is_Finished = True
        for e in self.char_list:
            l_word = l_word + e.get_char() + t_blank
            if e.get_char() == t_underscore:
                is_Finished = False
        return l_word, is_Finished
    
    
    def activate_same_chars(self, i_char):
        found_counter = 0
        for e in self.char_list:
            found_counter += e.activate(i_char)
        return found_counter > 0.