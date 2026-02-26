import schedule
import time
from tabulate import tabulate

data = [
    ["David", 88],
    ["Kim", 99],
    ["Mike", 91],
    ["Mary", 85]
]

print(tabulate(data, headers=["Name", "Marks"], tablefmt="grid"))
print(tabulate(data, headers=["Name", "Marks"], tablefmt="psql"))













# def reminder():
#     print("Drink water..!")

# schedule.every(1).hour.do(reminder)

# while True:
#     schedule.run_pending()
    # time.sleep(1)





# def job():
#     print("Task running")
    
# schedule.every(5).seconds.do(job)   

# schedule.every().hour().do(job)  #once after an hour
# schedule.every().day().do(job)   #once a day
# schedule.every().monday().do(job) #every monday
# schedule.every().day.at("10:00").do(job)  #everyday at 10 AM

# while True:
#     schedule.run_pending()
#     time.sleep(1)
    
    