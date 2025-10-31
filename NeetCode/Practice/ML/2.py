# https://neetcode.io/problems/linear-regression-forward

# Ok, not implementing linear regression, just finding it's forward pass

# Complete

import numpy as np
from numpy.typing import NDArray

class Solution:
    
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # weights is a 3x1 NumPy array
        # HINT: np.matmul() will be useful

        return np.round(np.matmul(X, weights), 5)


    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:

        return np.round(np.mean(np.square(model_prediction - ground_truth)), 5)
