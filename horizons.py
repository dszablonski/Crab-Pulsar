# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 11:09:19 2025

@author: w75158ns
"""
import numpy as np

FILENAME = "horizons_results.txt"

file = open(FILENAME, "r")

text = file.read()

data = text[(text.find("$$SOE")+5):(text.find("$$EOE"))] #start of ephmeris -> end of ephmeris

lines = data.split("\n")

mjd_arr, x_arr, y_arr, z_arr = np.zeros(1, dtype="float"), np.zeros(1, dtype="float"), np.zeros(1, dtype="float"), np.zeros(1, dtype="float")


for date_line in lines[1::2]:
    mjd = date_line[2:17]
    mjd_arr = np.vstack((mjd_arr, mjd))
for pos_line in lines[::2]:
    x_place = pos_line.find("X")
    x = pos_line[(x_place+4):(x_place+25)]
    x_arr = np.vstack((x_arr, x))
    y_place = pos_line.find("Y")
    y = pos_line[(y_place+4):(y_place+25)]
    y_arr = np.vstack((y_arr, y))
    z_place = pos_line.find("Z")
    z = pos_line[(z_place+4):(z_place+25)]
    z_arr = np.vstack((z_arr, z))
    
x_arr = x_arr[2:]
y_arr = y_arr[2:]
z_arr = z_arr[2:]

mjd_arr = mjd_arr[1:-1]

mjd_arr = np.array(mjd_arr, dtype="d")
mjd_arr = mjd_arr - 0.5 #for some reason, midnight at NASA jd is .5 of a day. GET OUT!
#mjd_arr = np.array(mjd_arr, dtype="str")
x_arr = np.array(x_arr, dtype=float)
y_arr = np.array(y_arr, dtype=float)
z_arr = np.array(z_arr, dtype=float)

file.close()

ssb_file = open("ssb_file.txt", "w")

for t, x, y, z in zip(mjd_arr, x_arr, y_arr, z_arr):
    ssb_file.write("{0} {1} {2} {3}\n".format(t[0], x[0], y[0], z[0]))

ssb_file.close()