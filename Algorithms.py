
def FCFS(processes):

    for p in processes:
        p.reset()
 
    gantt= []
    remaining = list(processes)
    current_time = 0

    while remaining:
        ready_queue = [p for p in remaining if p.at <= current_time]

        if not ready_queue:
          current_time= min(p.at for p in remaining )
          continue

        chosen = ready_queue[0]
        for p in ready_queue[1:]:
            if p.at < chosen.at:
                chosen = p
            elif p.at == chosen.at: #tiebreaker
                if p.pid < chosen.pid:
                    chosen = p

        start= current_time
        current_time+= chosen.bt
        chosen.ct = current_time
        if chosen.start == -1:
            chosen.start = start

        gantt.append((chosen.pid, start, current_time))
        remaining.remove(chosen)

    return gantt

##############################################################

def SJF(processes):
    for p in processes:
        p.reset()
 
    gantt= []
    remaining = list(processes)
    current_time = 0

    while remaining:
        ready_queue = [p for p in remaining if p.at <= current_time]

        if not ready_queue:
          current_time= min(p.at for p in remaining )
          continue
       
        chosen = ready_queue[0]
        for p in ready_queue[1:]:
            if p.bt < chosen.bt:
                chosen = p
            elif p.bt == chosen.bt: #tiebreaker 1
                if p.at < chosen.at:
                    chosen = p
                elif p.at == chosen.at: #tiebreaker 2
                    if p.pid < chosen.pid:
                        chosen = p

        start= current_time
        current_time+= chosen.bt
        chosen.ct = current_time
        if chosen.start == -1:
            chosen.start = start

        gantt.append((chosen.pid, start, current_time))
        remaining.remove(chosen)

    return gantt

##############################################################

def priority(processes):
    
    for p in processes:
        p.reset()
 
    gantt= []
    remaining = list(processes)
    current_time = 0

    while remaining:
        ready_queue = [p for p in remaining if p.at <= current_time]

        if not ready_queue:
          current_time= min(p.at for p in remaining)
          continue
        else:
            chosen = ready_queue[0]
            for p in ready_queue[1:]:
                if p.priority < chosen.priority:
                    chosen = p
                elif p.priority == chosen.priority: #tiebreaker 1
                    if p.at < chosen.at:
                      chosen = p
                    elif p.at == chosen.at: #tiebreaker 2
                       if p.pid < chosen.pid:
                            chosen = p

        start= current_time
        current_time+= chosen.bt
        chosen.ct = current_time
        if chosen.start == -1:
            chosen.start = start

        gantt.append((chosen.pid, start, current_time))
        remaining.remove(chosen)

    return gantt

##############################################################

def RR(processes):
    for p in processes:
        p.reset()
                
    remaining = list(processes)
    ready_queue = []
    gantt = []
    current_time = 0
    quantum = 2

    while remaining:
        for p in remaining: #add arrived processes to ready queue
            if p.at <= current_time and p not in ready_queue:
                ready_queue.append(p)

        if not ready_queue:
            current_time = min(p.at for p in remaining)
            continue

        p = ready_queue.pop(0)

        if p.start == -1:
            p.start = current_time

        start = current_time
        q = min(quantum, p.remaining_bt)
        p.remaining_bt -= q
        current_time += q

        gantt.append((p.pid, start, current_time))

        if p.remaining_bt == 0:
            p.ct = current_time
            remaining.remove(p)
        else:
            for p2 in remaining: #check new processes before appending current process to end of queue
                if p2.at <= current_time and p2 not in ready_queue and p2 != p:
                    ready_queue.append(p2)
            ready_queue.append(p)

    return gantt