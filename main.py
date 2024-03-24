import time
import os
import math
import threading
import pygame
from pygame.locals import *
pygame.init()
 
Ch = pygame.mixer.Sound(os.path.dirname(__file__) + '\Ch.wav')
Dh = pygame.mixer.Sound(os.path.dirname(__file__) + '\Dh.wav')
Eh = pygame.mixer.Sound(os.path.dirname(__file__) + '\Eh.wav')
Fh = pygame.mixer.Sound(os.path.dirname(__file__) + '\Fh.wav')
Gh = pygame.mixer.Sound(os.path.dirname(__file__) + '\Gh.wav')
Ah = pygame.mixer.Sound(os.path.dirname(__file__) + '\Ah.wav')
Bh = pygame.mixer.Sound(os.path.dirname(__file__) + '\Bh.wav')
Ch2 = pygame.mixer.Sound(os.path.dirname(__file__) + '\Ch2.wav')
bounces = 0
brg = 0
pygame.mixer.Sound.play(Ch)
time.sleep(0.5)
pygame.mixer.Sound.play(Ch)
time.sleep(0.5)
pygame.mixer.Sound.play(Ch)
time.sleep(0.5)
pygame.mixer.Sound.play(Ch)
time.sleep(0.5)
pygame.mixer.Sound.play(Ch)
 
 
# // below are the note sequence and length which can be changed to whatever you want
seqlength = 16
def wally():
          global brg
          notesequence = [Ch,Dh,Eh,Fh,Gh,Ah,Bh,Ch2,Ch2,Bh,Ah,Gh,Fh,Eh,Dh,Ch,]
          pygame.mixer.Sound.set_volume(notesequence[brg], 0.5)
          pygame.mixer.Sound.play(notesequence[brg])
#
          
brg -= 1
 
# // gravitational field strength (N)
g = 9.81
#
 
# // bounce velocity multiplier
b = 1.06
#
 
# // x(v1) and y(v2) velocity (m/s)
v1 = 2
v2 = 2
#
 
v0 = math.sqrt(v1 * v1 + v2 * v2)
v3 = v1 / v0
v4 = v2 / v0
if v1 == 0.001 and v2 == 0.001:
     v0 = 0
     v3 = 0
     v4 = -1
t = 0
tmax = 100
 
# // fps (numbers above 100 may cause lag)
tstep = 60
#
 
tstep = 1 / tstep
maxbounces = 1000000000
 
# // starting position (m)
x = 6
y = -5
#
 
# // outer circle diameter (m) (resmult changes the zoom)
resolution = 20
resmult = 12
#
 
 
 
# // size and size multiplier
sizemult = 1.05
size = 1
 
if x == 0:
     x += 0.0000001
if y == 0:
     y += 0.0000001
x += resolution/2
y += resolution/2
if x >= resolution:
     x = resolution - 1
if y >= resolution:
     y = resolution - 1
x1 = (t * v3 * v0) + x
y1 = (-g * t * t) + (t * v4 * v0) + y
x2 = (t * v3 * v0) + x
y2 = (-g * t * t) + (t * v4 * v0) + y
engle=0.00000
 
# // screen resolution (px)
screenwidth = 1920
screenheight = 1080
#
 
window = pygame.display.set_mode((screenwidth, screenheight))
cover = pygame.Surface((1920,1080))
cover.set_alpha(int(v0))
cover.fill((0,0,0))
window.fill((0, 0, 0))
xdis = (screenwidth - resolution * 4 * resmult) / 2
ydis = (screenheight - resolution * 4 * resmult) / 2
red = 255
grn = 0
blu = 0
col = 0
num = 0
xh = x
yh = y
countoor = 0
pygame.draw.circle(window, (255, 255, 255), 
                 [(resolution * 2 * resmult) + xdis, (resolution * 2 * resmult) + ydis], resolution*2 * resmult + 8, 8)
