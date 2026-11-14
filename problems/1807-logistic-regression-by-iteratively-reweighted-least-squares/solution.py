import numpy as np

def irls_logreg(X, y, n_iter, lam=0.0):
    feature_num = len(X[0])
    weights = np.array([0 for i in range(feature_num)])
    
    history = []

    for step in range(n_iter):
        mu = 1/(1+np.exp(-1 * (X @ weights)))
        s_n = mu * (1 - mu)
        S = np.diag(s_n)
        z = (X @ weights) + (y - mu) / s_n

        I = np.eye(feature_num)
        I[0,0] = 0.0 
        weights = np.linalg.solve(X.T @ S @ X + 2*lam* I,X.T @ S @ z)
        mu = 1/(1+np.exp(-1 * (X @ weights)))

        loss_function = -1 * np.sum(y * np.log(mu) + (1 - y) * np.log(1 - mu))
        loss_function += lam * np.sum(weights[1:] ** 2)
  
        history.append(loss_function)
    return (weights, history)
    
