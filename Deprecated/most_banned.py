"""Methods for generating a list of categories with the most banned books"""

from ProductionCode.data import bookban_data


def format_item(item):
    """Helper method for pretty formatting items
    Args:
        item ({"field": str, "bans": int}): an item with a field value and number of total bans
    Returns:
        a string with the name of the item and the number of bans
    """
    output = item["field"] + ": " + str(item["bans"])
    return output


def format_list(ban_list):
    """Helper method for pretty formatting lists
    Args:
        item (list[{"field":str, "bans": int}]): a list of items with a field value
        and number of total bans
    Returns:
        a list of strings with the name of the item and the number of bans
    """
    return map(format_item, ban_list)


def limit_results(ban_list, max_results):
    """Returns the first {max_results} elements of a list
    Args:
        list (list): list to be limited
        max_results (int): number of results
    Returns:
        the first {max_results} elements of a list
    """
    return ban_list[0:max_results]


def most_banned_districts(max_results: int):
    """generates a formatted list of districts with the most bans
    Args:
        max_results (int): number of districts
    Returns:
        a formatted list of districts with the most banned books
    """
    most_banned = count_bans(bookban_data, "district")
    limit_bans = limit_results(most_banned, max_results)
    format_results = format_list(limit_bans)

    return format_results


def most_banned_states(max_results: int):
    """generates a formatted list of states with the most bans
    Args:
        max_results (int): number of states
    Returns:
        a formatted list of states with the most banned books
    """
    most_banned = count_bans(bookban_data, "state")
    limit_bans = limit_results(most_banned, max_results)
    format_results = format_list(limit_bans)

    return format_results


def most_banned_authors(max_results: int):
    """generates a formatted list of authors with the most bans
    Args:
        max_results (int): number of authors
    Returns:
        a formatted list of authors with the most banned books
    """
    most_banned = count_bans(bookban_data, "author")
    limit_bans = limit_results(most_banned, max_results)
    format_results = format_list(limit_bans)

    return format_results


def most_banned_titles(max_results: int):
    """generates a formatted list of titles with the most bans
    Args:
        max_results (int): number of titles
    Returns:
        a formatted list of authors with the most banned titles
    """
    most_banned = count_bans(bookban_data, "title")
    limit_bans = limit_results(most_banned, max_results)
    format_results = format_list(limit_bans)

    return format_results


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


# def main():
#     """Main function for informal testing"""
#     top_bans = most_banned_titles(10)
#     for field in top_bans:
#         print(field)


# if __name__ == "__main__":
#     main()
