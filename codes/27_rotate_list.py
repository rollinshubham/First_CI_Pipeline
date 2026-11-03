def rotate_list(items, k):
    if not items:
        return []

    k = k % len(items)

    return items[-k:] + items[:-k] if k != 0 else items[:]