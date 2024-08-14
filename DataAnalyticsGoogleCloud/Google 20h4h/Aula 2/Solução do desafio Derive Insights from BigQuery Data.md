# Derive Insights from BigQuery Data: laboratório com desafio

## IMPORTANTE - Lembrar de trocar os valores que estão entre ** pelos valores do lab

**Tarefa 1: total de casos confirmados**

```jsx
SELECT SUM(cumulative_confirmed) AS total_cases_worldwide
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE date = **'2020-05-25'**
```

 **Tarefa 2: áreas mais afetadas**

```jsx
WITH deaths_by_states as (
  SELECT subregion1_name as state, sum(cumulative_deceased) as death_count
  FROM `bigquery-public-data.covid19_open_data.covid19_open_data` 
  WHERE country_name="United States of America" and date=**'2020-05-10'** and subregion1_name is NOT NULL
  GROUP BY subregion1_name
)

SELECT count(*) as count_of_states
FROM deaths_by_states
WHERE death_count > **200**
```

**Tarefa 3: identificação das áreas de risco** 

```jsx
SELECT subregion1_name as state, sum(cumulative_confirmed) as total_confirmed_cases 
FROM `bigquery-public-data.covid19_open_data.covid19_open_data` 
WHERE country_name="United States of America" and date='2020-05-10' and subregion1_name is NOT NULL
GROUP BY subregion1_name
HAVING total_confirmed_cases > **3000**
ORDER BY total_confirmed_cases DESC
```

**Tarefa 4: taxa de letalidade** 

```jsx
SELECT 
  sum(cumulative_confirmed) as total_confirmed_cases, 
  sum(cumulative_deceased) as total_deaths, 
  (sum(cumulative_deceased)/sum(cumulative_confirmed))*100 as case_fatality_ratio
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE country_name="Italy" 
  AND date BETWEEN "**2020-05-01**" AND "**2020-05-31**"

```

**Tarefa 5: identificação do dia específico** 

```jsx
SELECT
  date
FROM
  `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE
  country_name = 'Italy'
  AND cumulative_deceased > **16000**
ORDER BY
  date
ASC
LIMIT
  1
```

**Tarefa 6: busca por dias sem aumento nos casos**

```jsx
WITH india_cases_by_date AS (
  SELECT
    date,
    SUM(cumulative_confirmed) AS cases
  FROM
    `bigquery-public-data.covid19_open_data.covid19_open_data`
  WHERE
    country_name="India"
    AND date between '**2020-02-25**' and '**2020-03-13**'
  GROUP BY
    date
  ORDER BY
    date ASC
),

india_previous_day_comparison AS (
  SELECT
    date,
    cases,
    LAG(cases) OVER(ORDER BY date) AS previous_day,
    cases - LAG(cases) OVER(ORDER BY date) AS net_new_cases
  FROM
    india_cases_by_date
),

days_without_increase AS (
  SELECT
    date
  FROM
    india_previous_day_comparison
  WHERE
    net_new_cases = 0
)

SELECT
  COUNT(*) AS number_of_days
FROM
  days_without_increase;

```

**Tarefa 7: taxa de duplicação**

```jsx
WITH us_cases_by_date AS (
  SELECT
    date,
    SUM(cumulative_confirmed) AS cases
  FROM
    `bigquery-public-data.covid19_open_data.covid19_open_data`
  WHERE
    country_name="United States of America"
    AND date between '2020-03-22' and '2020-04-20'
  GROUP BY
    date
  ORDER BY
    date ASC 
 )
, us_previous_day_comparison AS 
(SELECT
  date,
  cases,
  LAG(cases) OVER(ORDER BY date) AS previous_day,
  cases - LAG(cases) OVER(ORDER BY date) AS net_new_cases,
  (cases - LAG(cases) OVER(ORDER BY date))*100/LAG(cases) OVER(ORDER BY date) AS percentage_increase
FROM us_cases_by_date
)
SELECT Date, cases as Confirmed_Cases_On_Day, previous_day as Confirmed_Cases_Previous_Day, percentage_increase as Percentage_Increase_In_Cases
FROM us_previous_day_comparison
WHERE percentage_increase > **10**
```

**Tarefa 8: taxa de recuperação** 

```jsx
WITH cases_by_country AS (
  SELECT
    country_name AS country,
    sum(cumulative_confirmed) AS cases,
    sum(cumulative_recovered) AS recovered_cases
  FROM
    bigquery-public-data.covid19_open_data.covid19_open_data
  WHERE
    date = '2020-05-10'
  GROUP BY
    country_name
 )
, recovered_rate AS 
(SELECT
  country, cases, recovered_cases,
  (recovered_cases * 100)/cases AS recovery_rate
FROM cases_by_country
)
SELECT country, cases AS confirmed_cases, recovered_cases, recovery_rate
FROM recovered_rate
WHERE cases > 50000
ORDER BY recovery_rate desc
LIMIT **20**
```

**Tarefa 9: taxa de crescimento diário cumulativo (CDGR, na sigla em inglês)** 

```jsx
WITH france_cases AS (
  SELECT
    date,
    CASE date
      WHEN '2020-01-24' THEN SUM(cumulative_confirmed)
      WHEN '**2020-05-10**' THEN SUM(cumulative_confirmed)
    END AS total_cases
  FROM
    `bigquery-public-data.covid19_open_data.covid19_open_data`
  WHERE
    country_name = "France"
    AND date IN ('2020-01-24', '**2020-05-10**')
  GROUP BY
    date
  ORDER BY
    date
),
summary AS (
  SELECT
    FIRST_VALUE(total_cases) OVER(ORDER BY date) AS first_day_cases,
    LEAD(total_cases) OVER(ORDER BY date) AS last_day_cases,
    DATE_DIFF(LEAD(date) OVER(ORDER BY date), date, DAY) AS days_diff
  FROM
    france_cases
  LIMIT 1
)
SELECT
  first_day_cases,
  last_day_cases,
  days_diff,
  POW((last_day_cases / first_day_cases), (1 / days_diff)) - 1 AS cdgr
FROM
  summary;

```

**Tarefa 10: criação de um relatório do Looker Studio**

```jsx
SELECT
  date, SUM(cumulative_confirmed) AS country_cases,
  SUM(cumulative_deceased) AS country_deaths
FROM
  `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE
  date BETWEEN '**2020-03-15**'
  AND '**2020-04-30**'
  AND country_name ="United States of America"
GROUP BY date
```

![image](https://github.com/user-attachments/assets/835320b1-342c-4d58-92fb-430ff0faffd5)
