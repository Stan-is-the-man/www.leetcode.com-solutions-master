# print(ord('a'))
# print(chr(101))

def replace_digits_by_certain_formula(s: str):
    # For example, shift('a', 5) = 'f'.
    final_str = ''
    for x in range(len(s)):
        curent_sumbol = s[x]
        if curent_sumbol.isalpha():
            final_str += s[x]
        if curent_sumbol.isdigit():
            str_to_digit = int(curent_sumbol)
            previous_char = ord(s[x-1])
            char = chr(previous_char + str_to_digit)
            final_str += char
    return final_str


print(replace_digits_by_certain_formula("a1b2c3d4e"))
