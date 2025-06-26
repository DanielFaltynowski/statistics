# Descriptive Statistics


### Moments

- `moment(data: list[float], order: int = 1, delta_degrees_of_freedom: int = 0) -> float`

    - Symbol $x$: `data`
    - Symbol $k$: `order`
    - Symbol $\Delta\text{df}$: `delta_degrees_of_freedom`
    - Symbol $n$: `len(data)`

$$\text{moment}(x, k, \text{df}) = \frac{1}{n - \Delta\text{df}}\displaystyle\sum_{i=0}^{n-1}{x_i^k}$$

- `centralised_moment(data: list[float], order: int = 1, delta_degrees_of_freedom: int = 0) -> float`

    - Symbol $x$: `data`
    - Symbol $k$: `order`
    - Symbol $\Delta\text{df}$: `delta_degrees_of_freedom`
    - Symbol $n$: `len(data)`
    - Symbol $\mu$: `mean(data)`

$$\text{centralMoment}(x, k, \text{df}) = \frac{1}{n - \Delta\text{df}}\displaystyle\sum_{i=0}^{n-1}{(x_i - \mu)^k}$$

- `standardised_moment(data: list[float], order: int = 1, delta_degrees_of_freedom: int = 0) -> float`

    - Symbol $x$: `data`
    - Symbol $k$: `order`
    - Symbol $\Delta\text{df}$: `delta_degrees_of_freedom`
    - Symbol $n$: `len(data)`
    - Symbol $\mu$: `mean(data)`
    - Symbol $\sigma$: `standard_deviation(data)`

$$\text{standardisedMoment}(x, k, \text{df}) = \frac{1}{(n - \Delta\text{df}) \times \sigma^{k}}\displaystyle\sum_{i=0}^{n-1}{(x_i - \mu)^k}$$


### Central Tendency

- `mean(data: list[float]) -> float`

    - Symbol $x$: `data`
    - Symbol $n$: `len(data)`

$$
\text{mean}(x) = \text{populationMean}(x) = \mu = \frac{1}{n} \sum_{i=0}^{n-1}{x_i}
$$
$$
\text{mean}(x) = \text{sampleMean}(x) = \overline{x} = \frac{1}{n} \sum_{i=0}^{n-1}{x_i}
$$

- `median(data: list[float]) -> float`

    - Symbol $x$: `data`
    - Symbol $n$: `len(data)`

$$
\text{median}(x) = 

x.\text{sort}_{\frac{n-1}{2}}\text{ if } n \text{ is odd, else } \displaystyle\frac{x.\text{sort}_{\frac{n-1}{2}} + x.\text{sort}_{\frac{n-1}{2} + 1}}{2}

$$

- `mode(data: list[float]) -> float | list[float] | None`

    - Symbol $x$: `data`
    - Symbol $n$: `len(data)`

$$
\text{mode}(x) = \bigg\{ x_i \bigg| x_i.\text{count} = \max_j (x_j.\text{count}) \bigg\}
$$
