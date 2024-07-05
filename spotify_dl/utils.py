import Levenshtein


def get_closest_match(results, expected) -> str:
    """
    Returns closest matching result based on Levenshtein edit distance.
    """
    best_r = ""
    min_distance = float('inf')
    for r in results:
        curr_distance = Levenshtein.distance(r, expected)
        if (curr_distance < min_distance):
            min_distance = curr_distance
            best_r = r
    return best_r


def sanitize(name, replace_with=""):
    """
    Removes some of the reserved characters from the name so it can be saved
    :param name: Name to be cleaned up
    :return string containing the cleaned name
    """
    clean_up_list = ["\\", "/", ":", "*", "?", '"', "<", ">", "|", "\0", "$", "\""]
    for x in clean_up_list:
        name = name.replace(x, replace_with)
    return name
