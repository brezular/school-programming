"""
Bubble sort with visualization - the largest digit bubbles up to the right
brezular 2025
"""

import time
import random
import tkinter

R = 800        # size of canvas
N = 9          # number of digits for ordering
START_POS = 40 # start position of number on canvas
GAP= 90        # gap between numbers on canvas
DELAY = 2      # delay in seconds

# Generate list of unique random numbers
def generate_list():
    l = []
    while len(l) != N:
        digit = random.randint(0,9)
        if digit not in l:
            l.append(digit)        # add unique number to list
    return l

# Draw numbers on canvas
def draw_numbers(random_list):
    my_canvas.delete("all")
    shift = 0
    for number in random_list:
        my_canvas.create_text(START_POS+shift, R/4, font=("Arial", 50), text=number)
        shift += GAP
    my_canvas.update()

# Bubble sort with visualization - the largest digit bubbles up to the right
def sort_list(random_list):
    for k in range(N-1):
        draw_numbers(random_list)
        sorted_list_flag = True
        for i in range(N-1-k):       # we sort only unsosrted part of list
            if random_list[i] > random_list[i+1]:
                random_list[i], random_list[i+1] = random_list[i+1], random_list[i]
                sorted_list_flag = False
            time.sleep(DELAY)           
            draw_numbers(random_list)

        if sorted_list_flag:
            break   

""" BODY """

# Inicialization of tkinter GUI
my_canvas = tkinter.Canvas(bg="white", width=R, height=R/2)
my_canvas.pack()

# Generate unsorted list of unique random numbers  
random_list = generate_list()

# Start Bubble sorting with visualization
sort_list(random_list)

# Start tkinter main loop
tkinter.mainloop()




        
       



