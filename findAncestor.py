file = open("input_dataset.txt", "r") 
input_dataset_list = file.readlines()
id_dict = {}
class Node:
     def __init__(self,father_id,mother_id):
        self.father_id = father_id
        self.mother_id = mother_id

def populate_parent_set(id_dict,id1,parent_set):
    """
      function finds path from id to root element  and nodes to parent set 
      input:
       id_dictionary - input dataset
       id1 - id of the node for which tree constructed
       parent_set - contains path from node to root element 
      output :
         return parent_set 
    """
    # current Node value is None base case
    if id1 == None:
       return parent_set
    # add node to parent set
    parent_set.add(id1)
    try:
        # call father parent of the id
    	parent_set = populate_parent_set(id_dict,id_dict[id1].father_id,parent_set)
        # call mother parent of the id
        parent_set = populate_parent_set(id_dict,id_dict[id1].mother_id,parent_set)
    except KeyError:
        """
           reached root node with no parent
        """
    return parent_set

def find_ancestor(id_dict,id2,parent_set,found_out):
    """
      finds if the nodes in the path of id2 to root  is in parent_set of id1  while traversing from id2 to root element 
    """ 
    # if id2 in id1 parent set we found common ancestor returns its value
    if id2 in parent_set:
       return id2
    
    #base case 
    if id2 == None:
       return None  
    try:
        # call recursively father parent
        found_out = find_ancestor(id_dict,id_dict[id2].father_id,parent_set,found_out)
        # call mother parent recursively if you havent found answer
        if found_out == None:
        	found_out = find_ancestor(id_dict,id_dict[id2].mother_id,parent_set,found_out)
    except KeyError:
        """
           reached root with no parent
        """
    return found_out
 
def find_common_ancestor(id_dict,id1,id2):
    parent_set = set()
    parent_set = populate_parent_set(id_dict,id1,parent_set) 
    ancestor =  find_ancestor(id_dict,id2,parent_set,None)
    if (ancestor == None):
       print "No Common Ancestor for",id1,"and",id2
    else:
       print "common ancestor for ",id1,"and",id2," is ",ancestor
    return ancestor 
def get_dataset():
    file = open("input_dataset.txt", "r")
    input_dataset_list = file.readlines()
    id_dict = {}
    for item in input_dataset_list:
    	 item = item.rstrip()
     	 id_list = item.split()
     	 my_id  =  id_list[0]
         father_id = id_list[1]
         mother_id = id_list[2]
     	 if father_id == "-":
            father_id = None
         if mother_id == "-":
            mother_id = None
         node = Node(father_id,mother_id)
         id_dict[my_id]=node
    return id_dict
if __name__== "__main__":
    id_dict = get_dataset()
    find_common_ancestor(id_dict,'1','4')
    find_common_ancestor(id_dict,'2','8')
    find_common_ancestor(id_dict,'1','9') 
    find_common_ancestor(id_dict,'1','10')  
