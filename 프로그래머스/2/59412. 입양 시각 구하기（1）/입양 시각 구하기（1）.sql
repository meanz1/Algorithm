-- 코드를 입력하세요
SELECT hour(datetime) as HOUR, count(*) as COUNT from animal_outs
where 9<=hour(datetime) and hour(datetime)<=20
group by HOUR
order by HOUR