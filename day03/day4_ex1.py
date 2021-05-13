#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/12/05

@author: johannes
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int

    @staticmethod
    def from_instruction(p: 'Point', instruction: str):
        direction = instruction[0]
        steps = int(instruction[1:])
        if direction == 'R':
            return Point(p.x + steps, p.y)
        elif direction =='L':
            return Point(p.x - steps, p.y)
        elif direction == 'U':
            return Point(p.x, p.y + steps)
        elif direction == 'D':
            return Point(p.x, p.y - steps)
        else:
            raise ValueError(f'Invalid direction: {direction}.')

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

@dataclass
class Segment:
    start: Point
    end: Point


def manhattan_dist(p1: Point, p2: Point):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def crossing(s1: Segment, s2: Segment) -> Point:
    dir1 = s1.start.x - s1.end.x
    dir2 = s2.start.x - s2.end.x

    if dir1 == dir2 or (dir1 != 0 and dir2 != 0):
        return None

    s_x, s_y = (s1, s2) if dir2 == 0 else (s2, s1)

    if (s_x.start.x <= s_y.start.x <= s_x.end.x) and (s_y.start.y <= s_x.start.y <= s_y.end.y):
        return Point(s_y.start.x, s_x.start.y)


def get_points(path: List[str]) -> List[Point]:
    origin = Point(0, 0)
    points = [origin]
    for instruction in path:
        new_point = Point.from_instruction(points[-1], instruction)
        points.append(new_point)
    return points


def get_segments(points: List[Point]) -> List[Segment]:
    segments = [Segment(p1, p2) for p1, p2 in zip(points[:-1], points[1:])]
    return segments


def get_crossings(segments1: List[Segment], segments2: List[Segment]) -> List[Point]:
    crossings = []
    origin = Point(0, 0)
    for seg_i in segments1:
        for seg_j in segments2:
            if (c := crossing(seg_i, seg_j)) is not None and c != origin:
                crossings.append(c)
    return crossings


with open('test2_paths.txt', 'r') as ifile:
    path1 = ifile.readline().split(',')
    path2 = ifile.readline().split(',')

    print(path1)
    print(path2)

    points1 = get_points(path1)
    points2 = get_points(path2)

    segments1 = get_segments(points1)
    segments2 = get_segments(points2)

    print(points1)
    print(segments1)

    crossings = get_crossings(segments1, segments2)
    print(crossings)
    origin = Point(0, 0)
    min_dist = min(manhattan_dist(origin, c) for c in crossings)
    print(min_dist)
