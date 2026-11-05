def check_leave_balance(balance, requested):
    if requested <= 0:
        return "Invalid leave request"

    if requested <= balance:
        return "Leave Approved"

    return "Insufficient Leave Balance"


print(check_leave_balance(10, 3))