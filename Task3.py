def return_json(file_path, data):
    with open(file_path, "w") as file:
        file.write(json.dumps(data))

def xml_to_json(file_path, data):
    json_data = load_xml(file_path)
    return_json(data, json_data)

def yaml_to_json(file_path, data):
    json_data = load_yaml(file_path)
    return_json(data, json_data)
