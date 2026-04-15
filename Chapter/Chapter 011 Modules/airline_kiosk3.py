def check_in(passenger_name, luggage_quantity):
	print(f"{luggage_quantity} pieces of luggage are checked by {passenger_name}.")

def check_bags(luggage_quantity):
	charge = luggage_quantity * 20
	print(f"${charge} is charged for {luggage_quantity} pieces of luggage.")