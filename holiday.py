#Flight options
print("Please choose from the following flight options: ")
print("1 Madrid")
print("2 New York")
print("3 London")
print("4 Tokyo")

#User inputs
city_flight = input("Please confirm your choice (1, 2, 3 or 4):  ")

num_nights = int(input("Please confirm the number of nights that you'll be staying at a hotel: "))

rental_days = int(input("Please confirm the number of days that you'll be hiring a car for: "))

#first function is hotel cost and takes number of nights as an argument
def hotel_cost(numbers_of_nights):
    hotel_price_per_night = 150
    return numbers_of_nights * hotel_price_per_night
    
print(f"Your hotel cost is: £{hotel_cost(num_nights)}")

#second function is plane cost and takes city flight as an argument
def  plane_cost(city_flight):
    if city_flight == "1":
        return(600)
    elif city_flight == "2":
        return(1800)
    elif city_flight == "3":
        return (1100)
    elif city_flight == "4":
        return (2200)

print(f"Your flight cost: £{plane_cost(city_flight)}")

#third function is car rental and takes number of rental days as an argument             
def car_rental(number_of_rental_days):
    rental_price_per_day = 30
    return number_of_rental_days * rental_price_per_day

print(f"Your car rental cost is: £{car_rental(rental_days)}")

#final function is holiday cost and it takes three agruments hotel_cost, plane_cost and car_rental
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return (hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days))
    
print(f"Your total holiday cost is: £{holiday_cost(hotel_cost, plane_cost, car_rental)}")