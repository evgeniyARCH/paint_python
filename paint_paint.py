import random
import itertools
import array
import os
import time
import subprocess
from paint_addons import *
from paint_output import *
from paint_isk_ris import *
    
def paint(mass,c):
    clear = lambda: os.system('clear')
    clear()
    px = [' ',1,1]
    x = 1
    y = 1
    nol = 0
    
    while nol == 0:
        output(mass)
        dist = 1
        cord = input('введите команду ')
        if cord == 'up' or cord == 'UP':
            dist = 0
            dist = chislo_prov(dist, 'введите на сколько символов переместить ')
            y-=dist
        elif cord == 'down' or cord == 'DOWN':
            dist = 0
            dist = chislo_prov(dist, 'введите на сколько символов переместить ')
            y+=dist
        elif cord == 'left' or cord == 'LEFT':
            dist = 0
            dist = chislo_prov(dist, 'введите на сколько символов переместить ')
            x-=dist
        elif cord == 'right' or cord == 'RIGHT':
            dist = 0
            dist = chislo_prov(dist, 'введите на сколько символов переместить ')
            x+=dist
        elif cord == 'paint':
            d = input('введите символ ввода ')
            coord_ris([d,x,y], mass)
        elif cord == 'text':
            text = input('введите текст ')
            paint_text(text,x, y, mass)
            # x = crd[0]
            # y = crd[1]
            # mass = crd[2]
        elif cord == 'sqare':
            a = 0
            a = chislo_prov(a, 'введите сторону квадрата ')
            smb = input('введите символ ')
            sqar = paint_sqare(a, smb, x, y, mass)
            x = sqar[0]
            y = sqar[1]
            mass = sqar[2]
        elif cord == 'sqare2':
            a = 0
            a = chislo_prov(a, 'введите диагональ ')
            smb = input('введите символ ')
            sqar2 = paint_sqare_ft(a, smb, x, y, mass)
            x = sqar2[0]
            y = sqar2[1]
            mass = sqar2[2]
        elif cord == 'pr':
            a = 0
            b = 0
            a = chislo_prov(a, 'введите ширину прямоугольника ')
            b = chislo_prov(b, 'введите высоту прямоугольника ')
            smb = input('введите символ ')
            paint_rectangle_nofill(a, b, smb, x, y, mass)
        elif cord == 'pr_fill':
            a = 0
            b = 0
            a = chislo_prov(a, 'введите ширину прямоугольника ')
            b = chislo_prov(b, 'введите высоту прямоугольника ')
            smb = input('введите символ ')
            paint_rectangle(a, b, smb, x, y, mass)

        elif cord == 'exit':
            nol = 1

        elif cord == 'cord':
            x = 0
            y = 0
            x = chislo_prov(x,'введите x ')
            y = chislo_prov(x,'введите y ')

        else:
            x+=1
            
        if dist == 0:
            x+=1
        if x > len(mass[0]) or x < 1 or y > len(mass) or y < 1:
            x = 1
            y = 1
        sx = x
        sy = y
        ns = coord_isk([sx,sy], mass)
        print(ns)
        nx = [ns,sx,sy]
        coord_ris(px, mass)
        px = nx

        coord_ris([c,x,y], mass)

        clear()

        time.sleep(0.1)
