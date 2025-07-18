# A entry/exit event recorded at building entrance
class Event {
  def __init__(self, badgeId, isEntry, timestamp):
    self.badgeId = badgeId
    self.isEntry = isEntry # if false, event is Exit
    self.timestamp = timestamp # number of seconds since midnight
}

# Print max number of people in the building and timestamp when it occurs
def findMaxOccupancy(events) {
  # Implement me!
}


def count_occupancy(sorted_events, time):
 ans = 0
 occupancy = 0
  for event in sorted_events:
	if event.time < time:
		if event.isEntry = True:
			occupancy +=1
		else:
			occupancy +=1
	else:
		break
   return occupancy # here we got occupancy for specific time or i would say          until specific time

def find_max_occupancy(events):
	max_occupancy = 0
	time_for_max_occupancy = 0
	for sorted_event.time in events:
		occupancy_at_time =   count_occupancy(sorted_events,sorted_event.time)
if occupancy_at_time > max_occupancy: # here we will get max value each time it is bigger than the current max value saved
max_occupancy = occupancy_at_time
time_for_max_occupancy = sorted_event.time
	return max_occupancy, time_for_max_occupancy
