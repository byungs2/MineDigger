import pyautogui
import time, subprocess
import random
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

### initial position of MineSweeper window
p_ini_l = (249, 420)
p_ini_r = (699, 779)

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
number_list = [dark_number_one, dark_number_two, dark_number_three, dark_number_four]

### for first click of Algorithm
def start_click():
    time.sleep(3)
    pyautogui.leftClick(464, 523)

### making index list of Position of Image
def making_index_list(count, num):
    index_list = []
    count_list = count_nearby(num)
    for index, i in enumerate(count_list[0]):
        if i == count:
            index_list.append(index)
    return index_list

### main body of Algorithm
def judge_situation_click(count_total):
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
        search_position_click(count_list[1], count)
        count += 1
    random_click(count_total)
    
### checking nine blocks near by specific number image
def count_nearby(num):
    count = 0
    count_list = []
    position = search_position(num)
    screen = ImageGrab.grab()
    for i in position:
        for j in range(i[0]-45, i[0]+46, 45):
            for k in range(i[1]-45, i[1]+46, 45):
                rgb = screen.getpixel((j, k-3))
                if rgb == dark_green or rgb == light_green or rgb == dark_flag:
                    count += 1
        count_list.append(count)
        count = 0
    return count_list, position

### getting position list of image of number
def search_position(number):
    position_list = []
    screen = ImageGrab.grab()
    for i in range(p_ini_l[0]+23, p_ini_r[0], 45):
        for j in range(p_ini_l[1]+23, p_ini_r[1], 45):
            rgb = screen.getpixel((i, j))
            rgb2 = screen.getpixel((i+4, j))
            if rgb == number or rgb2 == number:
                position_list.append((i, j))
    return position_list

### click searched image of number
def search_position_click(position, count):
    rgb = []
    screen = ImageGrab.grab() 
    for i in position:
        for j in range(i[0]-45, i[0]+46, 45):
            for k in range(i[1]-45, i[1]+46, 45):
                rgb.append(screen.getpixel((j, k-3)))
        if (dark_green in rgb or light_green in rgb) and rgb.count(dark_flag) == count:
            pyautogui.middleClick(i)
        del rgb[:]
    
### click random block of green fields
def random_click(count_total):
    print(count_total)
    green_field = []
    if count_total%5 == 0:
        green_screen = ImageGrab.grab()
        for i in range(p_ini_l[0]+23, p_ini_r[0], 45):
            for j in range(p_ini_l[1]+23, p_ini_r[1], 45):
                green_rgb2 = green_screen.getpixel((i, j-3))
                green_rgb3 = green_screen.getpixel((i+4, j))
                green_rgb = green_screen.getpixel((i, j))
                if green_rgb2 != dark_flag and green_rgb3 != dark_number_four and (green_rgb == light_green or green_rgb == dark_green):
                    green_field.append((i, j))
        if len(green_field) != 0:
            pyautogui.leftClick(random.choice(green_field))

### bring MineSweeper from chrome browser
def get_website():
    web_driver = webdriver.Chrome('chromedriver.exe')
    web_driver.get('https://www.google.com/search?q=%EC%A7%80%EB%A2%B0%EC%B0%BE%EA%B8%B0&oq=%EC%A7%80%EB%A2%B0%EC%B0%BE%EA%B8%B0&aqs=chrome.0.69i59l3j69i61l3.1603j0j8&sourceid=chrome&ie=UTF-8')
    web_driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div/div/div[1]/div[2]/div/div').click()
    web_driver.find_element_by_xpath('//*[@id="ow23"]/div[1]').click()
    web_driver.find_element_by_xpath('//*[@id="ow23"]/div[2]/g-menu/g-menu-item[1]/div').click()

### execute program   
def execute_program():
    rgb = ()
    count_total = 1
    time.sleep(3)
    start_click()
    time.sleep(0.8)
    while rgb != sky_blue:
        rgb = ImageGrab.grab().getpixel((471, 463))
        judge_situation_click(count_total)
        count_total += 1

get_website()
execute_program()



### just for fun
