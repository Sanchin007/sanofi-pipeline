SELECT 
    region,
    COUNT(DISTINCT hcp_id) AS active_hcps,
    SUM(total_calls) AS total_calls,
    ROUND(SUM(total_calls) :: FLOAT / COUNT(DISTINCT hcp_id), 1) AS avg_calls_per_hcp
FROM {{ ref('hcp_engagement') }}
GROUP BY region
ORDER BY total_calls DESC

