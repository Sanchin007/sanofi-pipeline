
  create or replace   view SANOFI_PIPELINE.dbt_dev.stg_hcps
  
  
  
  
  as (
    select
    hcp_id,
    trim(hcp_name) as hcp_name,
    specialty,
    region
from raw.hcp_master
  );

