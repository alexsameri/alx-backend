
'''module one
'''


def index_range(page, page_size):
    '''Retrieve the index range from a given page and page_size
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
