def load_xml(file_path):
    with open(file_path) as file:
        return xmltodict.parse(file).getroot()
