def tickets(people):
    # Variables
    cash = []

    # Main loop
    for person in people:
        change = person - 25

        if change == 75:
            # Variables
            tempList = []
            
            # A little biased here, but when your low on change you would normally tend to keep as much of it as possible.
            change = [[50, 25], [25, 25 , 25]]
            
            # Iterating through each elements of each list and checking to see if 'change' is in 'cash'
            for l in change:
                tempCash = list(cash) # copying cash list to new variable (avoding aliasing)
                count = 0

                for bill in l:
                    if bill not in tempCash:
                        break
                        
                    else:
                        tempCash.remove(bill)
                        count += 1

                if count == len(l):
                    tempList.append(True)
                    cash = list(tempCash) # copying tempCash back to cash
                    cash.append(person)
                    break

            if True not in tempList:
                return "NO"

        elif change == 0:
            cash.append(person)

        elif change in cash:
            cash.append(person)
            cash.remove(change)

        else:
            return "NO"
            
    return "YES"
