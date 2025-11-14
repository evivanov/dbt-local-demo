{% docs test_positive_number_rows %}

This test validates that the raw_sales table contains at least one row of data. An empty table would indicate a problem with the data loading process or source file availability. This is a critical check to ensure that downstream models have data to transform and that the ETL pipeline is functioning correctly. The test uses a strict comparison (strictly: true) to require at least one row, ensuring that the analytics pipeline always has data to process.

{% enddocs %}
