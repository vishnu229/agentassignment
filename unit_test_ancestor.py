from findAncestor import *

"""
common ancestor for  1 and 4  is  1
common ancestor for  2 and 8  is  6
No Common Ancestor for 1 and 9
common ancestor for  1 and 10  is  7
"""

def test_case1():
        id_dict = get_dataset()
        assert find_common_ancestor(id_dict,'1','4') ==  '1'
def test_case2():
        id_dict = get_dataset()
	assert find_common_ancestor(id_dict,'2','8') ==  '6'
def test_case3():
        id_dict = get_dataset()
        assert find_common_ancestor(id_dict,'1','9') ==  None
def test_case4():        
        id_dict = get_dataset()
	assert find_common_ancestor(id_dict,'1','10') ==  '7'
