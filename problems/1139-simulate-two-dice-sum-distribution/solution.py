import numpy as np
def simulate_dice_sum(num_rolls, seed=0):
    theoretical_mass_function_distribution =np.array([1,2,3,4,5,6,5,4,3,2,1]) / 36
    
    rng = np.random.RandomState(seed)

    die1_rolls = rng.randint(1, 7, size= num_rolls)
    die2_rolls = rng.randint(1,7, size= num_rolls)
    sum_of_rolls = die1_rolls + die2_rolls

    counts = np.bincount(sum_of_rolls)[2:]

    empirical_mass_function_distribution = counts / num_rolls

    return(empirical_mass_function_distribution,theoretical_mass_function_distribution)
