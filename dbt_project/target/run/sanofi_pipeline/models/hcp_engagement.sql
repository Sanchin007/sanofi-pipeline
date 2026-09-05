
  create or replace   view SANOFI_PIPELINE.dbt_dev.hcp_engagement
  
  
  
  
  as (
    SELECT 
    hcps.hcp_id,
    hcps.hcp_name,
    hcps.specialty,
    hcps.region,
    COUNT(calls.call_id) AS total_calls,
FROM SANOFI_PIPELINE.dbt_dev.stg_hcps AS hcps
LEFT JOIN SANOFI_PIPELINE.dbt_dev.stg_sales_calls AS calls
    ON hcps.hcp_id = calls.hcp_id
GROUP BY hcps.hcp_id, hcps.hcp_name, hcps.specialty, hcps.region
ORDER BY total_calls DESC
  );

