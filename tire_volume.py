import math
import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return volume

def main():
    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Get user input
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
    
    # Calculate volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)
    
    # Display result
    print(f"The approximate volume is {volume:.2f} liters")
    
    # Write to file
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")

if __name__ == "__main__":
    main()
