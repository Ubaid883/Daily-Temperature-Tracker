import os
def clear():
    os.system('cls' if os.name =='nt' else 'clear')

# Average Temperature
def average_tem(temperature):
   return sum(temperature)/ len(temperature)

# Maximum Temperature
def maximum_temp(temperature):
    return max(temperature)

# Minimum Temperature
def minimum_temp(temperature):
    return min(temperature)

    
def main():
    print("\n 🌡 Temperature Tracker! \n")
    temp = []
    day_01 = float(input("Enter Day 01 Temperature:"))
    day_02 = float(input("Enter Day 02 Temperature:"))
    day_03 = float(input("Enter Day 03 Temperature:"))
    day_04 = float(input("Enter Day 04 Temperature:"))
    day_05 = float(input("Enter Day 05 Temperature:"))
    day_06 = float(input("Enter Day 06 Temperature:"))
    day_07 = float(input("Enter Day 07 Temperature:"))
    
    temp_days = [day_01, day_02, day_03, day_04, day_05, day_06, day_07]
    # Store the vlaues of days temperature into temperature lists
    for values in temp_days:
        temp.append(values)
    
    # Clear Terminal Screeen
    clear()
    
    # Days wise Temperature
    for i , value in enumerate(temp_days, start=1):
        print(f'{i}Days Temperature: {value}*C')
            
    # Average Temperature!
    Avg_temp = average_tem(temp)
    print(f'Average Temperature: {Avg_temp:.2f}°C')
    
     # Maximum Temperature!
    Mxi_temp = maximum_temp(temp)
    print(f'Maximum Temperature: {Mxi_temp:.2f}°C')
    
    # Minimum Temperature!
    Min_temp = minimum_temp(temp)
    print(f'Minimum Temperature: {Min_temp:.2f}°C')
    

if __name__ == "__main__":
    main()
    
    