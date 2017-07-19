## 3.4 - 3.6
## initial guest list of people to invite to dinner
guest_list = ['elon musk', 'bill gates', 'warren buffet']
## printing invitations to dinner (could use a loop but we're not
## quite there in the book)
print(guest_list[0].title() + ", I'd like to invite you to dinner.")
print(guest_list[1].title() + ", I'd like to invite you to dinner.")
print(guest_list[2].title() + ", I'd like to invite you to dinner.")

## one guest can't make it to dinner
print("\n" + guest_list[2].title() + " can't make it to dinner.\n")

## replacing the guest that can't make it with a new one
guest_list[2] = 'granny'
print(guest_list[0].title() + ", I'd like to invite you to dinner.")
print(guest_list[1].title() + ", I'd like to invite you to dinner.")
print(guest_list[2].title() + ", I'd like to invite you to dinner.")

## inform guest we've found a bigger table and invite 3 new guests
print("\nWe've found a bigger table. Let's invite more guests.\n")
guest_list.insert(0,"luke")
guest_list.insert(2,"hoke")
guest_list.insert(4,"joe")


## print invites to all guests
print(guest_list[0].title() + ", I'd like to invite you to dinner.")
print(guest_list[1].title() + ", I'd like to invite you to dinner.")
print(guest_list[2].title() + ", I'd like to invite you to dinner.")
print(guest_list[3].title() + ", I'd like to invite you to dinner.")
print(guest_list[4].title() + ", I'd like to invite you to dinner.")
print(guest_list[5].title() + ", I'd like to invite you to dinner.")

## we can only have 2 guests due to delay in table delivery
print("\nOops, the table won't be here in time. Only two guests are able to come.\n")

## using pop(), uninvite all but 2 guests and print a message to each
## telling that guest they are uninvited
uninvite = guest_list.pop()
print("Sorry " + uninvite.title() + ", you are uninvited to dinner")
uninvite = guest_list.pop()
print("Sorry " + uninvite.title() + ", you are uninvited to dinner")
uninvite = guest_list.pop()
print("Sorry " + uninvite.title() + ", you are uninvited to dinner")
uninvite = guest_list.pop()
print("Sorry " + uninvite.title() + ", you are uninvited to dinner")

## tell the remaining two guests that they're still invited to dinner
print(guest_list[0].title() + " and " + guest_list[1].title() + ", you are still invited to dinner.")


## delete remaining guests from lists and print the empty list
del guest_list[:]
print(guest_list)

