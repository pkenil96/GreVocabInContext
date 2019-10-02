def removeDuplicates(items):
    '''
    :param items:
    :return:
    '''
    unique_list = []
    for item in items:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


def createURL(parentURL, searchKeyword, order, sortBy):
    '''
    :param parentURL:
    :param searchKeyword:
    :param order:
    :param sortBy:
    :return:
    '''
    url = ''
    url = parentURL + '?q=' + searchKeyword + '&order=' + order + '&sort=' + sortBy
    return url
