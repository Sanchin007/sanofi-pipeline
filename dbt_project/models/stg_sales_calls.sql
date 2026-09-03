select
    call_id,
    hcp_id,
    cast(call_date as date) as call_date,
    channel
from raw.sales_calls