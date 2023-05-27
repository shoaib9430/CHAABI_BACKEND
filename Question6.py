def get_every_other_sublist(lst, start_index, end_index):
    sub_list = lst[start_index:end_index+1]
    every_other_sub_list = sub_list[1::2]
    return every_other_sub_list

# Example usage
lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = get_every_other_sublist(lst, start_index, end_index)
print(result)
