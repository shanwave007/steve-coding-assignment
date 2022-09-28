import random
from time import sleep
from unittest import skip

completed_product_count = 0
conveyor_belt_length = 5
conveyor_belt = []
production_line_A = []
production_line_B = []
worker_count = conveyor_belt_length * 2
input_items = ["A","B","N"]


class Worker():
    
    timer_countdown = 3
    object_drawer = []
    locker = []
    
    def __init__(self, id, work_in_progress, items, process_time):
        self.id = id
        self.work_in_progress = work_in_progress
        self.object_drawer = items
        self.finished_product = ""
        self.timer_countdown = process_time
        
    def getId(self):
        return self.id
    
    def getLocker(self):
        if self.locker.__contains__("P"):
            print("Yes product exist")

    def getWorkStatus(self):
        return self.work_in_progress
        
    def isItemsFull(self,param):
        if param is "N":
            return False
        else:
            if param in self.object_drawer:
                return True
            else:
                return False
            
    def makeProduct(timer_countdown):
        sleep(timer_countdown)

def allocate_raw_material(item,belt_slot,worker1,worker2):
    #Rotating each belt item in between the workers who are placed both sides of each slot to identify who needs the part
    if item == "N" and worker1.locker.__contains__("P") or worker2.locker.__contains__("P"):
        #If belt item is empty and either worker has a finished product with him, product is adding to the same empty slot. And clearing the workers cache
        if worker1.locker.__contains__("P"):
            worker1.locker = []
            conveyor_belt.pop(belt_slot)
            conveyor_belt.insert(belt_slot,"P")
            worker1.work_in_progress = False
            worker1.locker=[]
            worker1.object_drawer=[]
        elif worker2.locker.__contains__("P"):
            worker2.locker = []
            conveyor_belt.pop(belt_slot)
            conveyor_belt.insert(belt_slot,"P")
            worker2.work_in_progress = False
            worker2.locker=[]
            worker2.object_drawer=[]
    elif item != "N" and item != "P":
        #if belt item is not empty and if it is not a finished product
        #checking whether line 1 employee already has the item
            if worker1.isItemsFull(item) == True:
                #If line 1 employee have the item, checking whether the line 2 employee have the item
                if worker2.isItemsFull(item) == True:
                    skip
                    #if both have the item, skipping the point
                elif worker2.isItemsFull(item) == False: 
                    #if line 2 employee doesn't have the item adding it to the line 2 employee
                    if len(worker2.object_drawer) == 1:
                        #if line 2 employee got both the needed part
                        worker2.object_drawer.append(item)
                        conveyor_belt.pop(belt_slot)
                        conveyor_belt.insert(belt_slot,"N")
                        worker2.work_in_progress = True
                        sleep(3)
                        worker2.locker.append("P")
                    elif len(worker2.object_drawer) == 0:
                        #line 2 employee only have one kind of part
                        worker2.object_drawer.append(item)
                        conveyor_belt.pop(belt_slot)
                        conveyor_belt.insert(belt_slot,"N")
                        worker2.work_in_progress = False
                        worker2.locker=[]
                    
                        
            elif worker1.isItemsFull(item) != True:
                #if line 1 employee doesn't have the item
                if len(worker1.object_drawer) == 1:
                    #if line 1 employee got both the needed part
                    worker1.object_drawer.append(item)
                    conveyor_belt.pop(belt_slot)
                    conveyor_belt.insert(belt_slot,"N")
                    worker1.work_in_progress = True
                    sleep(3)
                    # worker1.object_drawer=[]
                    worker1.locker.append("P")
                elif len(worker1.object_drawer) == 0:
                    #line 1 employee only have one kind of part
                    worker1.object_drawer.append(item)
                    conveyor_belt.pop(belt_slot)
                    conveyor_belt.insert(belt_slot,"N")
                    worker1.work_in_progress = False
                    worker1.locker=[]

def assigning_the_workers_to_lines():
    if(worker_count %2 == 0):
        print("Sending workers to the belt...")
        for worker in range(1,worker_count+1):
            if(worker <= worker_count/2):
                production_line_A.append(Worker(worker, False, [], 3))
            else:
                production_line_B.append(Worker(worker, False, [], 3))
        # print(production_line_A[0].isItemsFull())
        print("Both lines are formed!!!. Good to proceed.")
    else:
        print("Incorrect worker count")
        
def pick_and_place_item():
    random.shuffle(input_items)
    return input_items[0]

def rotate_belt(raw_material_item):
    #Assigning conveyor belt item count to identify from which point needs to add the materials to the belt
    items_in_belt = len(conveyor_belt)
    
    if items_in_belt == 0:
        #Initiation of the programme. Belt has no attributes
        conveyor_belt.insert(0,raw_material_item)
        allocate_raw_material(raw_material_item,0,production_line_A[0],production_line_B[0])
    elif items_in_belt > 0 and items_in_belt < conveyor_belt_length:
        #Belt has few attributes but still behind the full belt length 
        conveyor_belt.insert(0, raw_material_item)
        for item in range(1,len(conveyor_belt)+1):
            allocate_raw_material(conveyor_belt[((len(conveyor_belt))-item)],(len(conveyor_belt))-item,production_line_A[(len(conveyor_belt)-item)],production_line_B[(len(conveyor_belt)-item)])
    elif items_in_belt == conveyor_belt_length:
        #Belt is fully occupied
        if conveyor_belt[len(conveyor_belt)-1] == "P":
            #Check whether the last belt item is a finished product. If it is, adding 1 to the total count
            global completed_product_count
            completed_product_count+=1
            conveyor_belt.pop()
            print(completed_product_count)
        else:
            #If the final product is not a finished product, just removing it from the belt
            conveyor_belt.pop()
        conveyor_belt.insert(0, raw_material_item)
        for item in range(1,len(conveyor_belt)+1):
            allocate_raw_material(conveyor_belt[(len(conveyor_belt))-item],(len(conveyor_belt))-item,production_line_A[(len(conveyor_belt)-item)],production_line_B[(len(conveyor_belt)-item)])
    print(conveyor_belt)
            
            
def starting_the_belt():
    
    #Preparing the worker lines on both sides of the belt
    assigning_the_workers_to_lines()
    print("Starting the belt. Switched ON!!!")
    
    #Executing the programme for 100seconds
    for i in range(1,101):
        print("---------------------------------------")
        sleep(1)
        rotate_belt(pick_and_place_item())
        
    #Executing the programme for 100seconds
    print(f"completed product count - {completed_product_count}")
   
#Main function to start the programme
starting_the_belt()
