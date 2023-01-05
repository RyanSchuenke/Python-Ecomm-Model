import random

class EcomOrder:

    def __init__(self, order_type, due, order_size):
        # initializer method for creating an order, specifying type, time, and duration
        if order_type in ["P", "D"]:
            self.__order_type = order_type
        else:
            raise Exception("The order type must be pickup ('P') or delivery ('D')")
        
        if 7< due <21:
            self.__due = due
        else:
            raise Exception("Orders can only be placed between the hours of 8 and 20 (8pm)")
        
        if type(order_size) == int and order_size>0:
            self.__duration = order_size
        else:
            raise Exception("The order size must be a positive integer")

        self.__priority = 0
        # calculates priority based off of order qualities
        if self.__order_type == "D":
            self.__priority +=2
        if self.__duration >60: # large orders that can be double shopped are odd
            self.__priority +=1
        
        # id to increment to differentiate between orders with identical properties
        self.__id = 0 
    

    def collision(self): 
        # Called when an identical order is present in order to prevent overwritting
        self.__id +=1



    # getter methods for the differnt attributes of an order
    def get_type(self):
        return self.__order_type

    def get_due(self):
        return self.__due

    def get_duration(self):
        return self.__duration

    def get_priority(self):
        return self.__priority



    def __repr__(self): 
        # represents orders as a string
        # "Order type: D/P (Order type)  Due time: ##(due time):00  Time to complete: #(duration) minutes"
        return "Order type: "+str(self.__order_type)+"  Due time: "+str(self.__due)+":00  Time to complete: "+str(self.__duration)+" minutes"
    # all operations are O(1) time complexity

