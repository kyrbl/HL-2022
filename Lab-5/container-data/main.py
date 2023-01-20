import json

from pyspark.sql import SparkSession

def trip_driver_rate_map(trip):
    return trip['driver'], (trip['driver_rate'], 1)

def driver_rate_reduce(acc, n):
    return acc[0] + n[0], acc[1] + n[1]

def driver_avg_map(driver):
    avg_rating = round(driver[1][0] / driver[1][1], 2)
    return driver[0], avg_rating

def get_bad_drivers(df, rating):
    bad_drivers = df.filter(lambda trip: trip['driver_rate'] > 0).map(trip_driver_rate_map).reduceByKey(driver_rate_reduce).map(driver_avg_map).filter(lambda a: a[1] < rating).collect()
    return bad_drivers

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option") \
    .getOrCreate()
sc = spark.sparkContext
data_file = "data.txt"
df = sc.textFile(data_file, minPartitions=100).map(lambda x: eval(x))

bad_drivers = get_bad_drivers(df, 3.5)
with open("bad_drivers.json", "w") as f:
   json.dump(bad_drivers, f, indent=4, sort_keys=True)