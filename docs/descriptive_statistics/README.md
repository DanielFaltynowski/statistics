# 📊 Statistical Functions Documentation

## Table of Contents

- [Moments](#moments)
  - [`moment`](#moment)
  - [`centralised_moment`](#centralised_moment)
  - [`standardised_moment`](#standardised_moment)
- [Measures of Central Tendency](#measures-of-central-tendency)
  - [`mean`](#mean)
  - [`median`](#median)
  - [`mode`](#mode)
  - [`weighted_mean`](#weighted_mean)
  - [`weighted_median`](#weighted_median)
  - [`weighted_mode`](#weighted_mode)
- [Measures of Dispersion](#measures-of-dispersion)
  - [`variance`](#variance)
  - [`standard_deviation`](#standard_deviation)
  - [`data_range`](#data_range)
  - [`standard_error`](#standard_error)
  - [`weighted_variance`](#weighted_variance)
  - [`weighted_standard_deviation`](#weighted_standard_deviation)
  - [`weighted_standard_error`](#weighted_standard_error)
- [Shape Descriptors](#shape-descriptors)
  - [`skewness`](#skewness)
  - [`kurtosis`](#kurtosis)
  - [`excess_kurtosis`](#excess_kurtosis)
  - [`weighted_skewness`](#weighted_skewness)
  - [`weighted_kurtosis`](#weighted_kurtosis)
  - [`weighted_excess_kurtosis`](#weighted_excess_kurtosis)

---

## Moments

### `moment(data, order=1, delta_degrees_of_freedom=0)`

Computes the raw moment of a specified order.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `order` (`int`): The order of the moment to compute. Defaults to `1`.
  - `delta_degrees_of_freedom` (`int`): Value to subtract from the data length when calculating degrees of freedom. Defaults to `0`.
- **Returns**: `float`

---

### `centralised_moment(data, order=1, delta_degrees_of_freedom=0)`

Computes the centralised moment (i.e., moment about the mean).

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `order` (`int`): The order of the centralised moment. Defaults to `1`.
  - `delta_degrees_of_freedom` (`int`): Value to subtract from the data length when calculating degrees of freedom. Defaults to `0`.
- **Returns**: `float`

---

### `standardised_moment(data, order=1, delta_degrees_of_freedom=0)`

Computes the standardised moment (i.e., moment divided by standard deviation to the given power).

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `order` (`int`): The order of the standardised moment. Defaults to `1`.
  - `delta_degrees_of_freedom` (`int`): Value to subtract from the data length when calculating degrees of freedom. Defaults to `0`.
- **Returns**: `float`

---

## Measures of Central Tendency

### `mean(data)`

Computes the arithmetic mean of the input data.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
- **Returns**: `float`

---

### `median(data)`

Computes the median (middle value) of the input data.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
- **Returns**: `float`

---

### `mode(data)`

Computes the most frequent value(s) in the dataset.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
- **Returns**: `float` or `list[float]`

---

### `weighted_mean(data, weights)`

Computes the weighted arithmetic mean.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `weights` (`list[int]`): A list of non-negative weights, same length as `data`.
- **Returns**: `float`

---

### `weighted_median(data, weights)`

Computes the weighted median using cumulative weight ranking.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `weights` (`list[float]`): A list of non-negative weights, same length as `data`.
- **Returns**: `float`

---

### `weighted_mode(data, weights)`

Returns the value(s) with the highest weight.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `weights` (`list[int]`): A list of non-negative weights, same length as `data`.
- **Returns**: `float` or `list[float]`

---

## Measures of Dispersion

### `variance(data, from_sample=True)`

Computes the variance of the dataset.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `from_sample` (`bool`): If `True`, uses Bessel's correction (`n-1`). If `False`, uses population denominator (`n`). Default is `True`.
- **Returns**: `float`

---

### `standard_deviation(data, from_sample=True)`

Computes the standard deviation as the square root of variance.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `from_sample` (`bool`): Whether to apply Bessel's correction. Default is `True`.
- **Returns**: `float`

---

### `data_range(data)`

Computes the minimum and maximum values of the dataset.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
- **Returns**: `tuple[float, float]`

---

### `standard_error(data)`

Computes the standard error of the mean (SEM).

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
- **Returns**: `float`

---

### `weighted_variance(data, weights, from_sample=True)`

Computes the variance for weighted data.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `weights` (`list[int]`): A list of non-negative weights, same length as `data`.
  - `from_sample` (`bool`): Whether to apply correction for sample. Default is `True`.
- **Returns**: `float`

---

### `weighted_standard_deviation(data, weights, from_sample=True)`

Computes the weighted standard deviation.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `weights` (`list[int]`): A list of non-negative weights.
  - `from_sample` (`bool`): Whether to apply sample correction. Default is `True`.
- **Returns**: `float`

---

### `weighted_standard_error(data, weights)`

Computes the weighted standard error of the mean.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `weights` (`list[int]`): A list of non-negative weights.
- **Returns**: `float`

---

## Shape Descriptors

### `skewness(data, from_sample=True)`

Computes the skewness of the dataset.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `from_sample` (`bool`): Whether to apply correction for sample. Default is `True`.
- **Returns**: `float`

---

### `kurtosis(data, from_sample=True)`

Computes the kurtosis of the dataset.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `from_sample` (`bool`): Whether to apply correction for sample. Default is `True`.
- **Returns**: `float`

---

### `excess_kurtosis(data, from_sample=True)`

Computes excess kurtosis (kurtosis - 3).

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `from_sample` (`bool`): Whether to apply correction for sample. Default is `True`.
- **Returns**: `float`

---

### `weighted_skewness(data, weights, from_sample=True)`

Computes skewness for weighted data.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `weights` (`list[int]`): A list of non-negative weights.
  - `from_sample` (`bool`): Whether to apply sample correction. Default is `True`.
- **Returns**: `float`

---

### `weighted_kurtosis(data, weights, from_sample=True)`

Computes kurtosis for weighted data.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `weights` (`list[int]`): A list of non-negative weights.
  - `from_sample` (`bool`): Whether to apply sample correction. Default is `True`.
- **Returns**: `float`

---

### `weighted_excess_kurtosis(data, weights, from_sample=True)`

Computes excess kurtosis for weighted data.

- **Parameters**:
  - `data` (`list[float]`): A list of numeric values.
  - `weights` (`list[int]`): A list of non-negative weights.
  - `from_sample` (`bool`): Whether to apply sample correction. Default is `True`.
- **Returns**: `float`

---

## Notes

- All functions perform type validation and return `None` if invalid input is detected.
- Most functions follow statistical standards and apply Bessel's correction when `from_sample=True`.
