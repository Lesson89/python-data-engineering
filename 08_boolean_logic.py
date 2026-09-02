records_processed = 5000
missing_records = 50
pipeline_running = True

if records_processed > 0 and missing_records < 100 and pipeline_running:
    print("pipeline can continue")
else:
    print("pipeline cannot continue")   