# 시스템은 key,value로 구성
#준하는 JBNU를 개조하여 잘못된 Key를 입력하더라도
# 그 잘못된 Key와 제일 근접한 Key를 찾아주는 메커니즘을 도입
#Key와 Value는 항상 정수
#가장 근접한 Key란 두 수의 차이가 가장 작은 Key를 의미
#두 수의 차이가 K보다 큰 경우는 Key로 인정하지 않음
#초기 데이터 상태가 주어질 때, 데이터 추가, 수정 및 검색을 지원하는 프로그램을 작성

import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
