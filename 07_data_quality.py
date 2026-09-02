expected_records = 5000
records_processed = 4800

missing_records = expected_records - records_processed
print("Missing records:", missing_records)

if missing_records == 0:
    print("Data quality: Perfect")
elif missing_records < 100:
    print("Data quality: Acceptable")
else:
    print("Data quality: Investigate missing records") 

#=========================================================
# 
expected_records = 5000
records_processed = 5000

missing_records = expected_records - records_processed
print("Missing records:", missing_records)

if missing_records == 0:
    print("Data quality: Perfect")
elif missing_records < 100:
    print("Data quality: Acceptable")
else:
    print("Data quality: Investigate missing records") 

#=========================================================#

expected_records = 5000
records_processed = 4950

missing_records = expected_records - records_processed
print("Missing records:", missing_records)

if missing_records == 0:
    print("Data quality: Perfect")
elif missing_records < 100:
    print("Data quality: Acceptable")
else:
    print("Data quality: Investigate missing records") 
    
