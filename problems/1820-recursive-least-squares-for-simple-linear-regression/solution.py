import numpy as np

def online_simple_regression(xs, ys):
    count = 0
    mean_x = 0
    mean_y = 0
    S_xx = 0
    variance_x = 0
    S_xy = 0
    covariance_of_data = 0
    results = []

    for i in range(len(xs)):
        count += 1
        diffx_old = xs[i] - mean_x
        diffy_old = ys[i] - mean_y
        mean_x += diffx_old/count
        mean_y += diffy_old/count
        diffx_new = xs[i] - mean_x
        diffy_new = ys[i] - mean_y
        S_xx += diffx_old * diffx_new
        variance_x = S_xx / count
        S_xy += diffx_old * diffy_new
        covariance_of_data = S_xy / count
        if variance_x == 0:
            w1 = 0
        else:
            w1 = covariance_of_data / variance_x
        w0 = mean_y - w1 * mean_x
    
        results.append((w0,w1))
    return np.array(results)

    # return (N, 2) array of (w0, w1) after each point
    pass
