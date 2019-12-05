#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/12/05

@author: johannes
"""


def fuel(mass):
    if mass <= 0:
        return 0
    else:
        return mass + fuel(int(mass/3) - 2)


with open('masses.txt', 'r') as ifile:
    total_fuel = 0
    for line in ifile.readlines():
        mass = int(line)
        fuel_ = fuel(int(mass/3) - 2)
        total_fuel += fuel_


    print(total_fuel)

