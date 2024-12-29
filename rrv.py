import random

# initialize empty slots on a revolver
slots = [0] * 6
for slot in slots:
    print(slot, end=" ")
print()

selected_slot_index = random.randrange(len(slots))
print(selected_slot_index)

slots[selected_slot_index] = 1
print(slots)



