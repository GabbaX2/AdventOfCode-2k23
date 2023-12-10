import sys

def генератор_разницы(история: list[int]):
    предыдущее = история[0]
    for значение in история[1:]:
        yield значение - предыдущее
        предыдущее = значение
    if len(история) == 1:
        yield 0

def экстраполяция(ниже: int, выше: int, влево = False):
    return выше - ниже if влево else выше + ниже

def решение(данные: list[list[int]], влево = False):
    конечные_значения = []
    индекс = 0 if влево else -1
    for история in данные:
        значения = [история[индекс]]
        while True:
            история = list(генератор_разницы(история))
            значения.append(история[индекс])
            if история.count(0) == len(история):
                break
        текущее_значение = 0
        for значение2 in значения[::-1]:
            текущее_значение = экстраполяция(текущее_значение, значение2, влево)
        конечные_значения.append(текущее_значение)
    return sum(конечные_значения)

def часть1(данные: list[list[int]]):
    print(f"Часть 1: {решение(данные)}")

def часть2(данные: list[list[int]]):
    print(f"Часть 2: {решение(данные, True)}")

if __name__ == '__main__':
    with open('day9.in') as файл:
        строки = файл.readlines()
    данные = [[int(значение) for значение in строка.split()] for строка in строки]
    for тест_кейс in [(0,3,3),(3,15,18),(0,1,1),(1,6,7),(7,21,28),(0,2,2),(2,6,8),(8,15,23),(23,45,68),(-1,1,0), (-1,-1,-2), (1,-1,0), (-3,1,-2), (0,2,2), (4,-2,2), (2,-2,0), (1,-1,0), (-8,3,-5), (-4,4,0), (-3,4,1), (0,0,0), (4,-4,0)]:
        получено = экстраполяция(*тест_кейс[0:2])
        assert получено == тест_кейс[2], f"Ожидалось {тест_кейс[2]}, получено {получено} для {тест_кейс}"
    часть1(данные)
    часть2(данные)
