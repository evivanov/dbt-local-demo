{% docs test_total_transactions_non_negative %}

This test validates that transaction counts are always greater than or equal to zero. Negative transaction quantities are logically invalid and would indicate serious data quality problems in the source data or transformation logic. This test helps maintain the integrity of volume-based metrics and ensures reliable inventory and demand planning.

{% enddocs %}
