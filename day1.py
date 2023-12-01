import regex as re

with open("day1.in") as f:
    lines = f.read().strip().split()

#parte 1
def find_numbers(lines):
    number = ''
    for i in lines:
        for char in i:
          if char.isdigit():
            number += char
    return number

numbers = []
for line in lines:
    number = find_numbers(line)
    if number:
        numbers.append(number)

print("numeri trovati >>", numbers)

def check_len(numbers):
    new_numbers = []
    for n in numbers:
        if len(n) == 2:
            new_numbers.append(n)
        elif len(n) > 2:
            new_numbers.append(n[0] + n[-1])
        elif len(n) == 1:
            new_numbers.append(n[0] + n[0])
    return new_numbers

print("numeri finali >>", check_len(numbers))

lista_cifre = check_len(numbers)
cifre_intere = list(map(int, lista_cifre))

def sum(cifre_intere):
    sum = 0
    for cifra in cifre_intere:
        sum += cifra
    return sum

print("somma >>", sum(cifre_intere))
#fine parte 1

#parte 2
def get_calibration_values(lines):
    sum = 0
    digit_dict = {
        # 'zero': 0,
        'one': "o1ne",
        'two': "t2wo",
        'three': "t3hree",
        'four': "f4our",
        'five': "f5ive",
        'six': "s6ix",
        'seven': "s7even",
        'eight': "e8ight",
        'nine': "n9ine"
    }

    for line in lines:
        spelled_digits = (re.findall(r'(?:one|two|three|four|five|six|seven|eight|nine)', line, overlapped=True))
        for d in spelled_digits:
            line = line.replace(d, str(digit_dict[d]))
        reversed_line = line[::-1]
        sum += int(re.search(r"\d", line).group() + re.search(r"\d", reversed_line).group())

    return sum

print("soluzione parte 2 >>", get_calibration_values(lines))