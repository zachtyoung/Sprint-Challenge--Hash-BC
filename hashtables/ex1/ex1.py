#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for x in range(length):
        # Target is what we need to equal the weight limit
        target = limit - weights[x]
        value = hash_table_retrieve(ht, target)
        # Check if a key with value of target exists in the hash table. If it does, then we have 2 matching items. Then sort.
        if value is not None:
            if value > x:
                return (value, x)
            else:
                return (x, value)

        # weight = key, index = value
        hash_table_insert(ht, weights[x], x)
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
