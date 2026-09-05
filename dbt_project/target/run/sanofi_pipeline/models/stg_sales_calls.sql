
  create or replace   view SANOFI_PIPELINE.dbt_dev.stg_sales_calls
  
  
  
  
  as (
    select
    call_id,
    hcp_id,
    cast(call_date as date) as call_date,
    channel
from raw.sales_calls
  );

