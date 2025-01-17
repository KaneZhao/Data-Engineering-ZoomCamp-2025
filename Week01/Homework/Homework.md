###

## Q1

Run docker with the python:3.12.8 image in an interactive mode, use the entrypoint bash.

```bash
docker run -it --entrypoint bash python:3.12.8
```

Check pip version by

```bash
pip --version
```

pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)

## Q2

Hostname: db (service name). Port: 5432

## Q3

```bash
SELECT
SUM(CASE
        WHEN trip_distance <= 1 THEN 1
        ELSE 0
END) AS trips_cnt_1,
SUM(CASE
        WHEN trip_distance > 1 AND trip_distance <= 3 THEN 1
        ELSE 0
END) AS trips_cnt_2,
SUM(CASE
        WHEN trip_distance > 3 AND trip_distance <= 7 THEN 1
        ELSE 0
END) AS trips_cnt_3,
SUM(CASE
        WHEN trip_distance > 7 AND trip_distance <= 10 THEN 1
        ELSE 0
END) AS trips_cnt_4,
SUM(CASE
        WHEN trip_distance > 10 THEN 1
        ELSE 0
END) AS trips_cnt_5
FROM public.green_tripdata
WHERE CAST(lpep_pickup_datetime AS DATE) >= '2019-10-01'
AND CAST(lpep_dropoff_datetime AS DATE) < '2019-11-01';

```

results:

| trips_cnt_1 | trips_cnt_2 | trips_cnt_3 | trips_cnt_3 | trips_cnt_3 |
| :---------: | :---------: | :---------: | :---------: | :---------: |
|   104802    |   198924    |   109603    |    27678    |    35189    |

## Q4

```bash
SELECT CAST(lpep_pickup_datetime AS DATE) as pick_date,
trip_distance
FROM public.green_tripdata
WHERE trip_distance =
(
SELECT max(trip_distance)
FROM public.green_tripdata
)
limit 10
;
```

results:

| pick_date  | trip_distance |
| :--------: | :-----------: |
| 2019-10-31 |    515.89     |

## Q5

```bash
SELECT b."Zone" as pickup_location
FROM public.green_tripdata a
LEFT JOIN public.taxi_zones b
ON a."PULocationID" = b."LocationID"
WHERE CAST(lpep_pickup_datetime AS DATE) = '2019-10-18'
GROUP BY b."Zone"
HAVING SUM(a.total_amount) > 13000
ORDER BY SUM(a.total_amount) DESC
LIMIT 3
;
```

|   pickup_location   |
| :-----------------: |
|  East Harlem North  |
|  East Harlem South  |
| Morningside Heights |

## Q6

```bash
SELECT a.tip_amount, c."Zone"
FROM public.green_tripdata a
LEFT JOIN public.taxi_zones b
ON a."PULocationID" = b."LocationID"
LEFT JOIN public.taxi_zones c
ON a."DOLocationID" = c."LocationID"
WHERE DATE_TRUNC('month',a.lpep_pickup_datetime) = '2019-10-01 00:00:00'
AND b."Zone" = 'East Harlem North'
ORDER BY tip_amount DESC
LIMIT 1
;
```

| tip_amount |    Zone     |
| :--------: | :---------: |
|    87.3    | JFK Airport |

## Q7

terraform init, terraform apply -auto-approve, terraform destroy
