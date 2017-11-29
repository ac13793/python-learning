# def minute_to_seconds(minutes):
#     hours = minutes/60
#     return hours

# print(minute_to_seconds(70))

# Function Default arguments 
# def minute_to_seconds(seconds, minutes = 30):
#     hours = minutes/60
#     return hours

# print(minute_to_seconds(70))

def minute_to_seconds(seconds, minutes = 30):
    hours = minutes/60
    return hours

print(minute_to_seconds(70, 60))