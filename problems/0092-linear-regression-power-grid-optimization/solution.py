import math

PI = 3.14159

def power_grid_forecast(consumption_data):
	# 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
	defluctated_data = [consumption_data[i] - 10 * math.sin(2* PI * i / 10) for i in range(10)]
	# 2) Perform linear regression on the detrended data.
	y = defluctated_data
	sample_size = len(y)
	x = [i + 1 for i in range(10)]
	dummy_x = [1 for i in range(10)]
	weights = [0,0]
	lr = 0.01
	epoch = 10000
	for yarragimin_basi in range(epoch):
		gradients = []
		for i in range(len(weights)):
			loss = 0
			for j in range(sample_size):
				features = [dummy_x[j],x[j]]
				error = sum([weights[k] * features[k] for k in range(len(weights))]) - y[j]
				loss += error * features[i]	
			gradients.append(loss)
		for i in range(len(weights)):
			weights[i] -= lr * (1 / sample_size) * gradients[i]

	# 3) Predict day 15's base consumption.
	day_15 = weights[0] * 1 + weights[1] * 15 
	# 4) Add the day 15 fluctuation back.
	day_15 += 10 * math.sin(2* PI * 15 / 10)
	# 5) Round, then add a 5% safety margin (rounded up).
	# 6) Return the final integer.
	return math.ceil(day_15 * 1.05)
