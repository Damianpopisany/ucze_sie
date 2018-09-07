import math

signal_power = 50
noise_power = 10
#print(math)
ratio = (signal_power/noise_power)
print(ratio)

decibels = 10 * math.log10(ratio)
print(decibels)

radians = 0.7
height = math.sin(radians)
print(height)
print(height*radians*radians+4*noise_power)