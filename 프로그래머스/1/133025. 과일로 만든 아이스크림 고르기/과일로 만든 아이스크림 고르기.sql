-- 코드를 입력하세요
SELECT a.flavor from first_half a
JOIN icecream_info b ON a.flavor = b.flavor
WHERE a.total_order >= 3000 and ingredient_type = 'fruit_based'
ORDER BY a.total_order desc