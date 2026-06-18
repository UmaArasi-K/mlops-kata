def group_transactions( transactions: list[dict])->dict[str,float]:
    """Given a list of {"user": str, "amount": float}, return {user: total}."""
    result={}
    for item in transactions:
        user, amount = item["user"],item["amount"]
        result[user]=result.get(user,0)+amount
    return result


if __name__ == "__main__":
    sample_transactions=[
        { "user":"alex","amount": 50.3},
        { "user":"alex", "amount":50.3},
        { "user":"Kate", "amount":20},
        { "user":"alex","amount":50.8},
        { "user":"Ode", "amount": 500.7},
        { "user":"Kate", "amount":105.3},
        { "user":"alex", "amount":36.9}]
    print(group_transactions(sample_transactions))
