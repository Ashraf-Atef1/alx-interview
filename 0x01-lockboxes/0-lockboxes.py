#!/usr/bin/python3
'''This module contains a function that checks
if all the boxes can be opened'''


def open_box(boxes, number, numbers_list):
    '''This function opens the boxes and checks
    if all the boxes can be opened'''
    if isinstance(number, int) and number >= 0 and number < len(boxes):
        numbers_list.add(number)
        for c_number in boxes[number]:
            if c_number not in numbers_list:
                open_box(boxes, c_number, numbers_list)


def canUnlockAll(boxes):
    '''This function checks if all the boxes can be opened'''
    numbers_list = set()
    open_box(boxes, 0, numbers_list)
    if len(numbers_list) == len(boxes):
        return True
    return False
