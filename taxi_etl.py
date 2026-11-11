import pandas as pd

df = pd.read_parquet("yellow_tripdata_2024-01.parquet")
df["duration"] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
df["duration"] = df.duration.dt.total_seconds() / 60

df = df[(df.duration >= 1) & (df.duration <= 60) & (df.passenger_count > 0)]
df = df[(df.tpep_pickup_datetime >= "2024-01-01") & (df.tpep_pickup_datetime < "2024-02-01")]


print(df.shape)
print(df.head())
print(df.info())
df["pickup_date"] = df.tpep_pickup_datetime.dt.date

daily = df.groupby("pickup_date").agg(
    trips=("VendorID", "size"),
    avg_fare=("fare_amount", "mean"),
    avg_duration=("duration", "mean"),
    total_amount=("total_amount", "sum"),
)

print(daily.head(10))
daily.to_parquet("taxi_daily_summary.parquet")

print("Wrote taxi_daily_summary.parquet")

