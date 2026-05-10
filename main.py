from process import *
from metrics import *
from Algorithms import *


def run_all(dataset_name, processes):
    algorithms = [
        ("FCFS", FCFS),
        ("SJF", SJF),
        ("Priority", priority),
        ("Round Robin", RR),
    ]

    for name, algo in algorithms:
        print(f"\n{'='*50}")
        print(f"  {name} — {dataset_name}")
        print(f"{'='*50}")

        gantt = algo(processes)

        print_gantt(gantt)
        print()
        print_metrics(processes)

if __name__ == "__main__":

    A= [
        Process("P1", at=0, bt=7, priority=2),
        Process("P2", at=2, bt=4, priority=1),
        Process("P3", at=4, bt=1, priority=3),
        Process("P4", at=5, bt=4, priority=2),
        Process("P5", at=6, bt=3, priority=1),
    ]

    B= [
        Process("P1", at=0, bt=20, priority=3),
        Process("P2", at=1, bt=2,  priority=1),
        Process("P3", at=2, bt=1,  priority=2),
        Process("P4", at=3, bt=3,  priority=1),
        Process("P5", at=4, bt=2,  priority=2),
        Process("P6", at=6, bt=1,  priority=1),
    ]

    run_all("Dataset A", A)
    run_all("Dataset B", B)
