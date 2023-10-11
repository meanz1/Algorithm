-- 코드를 입력하세요
SELECT a.rest_id, a.rest_name, a.food_type, a.favorites as favorites, a.address as address, round(avg(b.review_score), 2) as score from rest_info a
    join rest_review b
    on a.rest_id = b.rest_id
where address like '서울%'
group by rest_id
order by score desc, favorites desc