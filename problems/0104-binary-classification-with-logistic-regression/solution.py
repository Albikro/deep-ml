import numpy as np
import math

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
    """
    Implements binary classification prediction using Logistic Regression.

    Args:
        X: Input feature matrix (shape: N x D)
        weights: Model weights (shape: D)
        bias: Model bias
    

    Returns:
        Binary predictions (0 or 1)
    """

    raw_outputs = [X[i] @ weights + bias for i in range(len(X))]
    sigmoid_outputs = [1 / (1 + math.exp(-1 * raw_output)) for raw_output in raw_outputs]
    return np.array([1 if sigmoid_output>= 0.5 else 0 for sigmoid_output in sigmoid_outputs])