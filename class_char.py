from text_elements import t_minus, t_blank, t_underscore

class class_char:
    
    def __init__(self, i_char):
        self.char = i_char
        self.guessed = False
    
    
    def check(self, i_char):
        if self.char == i_char:
            self.activate_same_chars()
            
            
    def activate(self, i_char):
        if self.char == i_char.lower() or self.char == i_char.upper():
            self.guessed = True
            return 1
        else:
            return 0
            
            
    def get_char(self):
        if self.char == t_blank or self.char == t_minus:
            return self.char
        elif self.guessed == True:
            return self.char
        else:
            return t_underscore