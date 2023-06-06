def return_xml(file_path, data):
    data = {"root": data}
    xml_data = xmltodict.unparse(data)
    with open(file_path, 'w') as file:
        file.write(xml_data)

def json_to_xml(file_path, data):
    x_data = load_json(file_path)
    xml_data = dicttoxml(x_data).decode('utf-8')
    return_xml(data, xml_data)

def yaml_to_xml(file_path, data):
    xml_data = load_yaml(file_path)
    return_xml(data, xml_data)
