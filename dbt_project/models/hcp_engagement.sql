with hcps as (
    select * from {{ ref('stg_hcps') }}
),

calls as (
    select * from {{ ref('stg_sales_calls') }}
)

select
    h.hcp_id,
    h.hcp_name,
    h.specialty,
    h.region,
    count(c.call_id) as total_calls,
    coalesce(sum(c.email_opens), 0) as total_email_opens,
    (count(c.call_id) * 10) + coalesce(sum(c.email_opens), 0) as engagement_score
from hcps h
left join calls c on h.hcp_id = c.hcp_id
group by 1, 2, 3, 4