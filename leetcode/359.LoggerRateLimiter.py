class Logger:

    def __init__(self):
        self.nextTimestamp = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.nextTimestamp and timestamp < self.nextTimestamp[message]:
            return False
        else:
            self.nextTimestamp[message] = timestamp + 10
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)