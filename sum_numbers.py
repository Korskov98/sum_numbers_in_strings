

def sum_numbers_in_strings(strings):
    sum = 0
    for val in strings:
        length = len(val)
        i = 0
        while i < length:
            s_int = ''
            while i < length and '0' <= val[i] <= '9':
                s_int += val[i]
                i += 1
            i += 1
            if s_int != '':
                sum += int(s_int)
    return sum

strings = ['hello world 123', '345 is greater then 111', 'hello 67'];
total = sum_numbers_in_strings(strings)
print(total)
