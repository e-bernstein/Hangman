import os
clear = lambda: os.system(t_clear_shell)

from random import randint
from text_elements import *


def read_text():
    
    file = open( file = t_text_file, mode = t_read_flag, encoding = t_file_encoding)
    all_words = file.read()
    file.close()
    ki_words = all_words.split(t_text_splitter)
    
    return ki_words


def game(i_word, ki_words, already_played):
    
    is_valid = False
    is_ki = False
    valid_chars = t_allowed.split(t_comma)
    clear()
    print_header()
    
    print(t_new_line)
    
    while not is_valid:
        input_word = input(t_white_bg + t_request_input + t_colour_end + t_blank)
        if input_word == t_input_random:
            input_word, already_played, ki_words = ki_game(ki_words, already_played)
            is_ki = True
            break
        else:
            if not (input_word == t_empty_string or input_word == t_blank):
                is_valid = True
                for e in input_word:    
                    try:
                        valid_chars.index(e)
                        pass
                    except ValueError:
                        clear()
                        is_valid = False
                        print_header()
                        print(t_new_line)
                        
                        print(t_response_invalid_input)
                        print(t_bell_sound + t_new_line)
                        break
                if is_valid and ( ( input_word not in ki_words ) and ( input_word not in already_played ) ):
                    want_save = input(t_output_save)
                    if want_save == t_input_yes_lower or want_save == t_input_yes_upper:
                        file = open( file = t_text_file, mode = t_append_flag, encoding = t_file_encoding)
                        file.write(t_text_splitter + input_word)
                        file.close()
            else:
                clear()
                print_header()
                print(t_new_line)
                print(t_response_invalid_input)
                print(t_new_line)
            
    i_word.new_word(input_word)
    attempts_left = 10
    
    text_out(t_start, i_word.get_word()[0], attempts_left)
    is_Finished = False
    
    while attempts_left > 0 and not is_Finished:
        attempts_left, is_Finished = game_round( i_word )
        
    if is_Finished:
        text_out(t_win, i_word.get_word()[0], attempts_left)
    else:
        if not is_ki:
            for e in i_word.char_list:
                e.guessed = True
        text_out(t_loss, i_word.get_word()[0], attempts_left)
    
    still_play = input(t_white_bg + t_output_enter + t_colour_end + t_blank)
    print(45 * t_minus)
    
    if still_play != t_stop:
        game(i_word, ki_words, already_played)


def ki_game(ki_words, already_played):
    if len(ki_words) > 0:
        index = randint(0, len(ki_words)-1)
        ki_word = ki_words.pop(index)
        already_played.append(ki_word)
    else:
        ki_word = t_output_enough
        
    return ki_word, already_played, ki_words


def game_round( i_word ):
    
    input_char = input(t_white_bg + t_request_char + t_colour_end + t_blank)
    
    if input_char == t_empty_string:
        input_char = t_blank
    is_Found, attempts_left = i_word.guess_char(input_char)
    if is_Found:
        text_out(t_correct, i_word.get_word()[0], attempts_left)
    else:
        text_out(t_wrong, i_word.get_word()[0], attempts_left)
        
    return attempts_left, i_word.get_word()[1]


def print_header():
    print(73 * t_minus)
    print(t_new_line)
    print(30 * t_blank + t_game_name + t_blank + t_version + 30 * t_blank)
    print(t_new_line)
    print(73 * t_minus)


