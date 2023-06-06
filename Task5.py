def return_yaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def json_to_yaml(file_path, data):
    yaml_data = load_json(file_path)
    return_yaml(data, yaml_data)

def xml_to_yaml(file_path, data):
    yaml_data = load_xml(file_path)
    return_yaml(data, yaml_data)
