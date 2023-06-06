def load_yaml(file_path):
    with open(file_path, 'root') as file:
        return {'root': yaml.safe_load(file)}
