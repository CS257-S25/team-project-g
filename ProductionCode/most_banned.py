"""Methods for generating a list of categories with the most banned books"""

from ProductionCode.data import bookban_data


def print_item(item):
    """Helper method for pretty printing items
    Args:
        item ({"field": str, "bans": int}): an item with a field value and number of total bans
    Returns:
        a string with the name of the item and the number of bans
    """
    output = item["field"] + ": " + str(item["bans"])
    return output


def most_banned_districts(limit: int):
    """generates a formatted list of districts with the most bans
    Args:
        limit (int): number of districts
    Returns:
        a formatted list of districts with the most banned books
    """
    most_banned = count_bans(bookban_data, "district")
    most_banned = most_banned[0:limit]
    return map(print_item, most_banned)


def most_banned_states(limit: int):
    """generates a formatted list of states with the most bans
    Args:
        limit (int): number of states
    Returns:
        a formatted list of states with the most banned books
    """
    most_banned = count_bans(bookban_data, "state")
    most_banned = most_banned[0:limit]
    return map(print_item, most_banned)


def most_banned_authors(limit: int):
    """generates a formatted list of authors with the most bans
    Args:
        limit (int): number of authors
    Returns:
        a formatted list of authors with the most banned books
    """
    most_banned = count_bans(bookban_data, "author")
    most_banned = most_banned[0:limit]
    return map(print_item, most_banned)


def most_banned_titles(limit: int):
    """generates a formatted list of titles with the most bans
    Args:
        limit (int): number of titles
    Returns:
        a formatted list of authors with the most banned titles
    """
    most_banned = count_bans(bookban_data, "title")
    most_banned = most_banned[0:limit]
    return map(print_item, most_banned)


def count_bans(ban_data, field):
    """counts the number of bans for each value in the field
    Args:
        ban_data: a list of book bans
        field: the field of ban_data
    Returns:
        a list of objects of the form {"field": str, "bans": int},
        showing the number of bans for each category
    """
    total_bans = {}
    for ban in ban_data:
        field_value = ban[field]
        if field_value not in total_bans:
            total_bans.update({field_value: 1})
        else:
            total_bans[field_value] = total_bans[field_value] + 1
    return top_bans_from_dict(total_bans)


def top_bans_from_dict(total_bans):
    """converts a dict with the number of values per key into a sorted decsending list based on
    value.
    Args:
        total_bans: a dict with keys of categories and values of numbers of bans
    Returns:
        a sorted list of objects of the form {"field": str, "bans": int}
        showing the number of bans for each category
    """
    sorted_bans = []
    for key in sorted(total_bans, key=total_bans.get, reverse=True):
        sorted_bans.append({"field": key, "bans": total_bans[key]})

    return sorted_bans


def main():
    """Main function for informal testing"""
    top_bans = most_banned_titles(10)
    for field in top_bans:
        print(field)


if __name__ == "__main__":
    main()