def text_out( i_text, i_word, i_rem_attempts):
    clear()
    print_header()
    
    # 1st line
    blanks_count = 26 + len(i_word)
    print( blanks_count * t_underscore + 15 * t_underscore )
    
    # 2nd line
    blanks_count = 24 + len(i_word)
    print(t_straight + blanks_count * t_blank + t_straight + t_empty_right)
    
    # 3rd line
    side_blanks_count = ( ( 24 + len(i_word) ) - len(i_text) ) // 2
    
    if i_rem_attempts < 8:
        right_side = 4 * t_blank + 6 * t_underscore + 4 * t_blank + t_straight
    else:
        right_side = t_empty_right
        
    if i_text == t_correct or i_text == t_win:
        colour_code = t_green_bg_white_fg
    elif i_text == t_wrong or i_text == t_loss:
        colour_code = t_red_bg_white_fg
    else:
        colour_code = t_orange_bg
    
    print(t_straight + side_blanks_count * t_blank + colour_code + i_text + t_colour_end + side_blanks_count * t_blank + t_straight + right_side)
    
    # 4th line
    blanks_count = 24 + len(i_word)
    
    if i_rem_attempts < 7:
        right_side = 3 * ( 4 * t_blank + t_straight ) 
    elif i_rem_attempts < 9:
        right_side = 4 * t_blank + t_straight + 9 * t_blank + t_straight
    else:
        right_side = t_empty_right

    print(t_straight + blanks_count * t_blank + t_straight + right_side)
    
    # 5th line
    colour_code = t_orange_fg
    side_blanks_count = 12
    
    if i_rem_attempts == 0:
        right_side = 4 * t_blank + t_straight + 4 * t_blank + t_red_fg + t_letter_o + t_colour_end + 4 * t_blank + t_straight
    elif i_rem_attempts < 2:
        right_side = 4 * t_blank + t_straight + 4 * t_blank + t_blue_fg + t_letter_o + t_colour_end + 4 * t_blank + t_straight
    elif i_rem_attempts < 6:
        right_side = 4 * t_blank + t_straight + 4 * t_blank + t_letter_o + 4 * t_blank + t_straight  
    elif i_rem_attempts < 9:
        right_side = 4 * t_blank + t_straight + 9 * t_blank + t_straight
    else:
        right_side = t_empty_right
        
    print(t_straight + side_blanks_count * t_blank + colour_code + i_word + t_colour_end + side_blanks_count * t_blank + t_straight + right_side)
    
    # 6th line
    blanks_count = 24 + len(i_word)
    
    if i_rem_attempts == 0:
        right_side = 4 * t_blank + t_straight + 3 * t_blank + t_red_fg +t_hangman_breast_1 + t_colour_end + 3 * t_blank + t_straight
    elif i_rem_attempts < 3:
        right_side = 4 * t_blank + t_straight + 3 * t_blank + t_hangman_breast_2 + 3 * t_blank + t_straight
    elif i_rem_attempts < 4:
        right_side = 4 * t_blank + t_straight + 3 * t_blank + t_hangman_breast_3 + 4 * t_blank + t_straight
    elif i_rem_attempts < 5:
        right_side = 3 * ( 4 * t_blank + t_straight )
    elif i_rem_attempts < 9:
        right_side = 4 * t_blank + t_straight + 9 * t_blank + t_straight
    else:
        right_side = t_empty_right
    
    print(t_straight + blanks_count * t_blank + t_straight + right_side)
    
    # 7th line
    side_blanks_count_1 = ( ( 24 + len(i_word) ) - 12 ) // 2
    side_blanks_count_2 = side_blanks_count_1 + 1
    
    if i_rem_attempts == 0:
        right_side = 3 * t_blank + t_basement + 3 * t_blank + t_red_fg + t_quotation + t_colour_end + 4 * t_blank + t_straight
    elif i_rem_attempts < 2:
        right_side = 3 * t_blank + t_basement + 3 * t_blank + t_roof + 4 * t_blank + t_straight
    elif i_rem_attempts < 10:
        right_side = 3 * t_blank + t_basement + 8 * t_blank + t_straight
    else:
        right_side = t_empty_right
        side_blanks_count_2 -= 1

    print(t_straight + side_blanks_count_1 * t_blank + t_output_tries + str(i_rem_attempts) + side_blanks_count_2 * t_blank + t_straight + right_side)
    
    # 8th line
    blanks_count = 24 + len(i_word)
    print(t_straight + blanks_count * t_blank + t_straight + t_empty_right)
    
    # 9th line
    print(t_straight + blanks_count * t_underscore + t_straight + 14 * t_underscore + t_straight)
    
    print(t_new_line)