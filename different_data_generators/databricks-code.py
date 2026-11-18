
# Step 1: Import libraries
import dbldatagen as dg
from pyspark.sql.types import (
    IntegerType,
    StringType
)
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("SyntheticDataGenerator") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

# Step 2: Define number of records
data_rows = 10000
partitions = 4

# Step 3: Create data generator
data_generator = (
    dg.DataGenerator(
        spark,
        name="employee_synthetic_data",
        rows=data_rows,
        partitions=partitions,
        randomSeedMethod="hash_fieldname",
        randomSeed=42
    )

    # Employee ID
    .withIdOutput()

    # Employee name
    .withColumn(
        "employee_name",
        StringType(),
        template=r"\w \w"
    )

    # Employee age
    .withColumn(
        "age",
        IntegerType(),
        minValue=21,
        maxValue=60
    )

    # Department
    .withColumn(
        "department",
        StringType(),
        values=["IT", "HR", "Finance", "Sales"],
        random=True,
        weights=[5, 2, 2, 1]
    )

    # Salary
    .withColumn(
        "salary",
        IntegerType(),
        minValue=20000,
        maxValue=150000
    )

    # Gender
    .withColumn(
        "gender",
        StringType(),
        values=["Male", "Female"],
        random=True
    )

    # Email
    .withColumn(
        "email",
        StringType(),
        template=r"\w.\w@\w.com"
    )
)

# Step 4: Generate synthetic DataFrame
df = data_generator.build()

# Step 5: Display generated records
df.show(20, truncate=False)

# Step 6: Count records
print("Total records:", df.count())

# Step 7: Save as Delta table
df.write \
    .mode("overwrite") \
    .parquet("output/employee_synthetic_data")
