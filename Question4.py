def switch_key_value(dictionary):
    return {value: key for key, value in dictionary.items()}

# Example usage
dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

result = switch_key_value(dictionary)
print(result)
