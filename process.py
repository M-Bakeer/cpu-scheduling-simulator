class Process:
    def __init__(self, pid, at, bt, priority):
        self.pid = pid          
        self.at = at           
        self.bt = bt            
        self.priority = priority

        self.remaining_bt = bt  # for RR
        self.ct = 0            
        self.start = -1         # -1 = not started yet

    def reset(self):
        self.remaining_bt = self.bt
        self.ct = 0
        self.start = -1

