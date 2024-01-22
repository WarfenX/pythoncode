def split_integer(number,parts):

    whole_number, remainder = divmod(number,parts)
    print ("whole number ", whole_number, " remainder ", remainder  )

    whole_number_slots = parts - remainder

    # Create array of whole_numbers to the size of whole_number_slots
    myoutput = whole_number * [whole_number_slots]
    myremainders = remainder * [whole_number + 1]
    
    return myoutput + myremainders
    

print("result =", split_integer(7,3))
print("result =", split_integer(10,2))
print("result =", split_integer(10,4))