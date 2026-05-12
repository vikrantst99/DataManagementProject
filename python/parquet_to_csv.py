import duckdb
files = ["C:/Users/Vikrant Singh Thakur/Downloads/data-2026-01.parquet", "C:/Users/Vikrant Singh Thakur/Downloads/data-2026-02.parquet"]
csvs = ["C:/Users/Vikrant Singh Thakur/Downloads/sample-2026-01.csv", "C:/Users/Vikrant Singh Thakur/Downloads/sample-2026-02.csv"]
for i, j in zip(files, csvs):
    duckdb.sql(f"COPY (SELECT * FROM read_parquet('{i}') LIMIT 50000) TO '{j}' (HEADER, DELIMITER ',');")