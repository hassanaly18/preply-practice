"""
COMP 1701 Assignment 1 - Task 2: Weekly Analytics and System Integration
Author: 
"""

import math

def estimate_stride_length(height_cm):
    
    stride_m = (math.log(height_cm) / 100) * height_cm / 100
    return stride_m

def calculate_daily_distance(steps, stride_length):
    
    distance_km = (steps * stride_length) / 1000    
    return distance_km

def estimate_weekly_distance(day1, day2, day3, day4, day5, day6, day7):
    
    weekly_distance = day1 + day2 + day3 + day4 + day5 + day6 + day7    
    return weekly_distance

def calculate_activity_score(avg_daily_distance):
   
    score = math.sqrt(avg_daily_distance) * 10 / 2    
    return score

def main():
    
    height_cm = float(input("Enter your height in cm: "))
    if height_cm <= 0:
        print("Height must be a positive number. Please try again.")
        return
    
    stride_length = estimate_stride_length(height_cm)
    
    print("\nenter your step count for each day of the week:")
    
    steps_day1 = int(input("Day 1 steps: "))
    steps_day2 = int(input("Day 2 steps: "))
    steps_day3 = int(input("Day 3 steps: "))
    steps_day4 = int(input("Day 4 steps: "))
    steps_day5 = int(input("Day 5 steps: "))
    steps_day6 = int(input("Day 6 steps: "))
    steps_day7 = int(input("Day 7 steps: "))
   
    distance_day1 = calculate_daily_distance(steps_day1, stride_length)
    distance_day2 = calculate_daily_distance(steps_day2, stride_length)
    distance_day3 = calculate_daily_distance(steps_day3, stride_length)
    distance_day4 = calculate_daily_distance(steps_day4, stride_length)
    distance_day5 = calculate_daily_distance(steps_day5, stride_length)
    distance_day6 = calculate_daily_distance(steps_day6, stride_length)
    distance_day7 = calculate_daily_distance(steps_day7, stride_length)
    
    weekly_distance = estimate_weekly_distance(
        distance_day1, distance_day2, distance_day3, 
        distance_day4, distance_day5, distance_day6, distance_day7
    )
    
    avg_daily_distance = weekly_distance / 7
    activity_score = calculate_activity_score(avg_daily_distance)
    
    rounded_weekly_distance = round(weekly_distance, 1)
    rounded_activity_score = round(activity_score, 1)
    
    print(f"Total walking distance for the week: {rounded_weekly_distance} km")
    print(f"Average daily walking distance: {round(avg_daily_distance, 1)} km")
    print(f"Your weekly activity score: {rounded_activity_score}")

main()
