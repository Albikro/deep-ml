import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X_ = np.array(X)
    Y = np.array(y)

    theta = np.linalg.inv(np.matmul(X_.T,X_)) @ X_.T @ Y
    return theta