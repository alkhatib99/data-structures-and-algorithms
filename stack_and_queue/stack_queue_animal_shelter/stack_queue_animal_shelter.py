from stack_and_queue.queue import Queue
class AnimalShelter:

    def __init__(self):
        """Inialization of Animal Shelter class define,
         two queues one for dogs and other for cats 
        """
        self.dogs=Queue()
        self.cats=Queue()
        pass

    def enqueue(self,animal):
        """Method to add an animal to to the queue, if it was "dog" or "cat"
        """
         
        
        if animal.lower().startswith("dog"):
           self.dogs.enqueue(animal) 
        elif animal.lower().startswith("cat"):
            self.cats.enqueue(animal) 

        else :
            raise Exception('The input not dog or cat')


    def dequeue(self,pref):
        """Method to remove and return a animal if was there found,
        else will return null, 
        * if the animal was not dog or cat will raise exception  
        """
        pref=str(pref)
        if pref.lower().startswith("dog"):
            self.dogs.dequeue()
        elif pref.lower().startswith("cat"):
            self.cats.dequeue()
        else: 
            return "Null"

if __name__=="__main__":
    pass