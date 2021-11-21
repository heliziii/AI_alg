import random
import numpy


n = int(input())
m = int(input())
start = input().split(" ")
start_x = int(start[0]) - 1
start_y = int(start[1]) - 1
array = [["" for i in range(n)] for j in range(n)]
for i in range(n):
    array[i] = input().split(", ")

number = 15000

arrays = [[0 for i in range(256)] for j in range(number)]
for i in range(number):
    for j in range(256):
        arrays[i][j] = random.randint(1,6)



dict = {'e' : 0, 'w' : 1, 'a' : 2, 's' : 3}


def cal_number(x,y):
    num = 0
    if y == n - 1:
        num += 1
    else:
        num += dict[array[x][y+1]]
    if y == 0:
        num += 1 * 16
    else:
        num += dict[array[x][y-1]]*16
    if x == 0:
        num += 1 * 4
    else:
        num += dict[array[x-1][y]]*4
    if x == n-1:
        num += 1 * 64
    else:
        num += dict[array[x+1][y]]*64
    return num

def cal_core(number, m, samples):
    scores = [0 for l in range(number)]
    level = [0 for l in range(number)]
    for i in range(number):
        x = start_x
        y = start_y
        new_map = [["" for _i in range(n)] for _j in range(n)]
        for j in range(n):
            for k in range(n):
                new_map[j][k] = array[j][k]
        for j in range(m):
            level[i] += 1
            position = cal_number(x,y)
            move = samples[i][position]
            if move == 6:
                move = random.randint(1,5)
            if move == 1:
                level[i] += (m - j)
                break
            if move == 2:
                if y == n - 1:
                    level[i] += (m - j)
                    break
                else:
                    if new_map[x][y+1] == 'e':
                        y += 1
                    elif new_map[x][y+1] == 'w':
                        level[i] += (m - j)
                        break
                    elif new_map[x][y+1] == "a":
                        y += 1
                        scores[i] += 1
                        new_map[x][y] = "e"
                    elif new_map[x][y+1] == "s":
                        if scores[i] == 0:
                            break
                        y += 1
                        scores[i] -= 1
                        new_map[x][y] = "e"
            if move == 3:
                if y == 0:
                    level[i] += (m - j)
                    break
                else:
                    if new_map[x][y-1] == 'e':
                        y -= 1
                    elif new_map[x][y-1] == 'w':
                        level[i] += (m - j)
                        break
                    elif new_map[x][y-1] == "a":
                        y -= 1
                        scores[i] += 1
                        new_map[x][y] = "e"
                    elif new_map[x][y-1] == "s":
                        if scores[i] == 0:
                            break
                        y -= 1
                        scores[i] -= 1
                        new_map[x][y] = "e"
            if move == 4:
                if x == 0:
                    level[i] += (m - j)
                    break
                else:
                    if new_map[x-1][y] == 'e':
                        x -= 1
                    elif new_map[x - 1][y] == 'w':
                        level[i] += (m - j)
                        break
                    elif new_map[x - 1][y] == "a":
                        x -= 1
                        scores[i] += 1
                        new_map[x][y] = "e"
                    elif new_map[x - 1][y] == "s":
                        if scores[i] == 0:
                            break
                        x -= 1
                        scores[i] -= 1
                        new_map[x][y] = "e"
            if move == 5:
                if x == n - 1:
                    level[i] += (m - j)
                    break
                else:
                    if new_map[x+1][y] == 'e':
                        x += 1
                    elif new_map[x + 1][y] == 'w':
                        level[i] += (m - j)
                        break
                    elif new_map[x + 1][y] == "a":
                        x += 1
                        scores[i] += 1
                        new_map[x][y] = "e"
                    elif new_map[x + 1][y] == "s":
                        if scores[i] == 0:
                            break
                        x += 1
                        scores[i] -= 1
                        new_map[x][y] = "e"

    return [i + j for i,j in zip(level, scores)]

maximum = 0
for i in range(20):

    # scores = cal_core(number, m, arrays)
    # arrays = [x for _,x in sorted(zip(scores,arrays))]
    # arrays.reverse()
    # selected = arrays[0:int(0.6 * number)]
    scores = cal_core(number,m,arrays)
    percents = [x/sum(scores) for x in scores]
    indexes = numpy.random.choice(a=range(0,number), size=number, replace=True, p=percents)
    new_arrays = [[0 for i in range(256)] for j in range(number)]
    for j in range(number):
        new_arrays[j] = arrays[indexes[j]]
    arrays = new_arrays

    # for k in range(number):
    #     crossover = random.randint(50,150)
    #     boolean = random.randint(0,100)
    #     if boolean > 30:
    #         index = random.randint(0,int(0.6*number)-2)
    #         arrays[k] = selected[index][0:crossover] + selected[index + 1][crossover:256]
    #     else:
    #         arrays[k] = arrays[random.randint(int(0.6*number),number -1)][0:crossover] + arrays[random.randint(int(0.6*number),number -1)][crossover:256]

    for k in range(0,number - 1,2):
        crossover = random.randint(0,255)
        boolean = random.randint(0,100)
        if boolean > 40:
            tmp = arrays[k][0:crossover]
            arrays[k] = arrays[k+1][0:crossover] + arrays[k][crossover:256]
            arrays[k+1] = tmp + arrays[k+1][crossover:256]


    maximum = max(maximum, max(cal_core(number,m,arrays)))

    p = 0.1
    for k in range(number):
        for j in range(1, int(p * 256)):
            place = random.randint(0, 255)
            arrays[k][place] = random.randint(1,6)

    maximum = max(maximum, max(cal_core(number, m, arrays)))
    print("iteration " + str(i) + " maximum of this " + str(maximum))

print(maximum)