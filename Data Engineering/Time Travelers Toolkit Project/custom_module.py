def generate_time_travel_message(year, destination, cost):
    time = "You are traveling to Year " + str(year) + "."
    location = "You are traveling to " + str(destination) + "."
    money = "The cost is $" + str(cost) + "."

    message = time + " " + location + " " + money

    return message