# Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

# All messages will come in chronological order. Several messages may arrive at the same timestamp.

# Implement the Logger class:

# Logger() Initializes the logger object.

# bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.


class Logger:
    def __init__(self):
        self.message_dict = {}
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_dict:
            self.message_dict[message] = timestamp
        
            return True
        
        if timestamp - self.message_dict[message]>= 10:
            self.message_dict[message] = timestamp

            return True
        else:
            return False

# T: O(1) creation of the dictionary -- the rest is O(1) this is happening in constant time
# Space - depends on the number of messages so I will say O(n) - n - number of messages 
        