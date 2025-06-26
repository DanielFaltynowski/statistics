# Descriptive Statistics


### Moments

- `moment(data: list[float], order: int = 1, delta_degrees_of_freedom: int = 0) -> float`

    - Symbol $x$ means `data`
    - Symbol $k$ means `order`
    - Symbol $\Delta\text{df}$ means `delta_degrees_of_freedom`
    - Symbol $n$ means `len(data)`

$$\text{moment}(x, k, \text{df}) = \frac{1}{n - \Delta\text{df}}\displaystyle\sum_{i=0}^{n-1}{x_i^k}$$

- `centralised_moment(data: list[float], order: int = 1, delta_degrees_of_freedom: int = 0) -> float`

    - Symbol $x$ means `data`
    - Symbol $k$ means `order`
    - Symbol $\Delta\text{df}$ means `delta_degrees_of_freedom`
    - Symbol $n$ means `len(data)`
    - Symbol $\mu$ means `mean(data)`

$$\text{centralMoment}(x, k, \text{df}) = \frac{1}{n - \Delta\text{df}}\displaystyle\sum_{i=0}^{n-1}{(x_i - \mu)^k}$$

- `standardised_moment(data: list[float], order: int = 1, delta_degrees_of_freedom: int = 0) -> float`

    - Symbol $x$ means `data`
    - Symbol $k$ means `order`
    - Symbol $\Delta\text{df}$ means `delta_degrees_of_freedom`
    - Symbol $n$ means `len(data)`
    - Symbol $\mu$ means `mean(data)`
    - Symbol $\sigma$ means `standard_deviation(data)`

$$\text{standardisedMoment}(x, k, \text{df}) = \frac{1}{(n - \Delta\text{df}) \times \sigma^{k}}\displaystyle\sum_{i=0}^{n-1}{(x_i - \mu)^k}$$

