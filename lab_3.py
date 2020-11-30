from PIL import Image, ImageDraw
WIDTH = 540
HEIGHT = 960

screen = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))

with open('DS8.txt') as file:
    dots = file.readlines()

for i in range(len(dots)):
    dots[i] = tuple(list(map(int, dots[i].strip('\n').split())))
    screen.putpixel(dots[i], (0, 0, 0))

dots_count = len(dots)
P = list(range(dots_count))

for i in range(1, dots_count):
    if dots[P[i]][0] < dots[P[0]][0]:
        P[i], P[0] = P[0], P[i]

H = [P[0]]
P.append(P.pop(0))

def rotate(A,B,C):
    return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

while True:
    right = 0
    for i in range(1, len(P)):
        if rotate(dots[H[-1]], dots[P[right]], dots[P[i]]) < 0:
            right = i
        
    if P[right] == H[0]:
        break
    else:
        H.append(P.pop(right))

draw = ImageDraw.Draw(screen)

for i in range(len(H)-1):
    d1 = dots[H[i-1]]
    d2 = dots[H[i]]
    draw.line((d1[0], d1[1], d2[0], d2[1]),'blue', 2)

screen.show()
screen.save('lab_3.png')
