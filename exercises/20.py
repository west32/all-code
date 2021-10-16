

def dict_with_counted_elements_from_txt_file(file_name):

    def read_file(file_name):
        with open(file_name,"r",encoding='utf-8') as open_file:
            data= open_file.read()
            return(data)


    def pop_uniques(data):
        set_elements=set()
        for element in data.replace("\n",",").split(","):
            set_elements.add(element)
        return list(set_elements)


    def list_of_elements(data):
        names_list=[]
        for  name in data.replace("\n",",").split(","):
            names_list.append(name)
        return names_list


    def dict_with_keys(uniques):
        dict_with_keys={}
        for unique in uniques:
            dict_with_keys[unique]=0
        return dict_with_keys


    def dict_with_keys_and_counted_values(elements_list,keys_dict):
        keys = list(keys_dict.keys())
        for key in keys:
            for element in elements_list:
                if element == key:
                    keys_dict[key] += 1
        return keys_dict


    data= read_file("nameslist.txt")
    uniques= pop_uniques(data)
    names_list= list_of_elements(data)
    keys_dict=dict_with_keys(uniques)
    final_dict=dict_with_keys_and_counted_values(names_list,keys_dict)
    print(final_dict)
    return final_dict

if __name__=="__main__":
    dict_with_counted_elements_from_txt_file(file_name="nameslist.txt")



