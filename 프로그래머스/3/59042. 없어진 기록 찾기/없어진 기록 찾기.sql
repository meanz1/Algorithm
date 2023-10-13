select a.animal_id, a.name 
from animal_outs a
left join animal_ins b 
on a.animal_id = b.animal_id
where b.animal_id is null

# SELECT B.ANIMAL_ID, B.NAME
# FROM ANIMAL_INS A
# RIGHT JOIN ANIMAL_OUTS B
# ON A.ANIMAL_ID = B.ANIMAL_ID
# WHERE A.ANIMAL_ID IS NULL