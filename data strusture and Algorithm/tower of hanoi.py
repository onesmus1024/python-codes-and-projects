disks=3
auxiliary_rod=[]
destination_rod=[]
source_rod=[]
def packing_rod_in_source_disk(disks):
    for i in reversed(range(1,disks+1)):
        source_rod.append(i)
    
    print("source rod contains")
    print(source_rod)


packing_rod_in_source_disk(disks)
def tower_of_hanoi(disks,source,destination,auxiliary):
    if disks == 1:
        destination.append(source.pop())
        print("destination rod contains")
        print(destination_rod)
    else:
        tower_of_hanoi(disks-1,source,auxiliary,destination)
        tower_of_hanoi(disks-1,auxiliary,destination,source)

tower_of_hanoi(disks,source_rod,destination_rod,auxiliary_rod)