with first_day as(
    select player_id, 
    min(event_date) as first_login
    from Activity
    group by player_id
),
second_day as(
    select distinct f.player_id
    from first_day f
    join Activity a
    on f.player_id = a.player_id
    and a.event_date = f.first_login + interval '1 day'

)
select round(
    (select count(*) from second_day)::numeric
    / (select count(distinct player_id) from Activity)
    ,2
)
as fraction;