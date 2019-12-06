#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/12/06

@author: johannes
"""
from pprint import pprint


def sum_orbits(planets: dict, planet: str):
    try:
        child_planets = planets[planet]
    except KeyError:
        return 0
    else:
        sum_ = 0
        for child_planet in child_planets:
            sum_ += sum_orbits(planets, child_planet) + 1
            pass
    return sum_


with open('orbits.txt', 'r') as ifile:
    planets = {}

    for line in ifile.readlines():
        line = line[:-1]
        left, right = line.split(')')
        planets.setdefault(left, []).append(right)

    pprint(planets)
    total_orbits = sum(sum_orbits(planets, planet) for planet in planets)
    print(total_orbits)

