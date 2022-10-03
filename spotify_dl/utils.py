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
