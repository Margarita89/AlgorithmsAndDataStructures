# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
# People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like.
# Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.

from collections import deque

class AnimalShelter():

    def __init__(self):
        self.queueDog = deque()
        self.queueCat = deque()
        self.oldest = 0


    def enqueue(self, item, animal):
        if animal == 'dog':
            self.queueDog.append((item, self.oldest))
        elif animal == 'cat':
            self.queueCat.append((item, self.oldest))
        else:
            print('We only accept dog and cat')
            return
        self.oldest += 1


    def dequeueAny(self):
        # if there are no animals
        if not self.queueDog and not self.queueCat:
            print('There are no animals currently')
            return
        # if there are no dogs
        if not self.dequeueDog:
            first_cat = self.queueCat.popleft()
            return first_cat[0]
        # if there are no cats
        if not self.dequeueCat():
            first_dog = self.queueDog.popleft()
            return first_dog[0]

        first_cat = self.queueCat.popleft()
        first_dog = self.queueDog.popleft()

        # check if cat arrived earlier
        if first_cat[1] < first_dog[1]:
            return first_cat[0]
        return first_dog[0]


    def dequeueDog(self):
        if not self.dequeueDog:
            print('There are no dogs, sorry')
            return
        first_dog = self.queueDog.popleft()
        return first_dog[0]


    def dequeueCat(self):
        if not self.dequeueCat:
            print('There are no cats, sorry')
            return
        first_cat = self.queueCat.popleft()
        return first_cat[0]


if __name__ == "__main__":
    # create empty AnimalShelter
    animalSh = AnimalShelter()

    animalSh.enqueue(5, 'cat')
    animalSh.enqueue(6, 'dog')
    animalSh.enqueue(62, 'dog')
    animalSh.enqueue(17, 'dog')
    animalSh.enqueue(2, 'cat')
    print(animalSh.dequeueAny())
    animalSh.enqueue(9, 'cat')
    animalSh.enqueue(3, 'cat')
    print(animalSh.dequeueAny())
    animalSh.enqueue(91, 'dog')
    animalSh.enqueue(51, 'cat')
    print(animalSh.dequeueDog())
    animalSh.enqueue(10, 'dog')
    print(animalSh.dequeueCat())
