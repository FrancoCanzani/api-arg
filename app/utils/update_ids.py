def update_ids(data):
    for index, item in enumerate(data):
        item["id"] = index + 1
    return data