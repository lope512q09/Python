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
