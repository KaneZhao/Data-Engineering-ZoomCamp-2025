import duckdb

# Connect to your DLT DuckDB database
conn = duckdb.connect("./ny_taxi_pipeline.duckdb")

# Run queries
res = conn.execute("""
    SELECT AVG(EXTRACT(epoch FROM (trip_dropoff_date_time - trip_pickup_date_time)) / 60.0) 
    FROM ny_taxi_data.taxi_rides;
""").fetchone()

# Print the result
print(f"Average trip duration (minutes): {res[0]}")
