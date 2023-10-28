#2번문제
# gpt 참조
from collections import defaultdict
def solution(products, purchased):
    product_dict = defaultdict(list)
    for p in products:
        p_info = p.split()
        product_dict[p_info[0]] = p_info[1:]

    purchased_ranking = defaultdict(int)
    for item in purchased:
        for f in product_dict[item]:
            purchased_ranking[f] += 1

    final_product = None
    final_priority = 0

    for product, features in product_dict.items():
        if product not in purchased:
            priority = 0
            for f in features:
                if purchased_ranking[f] > 0:
                    priority += 1
            #추천 제품 우선순위로 결정
            if priority > final_priority or (priority == final_priority and product < final_product):
                final_product = product
                final_priority = priority

    return final_product


#3번문제
#gpt 참조
def solution(N, simulation_data):
    wait_times = []
    end_times = [0] * N

    for data in simulation_data:
        arrival_time, process_time = data
        if arrival_time >= end_times[0]:
            end_times[0] = arrival_time + process_time
            wait_times.append(0)
        else:
            min_end_time_index = end_times.index(min(end_times))
            if arrival_time < end_times[min_end_time_index]:
                wait_time = end_times[min_end_time_index] - arrival_time
                wait_times.append(wait_time)
                end_times[min_end_time_index] += process_time
            else:
                wait_times.append(0)
                end_times[min_end_time_index] = arrival_time + process_time

    return sum(wait_times)