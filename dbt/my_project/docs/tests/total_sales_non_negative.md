{% docs test_total_sales_non_negative %}

This test checks that total_sales values are always greater than or equal to zero. Negative sales totals would indicate data quality issues such as incorrect price or quantity values, improper handling of returns/refunds, or calculation errors. While individual transactions might have negative values (refunds), the aggregated total should reflect the proper business logic for handling such cases.

{% enddocs %}