pygame.display.update()
time.sleep(1)
t = 0
while bounces != maxbounces and size <= resolution + 0.5:
    brg+=1
    if brg >= seqlength:
         brg = 0
    xy = math.sqrt((x - resolution/2) * (x - resolution/2) + (y - resolution/2) * (y - resolution/2))
    xengle = ((x - resolution/2))
    yengle = ((y - resolution/2))
    hehe = math.tan(math.radians(45))
    engless =  math.degrees(math.atan(v2/v1))
    if engless < 0:
         engless += 360
    if v1 > 0 and v2 > 0 and engless > 90:
         engless -= 180
    if v1 < 0 and v2 > 0 and engless > 180:
         engless -= 180
    elif v1 < 0 and v2 > 0 and engless <= 90:
         engless -= 180
    if v1 < 0 and v2 < 0 and engless > 270:
         engless -= 180
    elif v1 < 0 and v2 < 0 and engless <= 180:
         engless -= 180
    if v1 > 0 and v2 < 0 and engless > 360:
         engless -= 180
    elif v1 > 0 and v2 < 0 and engless <= 270:
         engless -= 180
    engless -= 180
    englseee = math.degrees(math.atan(-xengle / yengle))
    engler = 2 * englseee - engless - 180
    v0 = math.sqrt(v1 * v1 + v2 * v2)
    v4 = math.sin(math.radians(engler))
    v3 = math.cos(math.radians(engler))
    v2 = math.sin(math.radians(engler)) * v0
    v1 = math.cos(math.radians(engler)) * v0
    v0 = v0 * b
    while t <= tmax:
        col += 1 / 255 * 1
        if col * 255 >= 1530:
                col = 0
        if (col - (col % 1)) % 6 == 0:
            grn = col * 255
        elif (col - (col % 1)) % 6 == 1:
            red = 510 - col * 255
        elif (col - (col % 1)) % 6 == 2:
            blu = col * 255 - 510
        elif (col - (col % 1)) % 6 == 3:
            grn = 1020 - col * 255
        elif (col - (col % 1)) % 6 == 4:
            red = col * 255 - 1020
        elif (col - (col % 1)) % 6 == 5:
            blu = 1530 - col * 255
        if red > 255:
            red = 255
        if red < 0:
            red = 0        
        if blu > 255:
            blu = 255
        if blu < 0:
            blu = 0
        if grn > 255:
            grn = 255
        if grn < 0:
            grn = 0
        te = t - 0.000000001
        xh = t * v3 * v0 + x
        yh = -g * t **2 + t * v4 * v0 + y
        if ((yh - (resolution / 2)) * (yh - (resolution / 2))) + ((xh - (resolution / 2)) * (xh - (resolution / 2))) < (resolution/2 - (0.5 * (size * sizemult)))  * (resolution/2 - (0.5 * (size * sizemult))):
            x1 = t * v3 * v0 + x
            y1 = -g * t**2 + t * v4 * v0 + y
            x2 =  te * v3 * v0 + x
            y2 = - g * te**2 + te * v4 * v0 + y
            if size > resolution - 2 / resmult:
                 size = resolution - 2 / resmult
            op = 96
            rud = red/255 * op
            jrn = grn/255 * op
            blr = blu/255 * op
 
            # // trail length - increasing the number after the % with increase the length (decreases stuttering)
            if countoor % 4 == 0:
               window.blit(cover, (0, 0))
            #
 
            pygame.draw.circle(window, (red, grn, blu), 
                            [round(xh*4 * resmult) + xdis, round((resolution - yh)*4 * resmult) + ydis], 2 * resmult * size, 0)
            pygame.draw.circle(window, (rud, jrn, blr), 
                            [round(xh*4 * resmult) + xdis, round((resolution - yh)*4 * resmult) + ydis], 2 * resmult * size, 2)
            pygame.draw.circle(window, (255, 255, 255), 
                 [(resolution * 2 * resmult) + xdis, (resolution * 2 * resmult) + ydis], resolution*2 * resmult + 8, 8)
            pygame.display.update()
 
            # // speed - increasing the number after the / will increase the speed (may cause stuttering)
            time.sleep(tstep / 4)
            #
        else:
             if t <= tstep * 1: 
                    size = size / sizemult
             else:
                    size = size * sizemult
                    bounces += 1
                    x = x1
                    y = y1
                    #v1 = ((x3 - x2)  / (0.000000001)) 
                    v2 = ((y1 - y2)  / (0.000000001)) 
                    t = tmax
        t += tstep
        countoor += 1
    t = 0
    globals()["wal"+str(bounces)] = threading.Thread(target=wally)
    globals()["wal"+str(bounces)].start()
    