SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
-- WHERE YEAR(APNT_YMD)=2022 AND MONTH(APNT_YMD) = 5
GROUP BY MCDP_CD
ORDER BY 2, 1; -- 숫자는 칼럼순을 의미
