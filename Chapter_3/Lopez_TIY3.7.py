dinner_guests = ['Kanye West', 'Aries', 'Derek Jeter']
print(f"\nI invite you to dinner, {dinner_guests[0]}.")
print(f"\nWould you like to come to a dinner party {dinner_guests[1]}?")
print(f"\n{dinner_guests[2]}, would you like to go to dinner?")
canceled_guest = dinner_guests.pop(-1)
print(f"\n\tDarn, it looks like {canceled_guest} can't make it.")
new_guest = dinner_guests.append('J. Cole')
print(f"\nI invite you to dinner, {dinner_guests[0]}.")
print(f"\nWould you like to come to a dinner party {dinner_guests[1]}?")
print(f"\n{dinner_guests[2]}, would you like to go to dinner?")
print("\n\n\tEveryone, we have found a bigger table!")
dinner_guests.insert(0,'Jose Altuve')
dinner_guests.insert(2,'Jay-Z')
dinner_guests.insert(5,'Drake')
print(f"\nLet's get some dinner {dinner_guests[0]}.")
print(f"\nI invite you to dinner {dinner_guests[1]}.")
print(f"\nWould you like to come to a dinner party {dinner_guests[3]}?")
print(f"\nHow about we get some grub {dinner_guests[2]}")
print(f"\n{dinner_guests[4]}, would you like to go to dinner?")
print(f"\nLet's hit up a burger joint {dinner_guests[5]}.")
print("\n\tOh no, it looks like we only have room for two people now.")
print(f"\nI'm terribly sorry {dinner_guests.pop(5)}, but we will have to cancel.")
print(f"\nI'm terribly sorry {dinner_guests.pop(4)}, but we will have to cancel.")
print(f"\nI'm terribly sorry {dinner_guests.pop(2)}, but we will have to cancel.")
print(f"\nI'm terribly sorry {dinner_guests.pop(0)}, but we will have to cancel.")
print(f"\nGood news {dinner_guests[0]} and {dinner_guests[1]}, we can still go to dinner!")
del dinner_guests[0]
del dinner_guests[1]
print(dinner_guests)