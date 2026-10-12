import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	current_x = x
	total_gradient = 1

	for function in reversed(functions):
		match function:
			case 'square':
				total_gradient = total_gradient * 2 * current_x
				current_x = pow(current_x,2)
			case 'sin':
				total_gradient = total_gradient * np.cos(current_x)
				current_x = np.sin(current_x)
			case 'exp':
				total_gradient = total_gradient * np.exp(current_x)
				current_x = np.exp(current_x)
			case 'log':
				total_gradient = total_gradient * (1/current_x)
				current_x = np.log(current_x)
	return total_gradient