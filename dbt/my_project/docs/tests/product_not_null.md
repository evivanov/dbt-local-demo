{% docs test_product_not_null %}

This test validates that the product column contains no NULL values. Since product is the primary dimension for all aggregations and reporting, NULL values would compromise data integrity and make it impossible to properly attribute sales and pricing data. This is a critical data quality check that ensures every record can be properly categorized and analyzed.

{% enddocs %}
