{% docs test_total_transactions_not_null %}

This test ensures that the transactions column (total units sold) never contains NULL values. Every product in the summary must have a valid transaction count to maintain data integrity. NULL values would compromise volume analysis and prevent accurate calculation of metrics like average order size or inventory turnover rates.

{% enddocs %}
