--Export city data

select *
from city_data
where lower(country) = 'brazil'
and lower(city) = 'rio de janeiro'
