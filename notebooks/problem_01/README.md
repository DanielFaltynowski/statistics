# Problem 1: 🎯 Analysis of Age and Sex Structure in the U.S., California, and Tennessee Based on Census Data

## 🔍 Context and Research Question

Media and public discourse often suggest that California is more attractive to younger individuals due to its economic opportunities, lifestyle, and cultural environment, whereas Tennessee appeals more to older adults because of its lower cost of living, tax advantages, and quieter pace of life. For example, articles like ["The Best U.S. States to Live for Each Generation"](https://www.gobankingrates.com/money/lifestyle/best-us-states-to-live-for-each-generation/) reflect this general assumption.

The purpose of this task is to verify whether this perceived generational division is visible in actual demographic data.

## 🧪 Task Description

You are provided with CSV files containing demographic data for three regions: the entire United States, the state of California, and the state of Tennessee. These files include information about the population structure by age and sex, and were downloaded from the official US Census Data website: [https://data.census.gov](https://data.census.gov).

Start by loading each dataset using the `pandas` library. Process the data to extract the age and sex distribution for each region. Once you’ve cleaned and structured the data, visualize the age distribution using `matplotlib`.

Then, your own custom Python library to perform a descriptive statistical analysis of each region. For each dataset, compute core statistical metrics that describe the distribution of ages. This includes measures of central tendency (mean, median, mode), dispersion (range, variance, standard deviation), and distribution shape (skewness, kurtosis).

All of your analysis and visualizations should be clearly structured and reproducible in code. You are encouraged to compare the age profiles between California and Tennessee to explore whether the assumptions about their populations — California being "younger", Tennessee being "older" — are supported by actual data patterns.

Finally, interpret your results and discuss to what extent the demographic data confirms or contradicts the general narrative.
