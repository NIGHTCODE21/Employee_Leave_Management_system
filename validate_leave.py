def check_leave_balance(balance, requested):

    if requested <= 0:
        return False

    if requested > balance:
        return False

    return True


print(check_leave_balance(10, 5))