def convert_to_int_dict(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        try:
            str_key = str(key)
            new_key = int(str_key)            
            try:
                new_value = int(value)
                new_dict[new_key] = new_value
            except ValueError:
                pass
        except ValueError:
            pass
    return new_dict
# Contoh penggunaan
input_dict = {'1': '10', '2': '20', '3': 'abc', 'xyz': '30'}
output_dict = convert_to_int_dict(input_dict)
print(output_dict)
