import pyautogui
import time, subprocess
import random
from PIL import ImageGrab
### initial position of MineSweeper window
p_ini_l = (560, 278)
p_ini_r = (1009, 637)

### RGB values of numbers and flag images
light_green = (170, 215, 81)
dark_green = (162, 209, 73)
dark_number_three = (211, 47, 47)
dark_number_one = (25, 118, 210)
dark_number_two = (56, 142, 60)
dark_number_four = (123, 31, 162)
dark_flag = (242, 54, 7)
sky_blue = (77, 193, 249)

### list of RGB of number image
number_list = [dark_number_one, dark_number_two, dark_number_three]

### for checking size of window of MineSweeper
def check_position():
    n = 0
    while n < 11:
        print(pyautogui.position())
        time.sleep(1)
        n += 1
        return pyautogui.position()

### for checking RGB of Images
def search_rgb():
    count = 0
    while count < 11:
        screen = ImageGrab.grab()
        print(screen.getpixel(check_position()))
        count += 1

### for first click of Algorithm
def start_click():
    time.sleep(3)
    pyautogui.leftClick(759, 547)

### making index list of Position of Image
def making_index_list(count, num):
    index_list = []
    count_list = count_nearby(num)
    for index, i in enumerate(count_list[0]):
        if i == count:
            index_list.append(index)
    return index_list

### main body of Algorithm
def judge_situation_click():
    count = 1
    for num in number_list:
        count_list = count_nearby(num)
        index = making_index_list(count, num)
        for i in index:
            screen = ImageGrab.grab()
            for j in range(count_list[1][i][0] - 45, count_list[1][i][0] + 46, 45):
                for k in range(count_list[1][i][1] - 45, count_list[1][i][1] + 46, 45):
                    rgb = screen.getpixel((j, k))
                    rgb2 = screen.getpixel((j, k-3))
                    if rgb2 != dark_flag:
                        if rgb == dark_green or rgb == light_green:
                            pyautogui.rightClick(j, k)
        count += 1
        search_position_click(num)

### checking nine blocks near by specific number image
def count_nearby(num):
    count = 0
    count_list = []
    position = search_position(num)
    for i in position:
        screen = ImageGrab.grab()
        for j in range(i[0]-45, i[0]+46, 45):
            for k in range(i[1]-45, i[1]+46, 45):
                rgb = screen.getpixel((j, k-3))
                if rgb == dark_green or rgb == light_green or rgb == dark_flag:
                    count += 1
        count_list.append(count)
        count = 0
    return count_list, position

### getting position list of number image
def search_position(number):
    position_list = []
    screen = ImageGrab.grab()
    for i in range(p_ini_l[0]+23, p_ini_r[0], 45):
        for j in range(p_ini_l[1]+23, p_ini_r[1], 45):
            rgb = screen.getpixel((i, j))
            if rgb == number:
                position_list.append((i, j))
    return position_list

### click all number image
def search_position_click(number):
    screen = ImageGrab.grab()
    for i in range(p_ini_l[0]+23, p_ini_r[0], 45):
        for j in range(p_ini_l[1]+23, p_ini_r[1], 45):
            rgb = screen.getpixel((i, j))
            if rgb == number:
                pyautogui.middleClick(i, j)


rgb = ()
time.sleep(3)
start_click()
time.sleep(1)
while rgb != sky_blue:
    rgb = ImageGrab.grab().getpixel((791, 343))
    judge_situation_click()

### I need more effective Algorithm for soving this

