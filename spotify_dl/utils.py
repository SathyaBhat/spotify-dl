def sanitize(name):
    """
    Removes some of the reserved characters from the name so it can be saved
    :param name: Name to be cleaned up
    :return string containing the cleaned name
    """
    clean_up_list = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|", "\0"]
    return "".join(c for c in name if c not in clean_up_list)
