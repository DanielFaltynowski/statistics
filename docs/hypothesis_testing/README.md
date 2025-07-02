# 🧪 Hypothesis Testing & Multiple Testing Correction

## Table of Contents

* [Multiple Testing Correction](#multiple-testing-correction)

  * [`benjamini_hockberg_method`](#benjamini_hockberg_method)
* [T-Statistics & T-Tests](#t-statistics--t-tests)

  * [`one_sample_t_statistic`](#one_sample_t_statistic)
  * [`independent_samples_t_statistics`](#independent_samples_t_statistics)
  * [`dependent_samples_t_statistic`](#dependent_samples_t_statistic)
  * [`one_sample_t_test`](#one_sample_t_test)
  * [`independent_samples_t_test`](#independent_samples_t_test)
  * [`dependent_samples_t_test`](#dependent_samples_t_test)
* [Z-Statistics & Z-Tests](#z-statistics--z-tests)

  * [`one_sample_z_statistic`](#one_sample_z_statistic)
  * [`independent_samples_z_statistics`](#independent_samples_z_statistics)
  * [`dependent_samples_z_statistic`](#dependent_samples_z_statistic)
  * [`one_sample_z_test`](#one_sample_z_test)
  * [`independent_samples_z_test`](#independent_samples_z_test)
  * [`dependent_samples_z_test`](#dependent_samples_z_test)
* [Kolmogorov-Smirnov Test](#kolmogorov-smirnov-test)

  * [`d_statistics`](#d_statistics)
  * [`kolmogorov_function`](#kolmogorov_function)
  * [`kolmogorov_smirnov_test`](#kolmogorov_smirnov_test)

---

## Multiple Testing Correction

### `benjamini_hockberg_method(p_values)`

Adjusts p-values using the Benjamini-Hochberg procedure.

* **Parameters**:

  * `p_values` (`list[float]`): List of p-values to be adjusted. Values must be between 0 and 1.
* **Returns**: `list[float]` - Adjusted p-values.

---

## T-Statistics & T-Tests

### `one_sample_t_statistic(sample, population_mean)`

Computes the t-statistic for a one-sample t-test.

* **Parameters**:

  * `sample` (`list[float]`): The sample data.
  * `population_mean` (`float`): The hypothesised population mean.
* **Returns**: `float`

---

### `independent_samples_t_statistics(sample_one, sample_two)`

Computes the t-statistic for two independent samples.

* **Parameters**:

  * `sample_one` (`list[float]`): First independent sample.
  * `sample_two` (`list[float]`): Second independent sample.
* **Returns**: `float`

---

### `dependent_samples_t_statistic(differences)`

Computes the t-statistic for paired (dependent) samples.

* **Parameters**:

  * `differences` (`list[float]`): Differences between paired observations.
* **Returns**: `float`

---

### `one_sample_t_test(sample, population_mean)`

Performs a one-sample t-test.

* **Parameters**:

  * `sample` (`list[float]`): Sample data.
  * `population_mean` (`float`): Hypothesised population mean.
* **Returns**: `dict` with keys: `t-statistics`, `p-value`, `degrees_of_freedom`

---

### `independent_samples_t_test(sample_one, sample_two)`

Performs a two-sample independent t-test.

* **Parameters**:

  * `sample_one` (`list[float]`): First sample.
  * `sample_two` (`list[float]`): Second sample.
* **Returns**: `dict` with keys: `t-statistics`, `p-value`, `degrees_of_freedom`

---

### `dependent_samples_t_test(differences)`

Performs a paired sample t-test.

* **Parameters**:

  * `differences` (`list[float]`): Differences between paired values.
* **Returns**: `dict` with keys: `t-statistics`, `p-value`, `degrees_of_freedom`

---

## Z-Statistics & Z-Tests

### `one_sample_z_statistic(sample, population_mean, population_standard_deviation=None)`

Computes the z-statistic for a one-sample z-test.

* **Parameters**:

  * `sample` (`list[float]`): The sample data.
  * `population_mean` (`float`): The hypothesised population mean.
  * `population_standard_deviation` (`float`, optional): Population standard deviation. If `None`, falls back to t-statistic.
* **Returns**: `float`

---

### `independent_samples_z_statistics(sample_one, sample_two, population_standard_deviation_one=None, population_standard_deviation_two=None)`

Computes the z-statistic for two independent samples.

* **Parameters**:

  * `sample_one` (`list[float]`): First sample.
  * `sample_two` (`list[float]`): Second sample.
  * `population_standard_deviation_one` (`float`, optional): Std. dev. of first population.
  * `population_standard_deviation_two` (`float`, optional): Std. dev. of second population.
* **Returns**: `float`

---

### `dependent_samples_z_statistic(differences, differences_standard_deviation=None)`

Computes the z-statistic for paired samples.

* **Parameters**:

  * `differences` (`list[float]`): Differences between paired observations.
  * `differences_standard_deviation` (`float`, optional): If `None`, uses sample standard deviation.
* **Returns**: `float`

---

### `one_sample_z_test(sample, population_mean, population_standard_deviation=None)`

Performs a one-sample z-test.

* **Parameters**:

  * `sample` (`list[float]`): Sample data.
  * `population_mean` (`float`): Hypothesised population mean.
  * `population_standard_deviation` (`float`, optional): If `None`, uses t-distribution.
* **Returns**: `dict` with keys: `z-statistics`, `p-value`, `degrees_of_freedom`

---

### `independent_samples_z_test(sample_one, sample_two, population_standard_deviation_one=None, population_standard_deviation_two=None)`

Performs an independent two-sample z-test.

* **Parameters**:

  * `sample_one` (`list[float]`): First sample.
  * `sample_two` (`list[float]`): Second sample.
  * `population_standard_deviation_one` (`float`, optional): Std. dev. of first population.
  * `population_standard_deviation_two` (`float`, optional): Std. dev. of second population.
* **Returns**: `dict` with keys: `z-statistics`, `p-value`, `degrees_of_freedom`

---

### `dependent_samples_z_test(differences, differences_standard_deviation=None)`

Performs a paired z-test.

* **Parameters**:

  * `differences` (`list[float]`): Paired differences.
  * `differences_standard_deviation` (`float`, optional): If `None`, uses t-distribution.
* **Returns**: `dict` with keys: `z-statistics`, `p-value`, `degrees_of_freedom`

---

## Kolmogorov-Smirnov Test

### `d_statistics(sample, distribution)`

Calculates maximum distance between empirical and theoretical cumulative distributions.

* **Parameters**:

  * `sample` (`list[float]`): Empirical data.
  * `distribution` (`function`): Theoretical cumulative distribution function.
* **Returns**: `float`

---

### `kolmogorov_function(parameter_lambda, end=100)`

Computes the Kolmogorov distribution function.

* **Parameters**:

  * `parameter_lambda` (`float`): The scaling factor.
  * `end` (`int`): The number of terms in the series approximation. Default is 100.
* **Returns**: `float`

---

### `kolmogorov_smirnov_test(empirical_distribution, theoritical_distribution)`

Performs the Kolmogorov-Smirnov test for goodness of fit.

* **Parameters**:

  * `empirical_distribution` (`list[float]`): Sample data.
  * `theoritical_distribution` (`list[float]`): Theoretical CDF.
* **Returns**: `dict` with keys: `d-statistics`, `p-value`
