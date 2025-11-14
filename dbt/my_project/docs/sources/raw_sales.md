{% docs source_raw_sales %}

# Raw Sales Data

This table contains transaction-level sales data loaded from CSV files. Each row represents a single sale event with information about the product sold, pricing, quantity, and transaction date.

## Data Source

The data is loaded from `raw_sales.csv` files placed in the `/data` directory of the Docker environment. The loader service automatically detects new files and loads them into this table.

## Load Process

- **Frequency**: On-demand when the loader service runs
- **Method**: Truncate and reload (full refresh)
- **Schema**: Auto-created on first load with predefined column types

## Data Structure

The table contains four essential columns:
- Transaction date
- Product identifier
- Unit price
- Quantity sold

## Data Characteristics

- One row per transaction/sale event
- No aggregation - raw transactional data
- Historical data preserved across loads
- No soft deletes - data is fully replaced on each load

## Quality Expectations

- All columns should be populated (no NULLs expected)
- Dates should be valid calendar dates
- Prices and quantities should be positive numbers
- Table must contain at least one row of data

## Downstream Usage

This source table feeds into multiple dbt models:
- `sales_summary` - aggregates sales by product
- `avg_prices` - calculates average pricing metrics

{% enddocs %}
