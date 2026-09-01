records_processed = 5000
total_revenue = 196781603.50
source_system = "SQL Server"
pipeline_running = True

print("records_processed:", records_processed)
print("total_revenue:", total_revenue)
print("source_system:", source_system)
print("pipeline_running:", pipeline_running)

print(type(records_processed))  # <class 'int'>
print(type(total_revenue))  # <class 'float'>
print(type(source_system))  # <class 'str'>
print(type(pipeline_running))  # <class 'bool'>

# The pipeline processed 5000 records.
print("The pipeline processed", records_processed, "records.")

print(f"The pipeline processed {records_processed} records.")