from paint_addons import *
from paint_mass_gen import *
from paint_output import *
from paint_paint import *
from paint_isk_ris import *


mass = mass_gen_custom()
cursor = 'Y'
character = '#'
paint(mass, cursor)

vb = input('Сохранить как текст? Y/N ')
if vb == 'y' or vb == 'Y':
    a = int(input('введите ширину '))
    b = int(input('введите высоту '))
    output_paint(mass, a, b, './text.txt')
elif vb == 'n' or vb == 'N':
    print('Ок')