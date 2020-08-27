def checkRules(n, cell):
    if cell == 1 and n < 2:
        return 0
    elif cell == 1 and (n == 3 or n == 2):
        return 1
    elif cell == 1 and n > 3:
        return 0
    elif cell == 0 and n == 3:
        return 1
    else:
        return cell
