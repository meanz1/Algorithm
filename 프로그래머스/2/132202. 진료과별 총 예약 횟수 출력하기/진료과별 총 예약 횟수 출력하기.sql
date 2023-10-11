-- 코드를 입력하세요
SELECT mcdp_cd as '진료과코드', count(*) as '5월예약건수' from appointment
where year(apnt_ymd) = 2022 and month(apnt_ymd) = 5
group by mcdp_cd
order by `5월예약건수` asc, mcdp_cd asc

# SELECT MCDP_CD AS `진료과 코드`, COUNT(*) AS 5월예약건수
# FROM APPOINTMENT
# WHERE APNT_YMD LIKE '2022-05%'
# GROUP BY MCDP_CD
# ORDER BY 5월예약건수 ASC, MCDP_CD ASC;