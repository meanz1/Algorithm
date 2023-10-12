# -- 코드를 입력하세요
# SELECT month(start_date) as date, car_id, count(car_id) as records from car_rental_company_rental_history

# where car_id in (
#     select car_id from car_rental_company_rental_history
#     where month(start_date) between 8 and 10
#     group by 1
#     having count(car_id)>=5
#     order by month(start_date), car_id desc
# )
# group by car_id, month(start_date)
# order by month(start_date), car_id desc

SELECT month(start_date) as month, car_id, count(history_id) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where month(start_date) between 8 and 10 and car_id in 
(select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
 where month(start_date) between 8 and 10
 group by car_id 
 having count(history_id)>4) 
group by month, car_id
having records >0
order by month, car_id desc
