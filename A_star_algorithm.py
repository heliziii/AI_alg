n = int(input())
start = input()
start = start.split(" ")
x_start = int(start[0]) - 1
y_start = int(start[1]) - 1
end = input()
end = end.split(" ")
x_end = int(end[0]) - 1
y_end = int(end[1]) - 1
self_levels = input();
self_levels = self_levels.split(" ")
array = [[] * n] * n
seen = []
for i in range(n):
    self_levels[i] = int(self_levels[i])
for i in range(n):
    array[i] = input().split(" ")

find = 0

def dfs(x,y,c):
   # print(x,y,c)
    global find
    if c==0:
        find=1
        return
    else:
        for i in range(-1,2):
            for j in range(-1,2):
                if (abs(i+j) == 1):
                    if (x + i <= n - 1) and (x + i >= 0) and (y + j <= n - 1) and (y + j >= 0) and mark[x+i][y+j] == False and (x+i,y+j) not in seen:

                        if (mark[x + i][y_now + j]):
                            continue

                        now = array[x + i][y + j]

                        if now[0] == "m":
                            if self_levels[0] < int(now[1]):
                                continue
                            else:
                                seen.append((x+i,y+j))
                                dfs(x+i,y+j,c-1)
                                seen.remove((x+i,y+j))
                                continue
                        if now[0] == "M":
                            if self_levels[1] < int(now[1]):
                                continue
                            else:
                                seen.append((x+i,y+j))
                                dfs(x+i,y+j,c-1)
                                seen.remove((x+i,y+j))
                                continue
                        if now[0] == "h":
                            if self_levels[2] < int(now[1]):
                                continue
                            else:
                                seen.append((x+i,y+j))
                                dfs(x+i,y+j,c-1)
                                seen.remove((x+i,y+j))
                                continue
                        if now[0] == "t":
                            if self_levels[3] < int(now[1]):
                                continue
                            else:
                                seen.append((x+i,y+j))
                                dfs(x+i,y+j,c-1)
                                seen.remove((x+i,y+j))
                                continue
                        if now[0] == "d":
                            if self_levels[4] < int(now[1]):
                                continue
                            else:
                                seen.append((x+i,y+j))
                                dfs(x+i,y+j,c-1)
                                seen.remove((x+i,y+j))
                                continue
                        if now[0] == "e":
                            seen.append((x+i, y+j))
                            dfs(x+i, y+j, c - 1)
                            seen.remove((x+i, y+j))

    return

def cost(x,y):
    global find
    find = 0
 #   if x==3 and y==3:
  #      print('aaaaaaaaaa')
    seen.append((x,y))
    dfs(x,y,3)
    seen.remove((x,y))
    if find:
        return 0
    return 50000

def h(x,y):
    return abs(x_end - x) + abs(y_end - y) + cost(x,y)


x_now = x_start
y_now = y_start

g = [[10000000 for i in range(n)] for j in range(n)]
g[0][0] = 0
candidate_set = set()


parent_set = [[(0,0) for i in range(n)] for j in range(n)]
mark = [[False for i in range(n)] for j in range(n)]
mark[0][0] = True

for k in range(20):
    if (x_now == x_end) and (y_now == y_end):
        break
    else:
        for i in range(-1,2):
            for j in range(-1,2):
                if (abs(i+j) == 1):
                    if (x_now + i <= n - 1) and (x_now + i >= 0) and (y_now + j <= n - 1) and (y_now + j >= 0):

                        if (mark[x_now + i][y_now + j]):
                            continue

                        now = array[x_now + i][y_now + j]

                        if now[0] == "m":
                            if self_levels[0] < int(now[1]):
                                continue
                            else:
                                candidate_set.add((x_now +i, y_now + j))
                                g[x_now + i][y_now + j] = g[x_now][y_now] + 1
                                parent_set[x_now + i][y_now + j] = (x_now,y_now)
                                continue
                        if now[0] == "M":
                            if self_levels[1] < int(now[1]):
                                continue
                            else:
                                candidate_set.add((x_now +i, y_now + j))
                                g[x_now + i][y_now + j] = g[x_now][y_now] + 1
                                parent_set[x_now + i][y_now + j] = (x_now, y_now)
                                continue
                        if now[0] == "h":
                            if self_levels[2] < int(now[1]):
                                continue
                            else:
                                candidate_set.add((x_now + i, y_now + j))
                                g[x_now + i][y_now + j] = g[x_now][y_now] + 1
                                parent_set[x_now + i][y_now + j] = (x_now, y_now)
                                continue
                        if now[0] == "t":
                            if self_levels[3] < int(now[1]):
                                continue
                            else:
                                candidate_set.add((x_now +i, y_now + j))
                                g[x_now + i][y_now + j] = g[x_now][y_now] + 1
                                parent_set[x_now + i][y_now + j] = (x_now, y_now)
                                continue
                        if now[0] == "d":
                            if self_levels[4] < int(now[1]):
                                continue
                            else:
                                candidate_set.add((x_now +i, y_now + j))
                                g[x_now + i][y_now + j] = g[x_now][y_now] + 1
                                parent_set[x_now + i][y_now + j] = (x_now, y_now)
                                continue
                        if now[0] == "e":
                            candidate_set.add((x_now + i, y_now + j))
                            g[x_now + i][y_now + j] = g[x_now][y_now] + 1
                            parent_set[x_now + i][y_now + j] = (x_now, y_now)

        min = 10000000
        new_node = (0,0)
        for i in candidate_set:
            print(i, end = "")
            print(":f = " + str(g[i[0]][i[1]]) + " + "  + str(h(i[0], i[1])))
            if g[i[0]][i[1]] + h(i[0], i[1]) < min:
                min = h(i[0], i[1]) + g[i[0]][i[1]]
                new_node = i

        print("* ",  end = "")
        print(new_node, end= "")
        print("expands")
        candidate_set.remove(new_node)
        mark[new_node[0]][new_node[1]] = True
        x_now = new_node[0]
        y_now = new_node[1]





path = []
path.append((x_end ,y_end))
now = (x_end,y_end)
while (True):
    parent = parent_set[now[0]][now[1]]
    path.append(parent)
    now = parent
    if parent == (0,0):
        break


for i in range((len(path)-1),-1,-1):
    print(path[i], end= " ")














