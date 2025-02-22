
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
    "id": 1,
    "first_name": "Samuel L.",
    "last_name": self.last_name,
    "age": 110,
    "lucky_numbers": [1,2,3,4]
    }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 100)

    def add_member(self, member):
        member["id"]=self._generateId()
        self._members.append(member)
        return self._members
       

    def delete_member(self, id):
        for index in range(0,len(self._members)):
            if self._members[index]["id"]==id:
                del_member = self._members.pop(index)
                return del_member
            
    def update_member(self, id, member):
        saved_id = id
        del_member = None
        for index in range(0,len(self._members)):
            if self._members[index]["id"]==id:
                del_member = self._members.pop(index)
        member["id"]=saved_id
        self._members.append(member)
        return del_member
    

    def get_member(self, id):
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
