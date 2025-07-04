import src.linear_models as lm
import numpy as np

X = [1, 3, 5, 7, 8]
Y = [8, 5, 6, 3, 2]

print("=== Covariance ===")
print(f"My implementation     : {lm.covariance(X, Y)}")
print(f"NumPy implementation  : {np.cov(X, Y)[0, 1]}")

print("\n=== Correlation ===")
print(f"My implementation     : {lm.correlation(X, Y)}")
print(f"NumPy implementation  : {np.corrcoef(X, Y)[0, 1]}")

print("\n=== Linear Regression Parameters (slope, intercept) ===")
print(f"My implementation     : {lm.linear_regression_params(X, Y)}")
print(f"NumPy implementation  : {tuple(np.polyfit(X, Y, 1))}")

print("\n=== Linear Regression Prediction ===")
print(f"My implementation     : {lm.linear_regression(X, Y)}")
print(f"NumPy implementation  : {np.polyval(np.polyfit(X, Y, 1), X)}")
