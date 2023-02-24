#!/usr/bin/python3

"""square units of water will be retained after it rains"""


def rain(walls):
    if not walls:
        return 0

    n = len(walls)
    lmax = [0] * n
    rmax = [0] * n

    lmax[0] = walls[0]
    for i in range(1, n):
        lmax[i] = max(lmax[i - 1], walls[i])

    rmax[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        rmax[i] = max(rmax[i + 1], walls[i])

    total_water = 0
    for i in range(n):
        water_height = min(lmax[i], rmax[i]) - walls[i]
        if water_height > 0:
            total_water += water_height

    return total_water
