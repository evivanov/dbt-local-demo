{% docs source_raw %}

# Raw Data Schema

The raw schema contains data loaded directly from external sources into the database. This schema serves as the landing zone for all incoming data before any transformations are applied.

## Data Pipeline

Data in the raw schema is loaded through an automated Docker-based loader service that:
- Monitors the `/data` directory for CSV files
- Automatically creates tables based on file structure
- Loads data with proper type casting and validation
- Maintains idempotency through truncate-and-reload strategy

## Schema Organization

All raw tables follow a consistent naming convention and structure pattern. The schema is designed to be read-only from the dbt perspective, with all data modifications happening through the external loader service.

## Data Quality

Source data undergoes basic validation during the load process, but comprehensive data quality checks and transformations are applied in downstream dbt models. The raw schema preserves data in its original form to maintain traceability and enable reprocessing if needed.

## Usage

This schema should only be referenced by dbt sources and staging models. Direct querying of raw tables should be avoided in favor of using the transformed and tested models in the analytics layer.

{% enddocs %}
