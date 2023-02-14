import keyboard


row = int(input())
col = int(input())

ar=[]

x , y = (1 , 1)
for i in range(col):
    ar.append([])
    for j in range(row):
        ar[i].append(0)

def display():
    global x , y , ar
    ar[y][x] = 1
    for l in range(col):
        print(ar[l])




def up():
    global x , y , ar
    ar[y][x] = 0
    y -= 1
    display()
def down():
    global x , y , ar
    ar[y][x] = 0
    y += 1
    display()
def left():
    global x , y , ar
    ar[y][x] = 0
    x -= 1
    display()
def right():
    global y , ar
    ar[y][x] = 0
    x += 1
    display()



running = True
while running:
    event = keyboard.read_event()
    if event.name == "up":
        up()
        pass
    if event.name == "down":
        down()
        pass
    if event.name == "left":
        left()
        pass
    if event.name == "right":
        right()
        pass
