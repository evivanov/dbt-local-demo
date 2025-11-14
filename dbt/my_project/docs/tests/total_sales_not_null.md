{% docs test_total_sales_not_null %}

This test verifies that total_sales contains no NULL values. Every product in the summary should have a calculable sales total, even if it's zero. NULL values in this critical financial metric would indicate incomplete data processing or calculation errors, potentially leading to inaccurate revenue reporting and business decisions.

{% enddocs %}
