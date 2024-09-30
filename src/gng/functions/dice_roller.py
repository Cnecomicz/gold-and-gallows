import random
import re

class UnexpectedDiceSyntax(Exception):
    pass

def roll_x_d_n_and_keep_highest_k(x, n, k):
    if k > x:
        raise UnexpectedDiceSyntax(
            f"You are trying to keep {k} d{n}s but only rolling {x} d{n}s."
        )
    else:
        result = 0
        results_list = []
        for i in range(x):
            results_list.append(random.randint(1, n))
        for j in range(k):
            highest = max(results_list)
            result += highest
            results_list.remove(highest)
        return result


def roll_x_d_n(x, n):
    return roll_x_d_n_and_keep_highest_k(x, n, x)


def thread_the_needle(low, high):
    return low < roll_x_d_n(1, 20) < high


def roll_below(value):
    return thread_the_needle(0, value)


def roll_above(value):
    return thread_the_needle(value, 21)

def roll_usage(value):
    usage_dice_list = [4, 6, 8, 10, 12, 20]
    if value not in usage_dice_list:
        raise UnexpectedDiceSyntax(
            f"You cannot roll a usage die with {value} sides."
        )
    else:
        usage_die_index = usage_dice_list.index(value)
        if roll(f"d{value}") <= 2:
            if value == 4:
                return None
            else:
                return usage_dice_list[usage_die_index-1]
        else:
            return value


def roll(dice_syntax_string):
    xdn_regex = r"^\d*d\d+$"
    xdnkk_regex = r"^(?!1d)\d+d\d+k\d+$"
    un_regex = r"^u\d+$"
    # ^      : start of string
    # \d     : digits
    # *      : zero or more of the preceding regex
    # d      : the letter "d"
    # +      : one or more of the preceding regex
    # $      : end of string
    # (?!1d) : lookahead is not "1d"
    # k      : the letter "k"
    # u      : the letter "u"
    if re.match(xdn_regex, dice_syntax_string):
        values = re.split("d", dice_syntax_string)
        if values[0] != "":
            x, n = int(values[0]), int(values[1])
        else:
            x, n = 1, int(values[1])
        return roll_x_d_n(x, n)
    elif re.match(xdnkk_regex, dice_syntax_string):
        first_split = re.split("d", dice_syntax_string)
        values = [int(first_split[0])]
        values += re.split("k", first_split[1])
        x, n, k = int(values[0]), int(values[1]), int(values[2])
        return roll_x_d_n_and_keep_highest_k(x, n, k)
    elif re.match(un_regex, dice_syntax_string):
        value = int(re.split("u", dice_syntax_string)[1])
        return f"u{roll_usage(value)}"
    else:
        raise UnexpectedDiceSyntax(dice_syntax_string)



