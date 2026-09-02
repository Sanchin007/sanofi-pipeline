
  
  create view "warehouse"."main"."stg_hcps__dbt_tmp" as (
    select
    hcp_id,
    trim(hcp_name) as hcp_name,
    specialty,
    region
from raw.hcp_master
  );
