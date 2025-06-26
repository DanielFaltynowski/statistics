# Descriptive Statistics


### Moments

- `moment(data: list[float], order: int = 1, delta_degrees_of_freedom: int = 0) -> float`

    - Symbol $x$ means `data`
    - $k = $ `order`
    - $\Delta\text{df} = $ `delta_degrees_of_freedom`
    - $n = $ `len(data)`

$$\text{moment}(x, k, \text{df}) = \frac{1}{n - \Delta\text{df}}\displaystyle\sum_{i=0}^{n-1}{x_i^k}$$

- `centralised_moment(data: list[float], order: int = 1, delta_degrees_of_freedom: int = 0) -> float`

    - $x = $ `data`
    - $k = $ `order`
    - $\Delta\text{df} = $ `delta_degrees_of_freedom`
    - $n = $ `len(data)`
    - $\mu = $ `mean(data)`

$$\text{centralMoment}(x, k, \text{df}) = \frac{1}{n - \Delta\text{df}}\displaystyle\sum_{i=0}^{n-1}{(x_i - \mu)^k}$$

- `standardised_moment(data: list[float], order: int = 1, delta_degrees_of_freedom: int = 0) -> float`

    - $x = $ `data`
    - $k = $ `order`
    - $\Delta\text{df} = $ `delta_degrees_of_freedom`
    - $n = $ `len(data)`
    - $\mu = $ `mean(data)`
    - $\sigma = $ `standard_deviation(data)`

$$\text{standardisedMoment}(x, k, \text{df}) = \frac{1}{(n - \Delta\text{df}) \times \sigma^{k}}\displaystyle\sum_{i=0}^{n-1}{(x_i - \mu)^k}$$

