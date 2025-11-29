# მომხმარებელმა შეიყვანოს ტემპერატურა.
# თუ ტემპერატურა მეტია 0-ზე, შიგნით შეამოწმე:

#   თუ მეტია 30-ზე, დაბეჭდე "ცხელა"

#   თუ არა — "ნორმალურია"

# სხვა შემთხვევაში დაუბეჭდე - "ყინვაა"
temperature = int(input("enter any temperature"))
if temperature > 0:
    if temperature > 30:
        print("cxela")
    else:
        print("temperatura nkrmaluria")
else:
    print("yinvaa")
