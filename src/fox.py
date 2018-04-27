#!/usr/bin/env python3

import os, re, sys

arduinoProjectDirectory =  os.path.dirname(os.path.realpath(__file__)) + "/arduino"
sketchSource = os.path.dirname(os.path.realpath(__file__)) + "/source.txt"
sketchDestination = os.path.dirname(os.path.realpath(__file__)) + "/arduino/src/sketch.ino"

callsign = input("Callsign: ")
while not re.match("^[A-Za-z0-9]*$", callsign):
    callsign = input("Enter a valid callsign: ")

initialDelay = input("Start-up delay (seconds): ")
while not re.match("^[0-9]*$", initialDelay) or int(initialDelay) > 120 or int(initialDelay) < 1:
    initialDelay = input("Enter a number between 1 and 120: ")

songIterations = input("Number of song iterations (~4.5 seconds each): ")
while not re.match("^[0-9]*$", songIterations) or int(songIterations) > 10 or int(songIterations) < 1:
    songIterations = input("Enter a number between 1 and 10: ")

silenceDuration = input("Silence duration (seconds): ")
while not re.match("^[0-9]*$", silenceDuration) or int(silenceDuration) > 180 or int(silenceDuration) < 15:
    silenceDuration = input("Enter a number between 15 and 180: ")

wpm = input("Morse WPM (20 is recommended): ")
while not re.match("^[0-9]*$", wpm) or int(wpm) > 60 or int(wpm) < 12:
    wpm = input("Enter a number between 12 and 60: ")

print("")
print("")
print("Callsign: " + callsign)
print("Start-up delay: " + initialDelay + " seconds")
print("Song iterations: " + songIterations + " (~" + str(int(songIterations) * 4.5) + " seconds)")
print("Silence duration: " + silenceDuration + " seconds")
print("Morse speed: " + wpm + " wpm")

response = input("Are these setting correct [y/N]? ")
if not response.lower() == "y" and not response.lower() == "yes":
    sys.exit()

f = open(sketchSource, "r")
contents = f.read()
f.close()

contents = contents.replace("%CALLSIGN%", callsign)
contents = contents.replace("%INITIAL_DELAY%", str(int(initialDelay) * 1000))
contents = contents.replace("%NUM_SONGS%", songIterations)
contents = contents.replace("%SILENCE_DURATION%", str(int(silenceDuration) * 1000))
contents = contents.replace("%WPM%", wpm)

f = open(sketchDestination, "w")
f.write(contents)
f.close()

os.chdir(arduinoProjectDirectory)
os.system("ino clean")
os.system("ino build")
os.system("ino upload")