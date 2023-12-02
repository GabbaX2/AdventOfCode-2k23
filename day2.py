with open('day2.in') as f:
    lines = [line.rstrip() for line in f]

game_id: int = 1
somma = 0
potenza = 0

max_red = 12
max_blue = 14
max_green = 13

for line in lines:
    blue_max, red_max, green_max = 0, 0, 0
    _, cubes = line.split(':')
    grabs = cubes.split(';')

    for this_grab in grabs:
        grabbed = [g.strip() for g in this_grab.split(',')]
        for setx in grabbed:
            n, color = setx.split(' ')

            if color == 'blue':
                if int(n) > blue_max:
                    blue_max = int(n)
            elif color == 'red':
                if int(n) > red_max:
                    red_max = int(n)
            elif color == 'green':
                if int(n) > green_max:
                    green_max = int(n)

    if blue_max <= max_blue and green_max <= max_green and red_max <= max_red:
        somma += game_id
    game_id += 1

    #parte 2
    p = max_red * max_green * max_blue
    potenza += p

#stampa entrambe le parti
print(f'somma parte 1 >> {somma}')
print(f'potenza (parte 2) >> {potenza}')