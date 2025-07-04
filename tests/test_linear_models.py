import src.linear_models as lm
import numpy as np
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

X = [1, 3, 5, 7, 8]
Y = [8, 5, 6, 3, 2]

print("=== Covariance ===")
print(f"My implementation     : {lm.covariance(X, Y)}")
print(f"NumPy implementation  : {np.cov(X, Y)[0, 1]}")

print("\n=== Correlation ===")
print(f"My implementation     : {lm.correlation(X, Y)}")
print(f"NumPy implementation  : {np.corrcoef(X, Y)[0, 1]}")
print(f"SciPy implementation  : {linregress(X, Y).rvalue}")

print("\n=== Linear Regression Parameters (slope, intercept) ===")
a, b = lm.linear_regression_params(X, Y)
print(f"My implementation     : slope={a}, intercept={b}")
print(f"NumPy implementation  : slope={np.polyfit(X, Y, 1)[0]}, intercept={np.polyfit(X, Y, 1)[1]}")
lr = linregress(X, Y)
print(f"SciPy implementation  : slope={lr.slope}, intercept={lr.intercept}")

print("\n=== Linear Regression Prediction ===")
Y_pred = lm.linear_regression(X, Y)
print(f"My implementation     : {Y_pred}")
print(f"NumPy implementation  : {np.polyval(np.polyfit(X, Y, 1), X)}")

print("\n=== Residual Sum of Squares (RSS) ===")
rss = lm.residual_sum_of_squares(Y_observed=Y, Y_predicted=Y_pred)
print(f"My implementation     : {rss}")
print(f"Sklearn (MSE * n)     : {mean_squared_error(Y, Y_pred) * len(Y)}")

print("\n=== Mean Squared Error (MSE) ===")
mse = lm.mean_square_error(Y_observed=Y, Y_predicted=Y_pred)
print(f"My implementation     : {mse}")
print(f"Sklearn implementation: {mean_squared_error(Y, Y_pred)}")

print("\n=== R-squared (R²) ===")
r2 = lm.r_square(Y_observed=Y, Y_predicted=Y_pred, from_sample=True)
print(f"My implementation     : {r2}")
print(f"Sklearn implementation: {r2_score(Y, Y_pred)}")
print(f"SciPy implementation  : {lr.rvalue**2}")
