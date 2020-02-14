#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # insert tickets into hashtable
    for item in tickets:
        hash_table_insert(hashtable, item.source, item.destination)

    # set location to first val in route array to none
    route[0] = hash_table_retrieve(hashtable, 'NONE')
    # start at second item
    current_index = 1
    #while current index is less than length or array, use prev location to retrieve from hashtable
    for i in range(length):
        if hash_table_retrieve(hashtable, route[current_index - 1]) != 'NONE':
            next_location = hash_table_retrieve(
                hashtable, route[current_index - 1])
            #set location to be the next item in route array
            route[current_index] = next_location
            current_index += 1
        else:
            #if location is None, set location to be the last in the array 
            route[length - 1] = route[current_index - 1]
    return route[:length - 1]

  
