#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/12/06

@author: johannes
"""
from pprint import pprint


def path_to_com(planets: dict, planet: str):
    key = planet
    path = []
    while key != 'COM':
        next_planet = planets[key]
        path.append(next_planet)
        key = next_planet
    return path


def find_min_dist(planets: dict, planet1: str, planet2: str):
    path1, path2 = [path_to_com(planets, planet) for planet in (planet1, planet2)]
    common_planets = set(path1).intersection(set(path2))
    # print(path1)
    index1 = min(path1.index(planet) for planet in common_planets)
    closest_common_planet = path1[index1]
    index2 = path2.index(closest_common_planet)
    return index1 + index2


with open('orbits.txt', 'r') as ifile:
    planets = {}

    for line in ifile.readlines():
        line = line[:-1]
        left, right = line.split(')')
        planets[right] = left

    print(find_min_dist(planets, 'YOU', 'SAN'))
