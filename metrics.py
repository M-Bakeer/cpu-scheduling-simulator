def print_gantt(gantt):
    parts= []
    for pid, start, end in gantt:
        parts.append(f"{start}-{end} {pid}")

    full= " | ".join(parts)
    print(full)

def print_metrics(processes):

    total_tat = total_wt = total_rt = 0
    n = len(processes)

    print(f"{'PID':<6} {'AT':<5} {'BT':<5} {'CT':<5} {'TAT':<6} {'WT':<6} {'RT':<5}")
    print("-" * 45)

    for p in processes:
        tat= p.ct - p.at       
        wt= tat - p.bt          
        rt= p.start - p.at 

        total_tat += tat
        total_wt  += wt
        total_rt  += rt

        print(f"{p.pid:<6} {p.at:<5} {p.bt:<5} {p.ct:<5} {tat:<6} {wt:<6} {rt:<5}")

    print("-" * 45)
    print(f"{'Avg'}\t\t TAT={total_tat/n:<6.2f} WT={total_wt/n:<6.2f} RT={total_rt/n:<5.2f}")