class ShopQueue:

    def __init__(self): # initiator method O(1)
        self.order_queue = [] # creates a list

    def add(self, order): # adds an item to the end and sorts the list in O(n) time
        self.order_queue.append(order)
        self.sort()
        # self.sort1()

    def sort(self): # sorts the ordered queue in O(n) time 
        # sorts by delivery before pickup then by increasing size for each hour
        # found to be better than other sorting method

        if len(self.order_queue) <=1: 
            # doesn't sort when only one item is in the list
            pass
        else:
            for index in range(len(self.order_queue)):
                # iterates through the list until the order the new one should be placed before is found, 
                # all subsequent orders have their indices updated, making the operation always O(n)

                if (self.order_queue[-1].get_due() == self.order_queue[index].get_due() and 
                self.order_queue[-1].get_priority() == self.order_queue[index].get_due() and 
                self.order_queue[-1].get_duration() == self.order_queue[index].get_duration()):
                # if the orders are identical
                    self.order_queue.insert(index,self.order_queue[-1])
                    self.order_queue.pop()
                    # the new order is added to the same location and the copy at the end is removed.
                    break

                elif self.order_queue[-1].get_due() > self.order_queue[index].get_due():
                    # if the order is due earlier, 
                    self.order_queue.insert(index,self.order_queue[-1])
                    self.order_queue.pop()
                    # the new order is placed at the index, the orders after are moved over
                    break 

                elif self.order_queue[-1].get_due() == self.order_queue[index].get_due():
                    # if the orders are due at the same time,
                    if self.order_queue[-1].get_priority() <2 and self.order_queue[index].get_priority() >1:
                        # if the order isn't a delivery and the other is,
                        self.order_queue.insert(index,self.order_queue[-1])
                        self.order_queue.pop()
                        # the new order is placed at the index, the orders after are moved over
                        break 

                    elif self.order_queue[-1].get_priority() >1 and self.order_queue[index].get_priority() >1:
                        # if both orders have priority,
                        if self.order_queue[-1].get_duration() > self.order_queue[index].get_duration():
                            # if the order is longer,
                            self.order_queue.insert(index,self.order_queue[-1])
                            self.order_queue.pop()
                            # the new order is placed at the index, the orders after are moved over
                            break

                    elif self.order_queue[-1].get_priority() <2 and self.order_queue[index].get_priority() <2:
                        # if neither orders have priority,
                        if self.order_queue[-1].get_duration() > self.order_queue[index].get_duration():
                            # if the order is longer,
                            self.order_queue.insert(index,self.order_queue[-1])
                            self.order_queue.pop()
                            # the new order is placed at the index, the orders after are moved over
                            break             


    def sort1(self):# sorts the ordered queue in O(n) time
        # sorts by puting large orders pickup/deliver before smaller pickup/delivery orders at each hour, 
        # keeping deliver before pickups

        # found to be less effective sorting method
        if len(self.order_queue) <=1:
            # doesn't sort when only one item is in the list
            pass
        else:
            for index in range(len(self.order_queue)):
                # iterates through the list until a place for the order is found at which point, 
                # all subsequent orders have their indices updated, making the operation always O(n)

                if (self.order_queue[-1].get_due() == self.order_queue[index].get_due() and 
                self.order_queue[-1].get_priority() == self.order_queue[index].get_due() and 
                self.order_queue[-1].get_duration() == self.order_queue[index].get_duration()):
                # if the orders are identical,
                    self.order_queue.insert(index,self.order_queue[-1])
                    self.order_queue.pop()
                    # the new order is placed at the index, the orders after are moved over
                    break

                elif self.order_queue[-1].get_due() > self.order_queue[index].get_due():
                    # if the order is due earlier, 
                    self.order_queue.insert(index,self.order_queue[-1])
                    self.order_queue.pop()
                    # the new order is placed at the index, the orders after are moved over
                    break 

                elif self.order_queue[-1].get_due() == self.order_queue[index].get_due():
                    #if the orders are due at the same time,
                    if self.order_queue[-1].get_priority() < self.order_queue[index].get_priority():
                        # if the order has a lower priority,
                        self.order_queue.insert(index,self.order_queue[-1])
                        self.order_queue.pop()
                        # the new order is placed at the index, the orders after are moved over
                        break 

                    elif self.order_queue[-1].get_priority() == self.order_queue[index].get_priority():
                        # if both orders have the same priority,
                        if self.order_queue[-1].get_duration() > self.order_queue[index].get_duration():
                            # if the order is longer,
                            self.order_queue.insert(index,self.order_queue[-1])
                            self.order_queue.pop()
                            # the new order is placed at the index, the orders after are moved over
                            break


    def dequeue(self): # removes and returns last item O(1)
        return self.order_queue.pop()

    def is_empty(self): # checks if length is zero in O(1) time
        if len(self.order_queue) == 0:
            return True # returns true if length of zero
        else:
            return False

    def __getitem__(self,index): # index into the class object to index the list in O(1) time
        return self.order_queue[index]

    def __len__(self): # returns the number of objects in O(1) time
        return len(self.order_queue)

    def __repr__(self): # returns how the queue is to be displayed in reverse order in O(n) time
        orders = ""
        for i in range(len(self.order_queue)-1,-1,-1):
            # iterates through the list in reverse, so orders are listed forward 
            orders+=str(self.order_queue[i])+"\n"
        return(orders)


