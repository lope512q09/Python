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
