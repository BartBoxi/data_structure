def count_occupancy(events, time):
	sorted_events = sorted(events, key= lambda x : x[2])
	ans = 0
	occupancy = 0
	for event in sorted_events:
		if event[2] <= time:
			if event[1] == True:
				occupancy +=1
			else:
				occupancy -=1
		else:
			break
	return occupancy # here we got occupancy for specific time or i would say          until specific time

events = [
    (2, True, 3),
    (1, True, 3),
    (3, True, 4),
    (1, False, 5),
    (4, False, 6),
    (5, True, 6),
    (3, False, 6),
    (2, False, 7),
    (4, False, 7),
    (5, False, 7),
]

time = 7

print(count_occupancy(events, time))





#
#
#
# def find_max_occupancy(events):
# 	max_occupancy = 0
# 	time_for_max_occupancy = 0
# 	for sorted_event.time in events:
# 		occupancy_at_time =   count_occupancy(sorted_events,sorted_event.time)
# if occupancy_at_time > max_occupancy: # here we will get max value each time it is bigger than the current max value saved
# max_occupancy = occupancy_at_time
# time_for_max_occupancy = sorted_event.time
# 	return max_occupancy, time_for_max_occupancy
