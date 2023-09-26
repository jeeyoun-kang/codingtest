#USED_GOODS_BOARD와 USED_GOODS_FILE 테이블에서 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로를 조회
#첨부파일 경로는 FILE ID를 기준으로 내림차순 정렬
#기본적인 파일경로는 /home/grep/src/ 이며
#게시글 ID를 기준으로 디렉토리가 구분되고, 파일이름은 파일 ID, 파일 이름, 파일 확장자로 구성
SELECT CONCAT("/home/grep/src/",A.BOARD_ID,"/",FILE_ID,FILE_NAME,FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD A
JOIN USED_GOODS_FILE B ON A.BOARD_ID = B.BOARD_ID
WHERE VIEWS IN (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
-- WHERE VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY VIEWS DESC, FILE_ID DESC;

#VIEWS를 서브쿼리 WHERE절로 높은 조회수 조회