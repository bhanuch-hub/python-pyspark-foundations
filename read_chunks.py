import pyarrow.parquet as pq

pf = pq.ParquetFile("yellow_tripdata_2024-01.parquet")

total = 0
for i, batch in enumerate(pf.iter_batches(batch_size=500000)):
    print(f"Chunk {i}: {batch.num_rows} rows")
    total += batch.num_rows

    print ("Total:", total)