{% docs sales_summary %}

# Sales Summary Model

This model provides a comprehensive aggregated view of sales data by product. It serves as a key reporting table for understanding product performance across all transactions.

## Business Context

The sales_summary table is designed to answer critical business questions such as:
- Which products generate the most revenue?
- What is the total volume of sales for each product?
- How many individual transactions does each product have?

## Data Aggregation

This model aggregates transaction-level data from the raw sales source, grouping by product to calculate:
- **Total Sales**: The sum of all revenue generated (quantity × price) for each product
- **Total Transactions**: The sum of all units sold for each product

## Usage

This table is commonly used for:
- Executive dashboards and KPI tracking
- Product performance analysis
- Sales team reporting
- Revenue forecasting and trend analysis

## Data Quality

Multiple tests are applied to ensure data integrity:
- Product values must be unique and non-null
- Sales and transaction values must be non-negative
- All numeric fields are validated for completeness

{% enddocs %}
