"""
COMP 1701 Assignment 1 - Task 1:Daily Activity Estimation Module
Author: 
"""

import math

def estimate_stride_length(height_cm):
    
    height_inches = height_cm * 0.393701
    stride_m = 0.415 * height_inches * 0.0254
    return stride_m

def calculate_daily_distance(steps, stride_length):
    
    distance_km = (steps * stride_length) / 1000
    return distance_km

def estimate_calories_burned(distance_km):

    calories = distance_km * 60
    return calories

def main():

    height_cm = float(input("Enter your height in cm: "))
    if height_cm <= 0:
        print("Height must be a positive number. Please try again.")
        return
    
    steps = int(input("Enter your number of steps today: "))
    if steps < 0:
        print("Step count cannot be negative. Please try again.")
        return        
    
    stride_length = estimate_stride_length(height_cm)
    daily_distance_km = calculate_daily_distance(steps, stride_length)
    calories_burned = estimate_calories_burned(daily_distance_km)
    
    rounded_distance = round(daily_distance_km, 1)  #Nearest tenth
    rounded_calories = round(calories_burned / 10) * 10  #Nearest ten
    
    print("Estimated walking distance:", rounded_distance, "km")
    print("Estimated calories burnt:", rounded_calories)

main()
