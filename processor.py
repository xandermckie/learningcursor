def filter_items(items, query):
    if not query:
        return items
    return [item for item in items if query.lower() in str(item).lower()]

def sort_items(items, key, reverse=False):
    return sorted(items, key=lambda x: x.get(key, ""), reverse=reverse)