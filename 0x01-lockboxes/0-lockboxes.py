#!/usr/bin/python3
'''This module contains a function that checks if all the boxes can be opened'''

def open_box(boxes, number, numbers_list):
    '''This function opens the boxes and checks if all the boxes can be opened'''
    if number < 0 or number >= len(boxes):
        return
    numbers_list.add(number)
    for current_number in boxes[number]:
        if current_number not in numbers_list and isinstance(current_number, int):
            open_box(boxes, current_number, numbers_list)

def canUnlockAll(boxes):
    '''This function checks if all the boxes can be opened'''
    numbers_list = set()
    open_box(boxes, 0, numbers_list)
    if len(numbers_list) == len(boxes):
        return True
    return False
