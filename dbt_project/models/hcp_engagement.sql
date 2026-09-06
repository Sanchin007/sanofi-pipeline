{{ config(
    materialized='incremental',
    unique_key='hcp_id'
) }}

WITH sales_calls AS (
    SELECT * FROM {{ ref('stg_sales_calls') }}
    {% if is_incremental() %}
        WHERE call_date > (SELECT MAX(latest_call_date) FROM {{ this }})
    {% endif %}
),
hcps AS (
    SELECT * FROM {{ ref('stg_hcps') }}
)
SELECT
    h.hcp_id,
    h.hcp_name,
    h.region,
    COUNT(s.call_id) AS total_calls,
    MAX(s.call_date) AS latest_call_date,
    ROUND(COUNT(s.call_id) * 12.5, 2) AS engagement_score
FROM hcps h
LEFT JOIN sales_calls s ON h.hcp_id = s.hcp_id
GROUP BY 1, 2, 3