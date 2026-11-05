def request_leave(balance, requested):
    if requested <= 0:
        return "Invalid Request"

    if requested <= balance:
        return "Leave Request Submitted"

    return "Insufficient Leave Balance"