import math

def sigmoid(z: float) -> float:
	result = round(1 / (1 + math.exp(-1 * z)),4)
	return result