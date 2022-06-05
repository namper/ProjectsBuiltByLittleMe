def hotel_cost(nights):
	return 140*nights

def plane_ride_cost(city):
    city=input("Enter The Location: ")
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475
    return 140
def rental_car_cost(days):  
    cost=40*days
    if days >=7:
        cost-=50
        return cost
    elif days >=3:
        cost-=20
        return cost
    else:
        return cost
def trip_cost(city,days,spendingmoney):
    return plane_ride_cost(city) + hotel_cost(days) + rental_car_cost(days)+spendingmoney
print(trip_cost(None,5,600))

