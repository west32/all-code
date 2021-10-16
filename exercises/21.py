def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as open_file:
        data = open_file.read()
        return (data)

def read_file_by_lines(file_name):
    with open(file_name, "r", encoding='utf-8') as open_file:
        lines= open_file.readlines()
        return lines


def pop_uniques(data):
    set_elements = set()
    for element in data.replace("\n", ",").split(","):
        set_elements.add(element)
    return list(set_elements)

def pop_uniques_by_lines(data):
    set_elements= set()
    for line in data:
        set_elements.add(line.split("/")[2])
    return list(set_elements)

def list_of_all_elements(data):
    all_elements_list = []
    for name in data.replace("\n", ",").split(","):
        all_elements_list.append(name)
    return all_elements_list

def list_of_keys_by_lines(data):
    keys_list=[]
    for line in data:
        keys_list.append(line.split("/")[2])
    return keys_list


def dict_with_keys(uniques):
    dict_with_keys = {}
    for unique in uniques:
        dict_with_keys[unique] = 0
    return dict_with_keys


def dict_with_keys_and_counted_values(all_elements_list, keys_dict):
    keys = list(keys_dict.keys())
    for key in keys:
        for element in all_elements_list:
            if element == key:
                keys_dict[key] += 1
    return keys_dict


data = read_file_by_lines("solarsystem.txt")
unique_keys_list = pop_uniques_by_lines(data)
all_keys_list = list_of_keys_by_lines(data)
keys_dict = dict_with_keys(unique_keys_list)
final_dict=dict_with_keys_and_counted_values(all_keys_list,keys_dict)
print(final_dict)






# uniques = pop_uniques(data)
# names_list = list_of_elements(data)
# keys_dict = dict_with_keys(uniques)
# final_dict = dict_with_keys_and_counted_values(names_list, keys_dict)
# print(final_dict)