def store(): # model for a typical day
    unpicked = ShopQueue() # initializes list
    available_shoppers = 0 # number of shoppers available at a time to dequeue an order.
    
    picking = {} # dictionary for orders that are being processed
    potential_double_picks = [] # list for orders that are being single picked but can be doubled
    dequeue_orders = [] # list for orders that are going to be removed from picking
    
    completed_orders = 0 # accumulator for number of completed orders
    late_time = 0 # accumulator for late time
    

    for orders in range(2): # creates start of day orders for morning and deliveries
        order = EcomOrder("P", 8, random.randint(10,40))
        unpicked.add(order)
        order = EcomOrder("P", 20, random.randint(10,40))
        unpicked.add(order)
    for deliveries in range(11,18):
        for count in range(random.randint(0,3)):
            order = EcomOrder("D", deliveries, random.randint(15,75))
            unpicked.add(order)
    
    for orders in range(15):
        order = EcomOrder("P",random.randint(9,19), random.randint(1,121))
        unpicked.add(order)


    for hour in range(6,21): # iterates through hours that are worked

        # models the average day's number of workers at a given time
        # adds workers at 6am, 7am, 8am, 9am, and 12pm
        if hour == 6 or hour == 8 or hour == 9 or hour == 12:
            available_shoppers+=1
        elif hour == 7:
            available_shoppers+=4
        
        # removes workers at 2pm, 3pm, 4pm and 5pm
        elif hour == 14 or hour == 16 or hour == 17:
            available_shoppers-=1
        elif hour == 15:
            available_shoppers-=4
        # closing worker would leave once all orders are finished which should be either by 8pm and not after 9pm

        # adds new orders every hour
        if 8< hour <17:
            for orders in range(random.randint(1,4)):
                order = EcomOrder("P",random.randint(hour+2,20), random.randint(1,121))
                unpicked.add(order)
        elif 16 <hour<19:
            for orders in range(random.randint(0,2)):
                order = EcomOrder("P", 20, random.randint(1,60))
                unpicked.add(order)
        
        print(unpicked)
        for minute in range(0,60): # iterates through minutes of the hour

            dequeue_orders = []
            if len(picking) >0:
                for order in picking: 
                    # iterates through orders being picked

                    if picking[order] == 0: 
                        # if any orders have been completed,
                        if order.get_priority() %2 != 0: 
                            # if the priority is odd meaning the order is large
                            if order in potential_double_picks: 
                                # re add one person if double pick wasn't started and adds order to dequeue
                                available_shoppers +=1
                                potential_double_picks.remove(order)
                                dequeue_orders.append(order)
                                completed_orders +=1
                            else: 
                                # re add two available shoppers if the double picking was started and adds order to dequeue
                                available_shoppers +=2
                                dequeue_orders.append(order)
                                completed_orders+=1

                        else: # re adds a shopper when normal orders are completed and adds order to dequeue
                            available_shoppers +=1
                            dequeue_orders.append(order)
                            completed_orders+=1
                    else: 
                        # if the order isn't complete, the time is reduced by one
                        picking[order] -=1

            for order_index in range(len(dequeue_orders)):
                # removes all orders marked to be removed by the dequeue list
                picking.pop(dequeue_orders[order_index])
            

            while available_shoppers>0: # when there are workers available to start an order
                
                # potential double pick started with one person add another and cut the time in half
                if len(potential_double_picks)>0:
                    picking[potential_double_picks[-1]] = picking[potential_double_picks[-1]]//2
                    potential_double_picks.pop() # removes mark that order isn't being double picked
                    available_shoppers -=1


                # as long as there are orders to be completed,
                elif not unpicked.is_empty():
                    while unpicked[-1] in picking:
                        # if an order to be added is identical to an order in the dictionary already,
                        # collision is called to change the id and make them not identical
                        unpicked[-1].collision()

                    # potential double pick with only one available shopper moves it to picking and added to list, 
                    # marking it for future double picking
                    if available_shoppers ==1 and unpicked[-1].get_priority() % 2 != 0:
                        potential_double_picks.append(unpicked[-1])
                        picking[unpicked.dequeue()] = unpicked[-1].get_duration()
                        available_shoppers -=1

                    # double pick with two available shoppers moves order to picking
                    elif unpicked[-1].get_priority() % 2 !=0 and available_shoppers>1:
                        picking[unpicked.dequeue()] = unpicked[-1].get_duration() // 2
                        available_shoppers -=2

                    # single pick order takes one worker and moves the order to picking
                    else:
                        picking[unpicked.dequeue()] = unpicked[-1].get_duration()
                        available_shoppers -=1
                else:
                    break


            for order in range(len(unpicked)): # adds to the late time when an order is late and hasn't started yet
                if unpicked[order].get_due() <= hour:
                    if unpicked[order].get_priority() >1:
                        late_time +=100
                        # delivery orders add 100 since they need to be done on time
                        continue
                    late_time +=1

            
            for order in picking: # adds to the late time when an order is late while being worked on
                if order.get_due() <= hour:
                    if order.get_priority() >1:
                        late_time +=100
                        continue
                    late_time +=1



            print(hour, minute)
            print(picking)
            print(available_shoppers)
            print(late_time)
    print(completed_orders)
            
                
