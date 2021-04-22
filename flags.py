#!/usr/local/bin/python3
import pyautogui
import json

from tkinter import *
import tkinter
top = Tk()


pyautogui.MINIMUM_DURATION = 0.001
geojson = json.load(open("countries.json","r", encoding="utf-8"))
a = pyautogui.locateAllOnScreen('locator.png', grayscale=True, confidence=.5)
locator = next(a)
countries = sorted([x['properties']['CNTRY_NAME'] for x in geojson["features"]])




x = locator.left + 304
y = locator.top + 62
play_x = 782
play_y = 482

red_x = x-95
red_y = y+370
black_x = x-125
black_y = y+290

def lon_lat_to_xy(lon, lat):
    lon = lon + 180 # shift right so 0  ... 360
    lon = (lon / 360) * play_x
    lon = lon + x
    lat = lat + 90 # shift right so 0  ... 180
    lat = (lat / 180) * play_y
    lat = (y + play_y) - lat 
    return (lon, lat)



Lb1 = Listbox(top,selectmode="browse")
for country in countries:
    Lb1.insert("end", country)
Lb1.pack()

def go(event):
    global country
    cs = Lb1.curselection()
    country = Lb1.get(cs)
    pyautogui.click(x=black_x,y=black_y,duration=0.1, _pause=False)
    for feature in geojson["features"]:
        last_x = last_y = 0
        print(feature['properties']['CNTRY_NAME'])
        if feature['properties']['CNTRY_NAME'] == country:
            pyautogui.click(x=red_x,y=red_y,duration=0.1)
        if feature["geometry"]:
            if feature["geometry"]["type"]  == "Polygon":
                for coords in feature["geometry"]["coordinates"]:
                    
                    for coord in coords:
                        pos_x, pos_y = lon_lat_to_xy(coord[0], coord[1])
                        if abs(pos_x - last_x) > 3 or abs(pos_y - last_y) > 3:
                            pyautogui.moveTo(pos_x, pos_y, duration=0.001,_pause=False)
                            last_x = pos_x
                            last_y = pos_y
                            pyautogui.mouseDown(_pause=False)
                pyautogui.mouseUp(_pause=False)
                # mouse up
            elif feature["geometry"]["type"] == "MultiPolygon":
                for coords in feature["geometry"]["coordinates"]:
                    for polygons in coords:
                        for coord in polygons:
                            if abs(pos_x - last_x) > 3 or abs(pos_y - last_y) > 3:
                                pos_x, pos_y = lon_lat_to_xy(coord[0], coord[1])
                                pyautogui.moveTo(pos_x, pos_y, duration=0.001,_pause=False)
                                pyautogui.mouseDown(_pause=False)
                    pyautogui.mouseUp(_pause=False)
                    # mouse up
        if feature['properties']['CNTRY_NAME'] == country:
            pyautogui.click(x=black_x,y=black_y,duration=0.1, _pause=False)

Lb1.bind('<Double-1>', go)
top.mainloop()

