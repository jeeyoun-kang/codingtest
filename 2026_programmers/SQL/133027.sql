--FIRST_HALF테이블의 SHIPMENT_ID는 JULY테이블의 SHIPMENT_ID의 외래 키

--7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값
--이 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문

-- 상반기 주문 FIRST_HALF, 7월 아스크림 주문정보 JULY


SELECT A.FLAVOR
FROM FIRST_HALF A
JOIN (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS JULY_SUM --B에서 FLAVOR별로 처리해야 비교가능
    FROM JULY
    GROUP BY FLAVOR
) B ON A.FLAVOR = B.FLAVOR
ORDER BY A.TOTAL_ORDER + B.JULY_SUM DESC
FETCH FIRST 3 ROWS ONLY --ROWNUM대신에 바로 쿼리에 붙일수 있어서 자주 씀(ROWNUM : 정렬 전에 매겨져서 서브쿼리로 감싸야 함)