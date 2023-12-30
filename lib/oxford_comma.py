def oxford_comma(items):
    item_string = ""
    if len(items) == 1:
        item_string = items[0]
    elif len(items) == 2:
        item_string = items[0] + " and "+ items[1]
    elif len(items) == 3:
        item_string = items[0] + ', ' + items[1]+ ', and '+items[2]
    else:
        counter = 0
        for item in items:
            if len(items) - counter != 1:
                item_string += item + ", "
                counter += 1
            else:
                item_string += "and " + item
        
            
        
    return item_string


