-- 코드를 입력하세요
SELECT ingredient_type, sum(total_order) as total_order from icecream_info b, first_half a
where a.flavor = b.flavor
group by b.ingredient_type
having sum(a.total_order)
order by a.total_order