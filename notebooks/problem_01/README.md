# Problem 1: 🎯 Analysis of Age and Sex Structure in the U.S., California, and Tennessee Based on Census Data

## 🔍 Research Question:
It is often claimed that California is more attractive to young people, while Tennessee is better suited for older adults. Do these general statements reflect actual demographic differences?

The goal of this task is to investigate whether California has a higher proportion of young people and whether Tennessee has a higher proportion of older residents compared to the overall United States.

## 🧪 Task Scope:

1. **Fetch demographic data** from the U.S. Census Bureau API for three regions:
   - **USA**: [https://api.census.gov/data/2023/acs/acs1/subject?get=group(S0101)&ucgid=0100000US](https://api.census.gov/data/2023/acs/acs1/subject?get=group(S0101)&ucgid=0100000US)
   - **California**: [https://api.census.gov/data/2023/acs/acs1/subject?get=group(S0101)&ucgid=0400000US06](https://api.census.gov/data/2023/acs/acs1/subject?get=group(S0101)&ucgid=0400000US06)
   - **Tennessee**: [https://api.census.gov/data/2023/acs/acs1/subject?get=group(S0101)&ucgid=0400000US47](https://api.census.gov/data/2023/acs/acs1/subject?get=group(S0101)&ucgid=0400000US47)

2. **Extract age and sex distribution data** from the API response.

3. **Create age histograms** for each region (USA, California, Tennessee).

4. **Calculate and describe the following statistical metrics** for each region:
   - **Dispersion:**
     - Range
     - Variance
     - Standard Deviation
   - **Central Tendency:**
     - Median
     - Mode
     - Mean
   - **Distribution Shape:**
     - Skewness
     - Kurtosis

5. **Visualize the computed metrics**, using appropriate plots such as:
   - Bar charts
   - Boxplots
   - Density plots

6. **Interpret the results**:
   - Do the data support the hypothesis that California is demographically younger than Tennessee?
   - How do the age distributions differ between these three regions?
