def delete_nth(order, max_e):
    clean_order = []

    for x in order:
        if clean_order.count(x) < max_e:
            clean_order.append(x)
    return clean_order