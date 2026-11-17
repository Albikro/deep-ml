import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def fit_robust_logreg(X, y, n_iter, lr, rho0=-2.0):


    feature_num = len(X[0])
    sample_num = len(X)
    rho = rho0
    weights = np.zeros(feature_num)
    history = []
    for i in range(n_iter):
        s = sigmoid(X @ weights) 
        pi = sigmoid(rho)

        q = np.where(y==1,s,1-s)
        probability = pi * 0.5 + (1 - pi) * q
        mean_log_likelihood = np.mean(np.log(probability))
        history.append(mean_log_likelihood)
        weight_gradient = X.T @ ((2 * y - 1) * s * (1 - s) * (1 - pi) / probability) / sample_num
        rho_gradient = np.mean((0.5 - q) * pi * (1- pi) * (1/probability))

        weights += lr * weight_gradient
        rho += lr * rho_gradient

        pi = sigmoid(rho)

    return (weights, pi, history)
