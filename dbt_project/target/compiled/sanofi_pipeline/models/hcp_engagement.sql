with hcps as (
    select * from "warehouse"."main"."stg_hcps"
),

calls as (
    select * from "warehouse"."main"."stg_sales_calls"
)

select
    h.hcp_id,
    h.hcp_name,
    h.specialty,
    h.region,
    count(c.call_id) as total_calls,
    count(c.call_id) * 10 as engagement_score
from hcps h
left join calls c on h.hcp_id = c.hcp_id
group by 1, 2, 3, 4