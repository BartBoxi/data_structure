# Given a file consisting of lines like this:
# 2017-02-01T20:00 OperationA Start
# 2017-02-01T20:01 OperationA End
# 2017-02-01T20:08 OperationB Start
# 2017-02-01T20:09 OperationC Start
# 2017-02-01T20:10 OperationB End
# 2017-02-01T20:12 OperationC End
# Produce an average runtime of all operations.
# Example output:
# Average: 0 days 0 hours 2 minutes (0 days 0 hours 6 minutes total for 3 operations) 



from datetime import datetime 

def findAverage(logs:List[str]) -> int:
    
    starts = {}
    durations = []
    
    for log in logs:
        ## you have to split the input from strings 
        
        time_str, op_name, op_type = log.split()
        
        
        time_converted = datetime.strptime(time_str, '%Y-%m-%dT%H:%M')
        
        if op_type == "Start":
            starts[op_name] = time_converted
            
        elif op_type == 'End':
            # counting the diff and changing to minutes 
            duration = (time_converted - starts[op_name]).total_seconds() / 60
            durations.append(duration) 
    if durations: 
        avg_runtime = sum(durations) / len(durations)
            
    return avg_runtime



logs = [
    "2017-02-01T20:00 OperationA Start",
    "2017-02-01T20:01 OperationA End",
    "2017-02-01T20:08 OperationB Start",
    "2017-02-01T20:09 OperationC Start",
    "2017-02-01T20:10 OperationB End",
    "2017-02-01T20:12 OperationC End"
]


print(findAverage(logs))