import math
import sys

def run_program():
	user_input = input("Enter 'c' to continue, or 'q' to quit: ")
	print()

	if (user_input == "q"):
		print("Exiting...")
		try:
			sys.exit(1)
		except SystemExit as e:
			sys.exit(e)
	
	if (user_input == "c"):
		roll_diameter = float(input("Enter roll diameter in inches: "))
		core_diameter = float(input("Enter core diameter in inches: "))
		material_thickness = float(input("Enter material thickness in inches: "))
		roll_width = float(input("Enter roll width in inches: "))
		print()
	
		roll_radius = (roll_diameter / 2)
		core_radius = (core_diameter / 2)
	
		roll_radius_squared = (roll_radius * roll_radius)
		core_radius_squared = (core_radius * core_radius)
	
		diff_in_radius = (roll_radius_squared - core_radius_squared)
	
		pi_times_diff_in_radius = (math.pi * diff_in_radius)
	
		total = (pi_times_diff_in_radius / material_thickness)
	
		linear_feet = (total / 12)
		area = (linear_feet * (roll_width / 12))
	
		print("Length of roll in linear feet: ")
		print(format(linear_feet, ".2f"))
		print()
	
		print("Area of roll in square feet: ")
		print(format(area, ".2f"))
		print()
	
while (True):
	run_program()
	