def stress_test(): 
    # definite orders to test sorting and compare efficiency

    unpicked = ShopQueue() # initializes list
    available_shoppers = 3 # number of shoppers available at a time to dequeue an order.
    
    picking = {} # dictionary for orders that are being processed
    potential_double_picks = [] # list for orders that are being single picked but can be doubled
    dequeue_orders = [] # list for orders that are going to be removed and from picking
    
    completed_orders = 0 # accumulator for number of completed orders
    late_time = 0 # accumulator for late time


    for time in range(4): # adds a mix of 3 large and 2 small orders every hour for 4 hourse
        for orders in range(3):
            order = EcomOrder("P",8+orders, 80)
            unpicked.add(order)
        for orders in range(2):
            order = EcomOrder("P",8+time, 20)
            unpicked.add(order)


    for hour in range(6,12):
        print(unpicked)
        for minute in range(0,60): # iterates through minutes of the hour

            dequeue_orders = []
            if len(picking) >0:
                for order in picking: 
                    # iterates through orders being picked

                    if picking[order] == 0: 
                        # if any orders have been completed,
                        if order.get_priority() %2 != 0: 
                            # if the priority is odd meaning the order is large
                            if order in potential_double_picks: 
                                # re add one person if double pick wasn't started and adds order to dequeue
                                available_shoppers +=1
                                potential_double_picks.remove(order)
                                dequeue_orders.append(order)
                                completed_orders +=1
                            else: 
                                # re add two available shoppers if the double picking was started and adds order to dequeue
                                available_shoppers +=2
                                dequeue_orders.append(order)
                                completed_orders+=1

                        else: # re adds a shopper when normal orders are completed and adds order to dequeue
                            available_shoppers +=1
                            dequeue_orders.append(order)
                            completed_orders+=1
                    else: 
                        # if the order isn't complete, the time is reduced by one
                        picking[order] -=1

            for order_index in range(len(dequeue_orders)):
                # removes all orders marked to be removed by the dequeue list
                picking.pop(dequeue_orders[order_index])
            

            # as long as there are orders to be completed,
            while available_shoppers>0: # when there are workers available to start an order
                
                # potential double pick started with one person add another and cut the time in half
                if len(potential_double_picks)>0:
                    picking[potential_double_picks[-1]] = picking[potential_double_picks[-1]]//2
                    potential_double_picks.pop() # removes mark that order isn't being double picked
                    available_shoppers -=1

                elif not unpicked.is_empty():
                    while unpicked[-1] in picking:
                        # if an order to be added is identical to an order in the dictionary already,
                        # collision is called to change the id and make them not identical
                        unpicked[-1].collision()

                    # potential double pick with only one available shopper moves it to picking and added to list, 
                    # marking it for future double picking
                    if available_shoppers ==1 and unpicked[-1].get_priority() % 2 != 0:
                        potential_double_picks.append(unpicked[-1])
                        picking[unpicked.dequeue()] = unpicked[-1].get_duration()
                        available_shoppers -=1

                    # double pick with two available shoppers moves order to picking
                    elif unpicked[-1].get_priority() % 2 !=0 and available_shoppers>1:
                        picking[unpicked.dequeue()] = unpicked[-1].get_duration() // 2
                        available_shoppers -=2

                    # single pick order takes one worker and moves the order to picking
                    else:
                        picking[unpicked.dequeue()] = unpicked[-1].get_duration()
                        available_shoppers -=1
                else:
                    break


            for order in range(len(unpicked)): # adds to the late time when an order is late and hasn't started yet
                if unpicked[order].get_due() <= hour:
                    if unpicked[order].get_priority() >1:
                        late_time +=100
                        continue
                    late_time +=1

            
            for order in picking: # adds to the late time when an order is late while being worked on
                if order.get_due() <= hour:
                    if order.get_priority() >1:
                        late_time +=100
                        continue
                    late_time +=1

            print(hour, minute)
            print(picking)
            print(available_shoppers)
            print(late_time)


def queue_test(): # test for making a sorted queue
    test_store = ShopQueue()
    for orders in range(2): # adds 2 orders for 8 and 20 with random size 
        order = EcomOrder("P", 8, random.randint(10,40))
        test_store.add(order)
        order = EcomOrder("P", 20, random.randint(10,40))
        test_store.add(order)
        
    for deliveries in range(11,18): # for each hour,
        for count in range(random.randint(0,3)): # 0-3 deliveries are added with random size
            order = EcomOrder("D", deliveries, random.randint(15,75))
            test_store.add(order)

    for orders in range(30): #adds 30 randomly due and sized pickup orders.
        order = EcomOrder("P",random.randint(8,19), random.randint(1,121))
        test_store.add(order)

    return test_store # returns the ordered queue


print(queue_test())
store()
stress_test()
