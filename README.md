## zeppelin
```python
%pyspark
df1 = spark.read.csv('hdfs://localhost:9000/nielsen/tv1', inferSchema=True)
df2 = spark.read.csv('hdfs://localhost:9000/nielsen/tv2', inferSchema=True)
df3 = spark.read.csv('hdfs://localhost:9000/nielsen/tv3', inferSchema=True)
```