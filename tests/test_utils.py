from eule import utils

delimited_sort = utils.delimited_sort
keyfy = utils.keyfy
non_empty_sets_keys = utils.non_empty_sets_keys
reduce_ = utils.reduce_
unique = utils.unique

# define the tests
def test_keyfy():
    '''
    tests the key string generation
    '''
    assert keyfy([1, 2, 3]) == '1,2,3'


def test_one_set_euler():
    '''
    tests the reduce function
    '''
    assert reduce_(lambda a, b: a+b, [1, 2], 0) == 3


def test_unique_elems():
    '''
    tests the reduce function
    '''
    assert unique([1, 2, 3, 3]) == [1, 2, 3]


def test_delimited_sort():
    '''
    tests sorting delimited by token
    '''
    assert delimited_sort('4,1,2,3', ',') == '1,2,3,4'


def test_non_empty_sets_keys():
    '''
    tests dict clean with empty values
    '''
    assert non_empty_sets_keys({'a': [1, 2, 3], 'b': []}) == ['a']
