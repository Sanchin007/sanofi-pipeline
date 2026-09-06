{{ config(materialized='table') }}

SELECT
    region,
    COUNT(hcp_id) AS total_hcps,
    ROUND(AVG(engagement_score), 2) AS avg_engagement_score,
    SUM(total_calls) AS total_sales_calls
FROM {{ ref('hcp_engagement') }}
GROUP BY region