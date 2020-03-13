# This is python program to understand shallow and deep copy concept.


# old_list = [1,2,3,4,5]
# print("old list: ",old_list)
# new_list = old_list
# print("new list:",new_list)
 
# new_list[2] = 66
# print("after change old list:",old_list)
# print("after change new list:",new_list)

# print("old list:",id(old_list))
# print("new list:",id(new_list))
####################################################

# import copy as c
# old_list = [1,2,3,4,5]
# print("old list: ",old_list)
# new_list = c.copy(old_list)
# print("new list:",new_list)

# new_list[2] = 66
# print("after change old list:",old_list)
# print("after change new list:",new_list)

# print("old list:",id(old_list))
# print("new list:",id(new_list))
######################################################

# old_nested_list = [1,2,3,[10,20],4,5]
# print("old nested list:",old_nested_list)
# new_nested_list  = old_nested_list
# print("new nested list:",new_nested_list)

# new_nested_list[3][1] = 200
# print("after change old nested list:",old_nested_list)
# print("after change new nested list:",new_nested_list)

# print("old nested list:",id(old_nested_list))
# print("new nested list:",id(new_nested_list))
########################################################

# import copy as c
# old_nested_list = [1,2,3,[10,20],4,5]
# print("old nested list:",old_nested_list)
# new_nested_list  = c.deepcopy(old_nested_list)
# print("new nested list:",new_nested_list)
# # suppose
# new_nested_list[3][1] = 200
# print("after change old nested list:",old_nested_list)
# print("after change new nested list:",new_nested_list)

# print("old nested list:",id(old_nested_list))
# print("new nested list:",id(new_nested_list))
########################################################