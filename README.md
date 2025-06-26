# Statistics 📊  
A collection of statistical functions and tools implemented in Python. This project is part of my personal journey to better understand mathematical statistics and data analysis from the ground up.

## About the Project  
This repository contains custom implementations of essential statistical concepts, such as point estimators, hypothesis tests, probability distributions, and numerical integration methods (e.g., Simpson's Rule). The main goal is to internalize the logic behind statistical procedures rather than rely solely on black-box functions from external libraries like `scipy` or `statsmodels`.

The project aims to:  
- Deepen my understanding of mathematical statistics through hands-on coding.  
- Build a small, educational library of core statistical tools.  
- Experiment with data (e.g., sports data from FIFA) using hypothesis testing without relying on linear regression or high-level ML libraries.

## Project Structure  
The project is organized into several thematic modules, including:

- `descriptive_statistics.py` – basic statistics: mean, variance, standard deviation  
- `distributions.py` – probability distributions and their cumulative distribution functions  
- `hypothesis_testing.py` – statistical tests (e.g., t-test, p-value calculation)  
- `univariate_calculus.py` – utility functions like numerical integration and gamma function  
- `benjamini_hochberg.py` – implementation of multiple testing correction  

## Requirements  
To use the library, you need:  
- Python 3.12+  
- Libraries listed in `requirements.txt`

### Environment setup:  
```bash
git clone https://github.com/DanielFaltynowski/statistics.git  
cd statistics  
pip install -r requirements.txt  
