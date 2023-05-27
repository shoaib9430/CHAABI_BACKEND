def get_file_types(extension_type_list, file_list):
    file_types = {}
    extension_type_pairs = extension_type_list.split(';')
    
    for file in file_list:
        if '.' in file:
            extension = file.split('.')[-1]
            for pair in extension_type_pairs:
                ext, file_type = pair.split(',')
                if ext == extension:
                    file_types[file] = file_type
                    break
            else:
                file_types[file] = "unknown"
        else:
            file_types[file] = "unknown"
    
    return file_types

# Example usage
extension_type_list = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
file_list = ["abc.jpg", "xyz.xls", "text.csv", "123"]

result = get_file_types(extension_type_list, file_list)
print(result)
