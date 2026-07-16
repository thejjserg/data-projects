# Add your Code below
from datetime import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

# Gather today's Datetime
today = dt.now()

# Example Birthday
birthday = dt(1998, 4, 20, 4, 2, 0)

# Base Cost for Traveling
base_cost = Decimal('1000.00') # Every Trip starts at $1000.00
cost_multiplier = Decimal('2.50') # Every Year traveled multiplies costs by $2.50

# Generate a Random Year
random_year = randint(1, 9999) # Generate a Random Year

# List of Destinations
locations = ["The Moon", "Jupiter", "My Room", "School"] # Locations that we can Travel to
final_destination = choice(locations)

# Costs
years = abs(today.year - random_year) # Compute the number of years we travel
final_cost = base_cost + years * cost_multiplier # Compute the costs of the travel


# Using Custom Module
# Find where we're going
final_message = custom_module.generate_time_travel_message(year = random_year, destination = final_destination, cost = final_cost)

# Print the Specs of the Travel
print("Today is " + dt.strftime(today, '%b %d, %Y'))

print(final_message)