from abc import abstractmethod


# КЛАССЫ
class Group :
    pupis = True
    scholl_name = 23
    director = "Marivana"

    def __init__(self,title,pupils_count, group_leader):
        self.title = title
        self.pupils_count= pupils_count
        self.group_leader = group_leader



    def stady (self):
        print('сидит и учится')

    @abstractmethod
    def move (self):
        pass

class PrimaryGroup(Group):
    max_age = 11
    min_age = 6
    buildimg_section = "left"
    def __init__(self,title,pupils_count, group_leader, class_room):
        super().__init__(title,pupils_count, group_leader)
        self.class_room = class_room

    def move(self):
        print('бегают')

class HighGroup (Group):
    max_age = 18
    min_age = 14
    buildimg_section = "rait"
    def move(self):
        print('ходят')

class MediumGrop(Group):
    max_age = 18
    min_age = 14



first_a = PrimaryGroup(1,2,3,4)
eleven_a  = HighGroup (154,23,4)
six_a = MediumGrop(114,23,45)

first_a.stady()
eleven_a.move()
six_a.move()
print(six_a.title)
print(first_a.class_room)