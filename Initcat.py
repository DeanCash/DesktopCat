import os

def load_init(file_path: str):
    if (not os.path.isfile(file_path)) or (not file_path.endswith('.ini')):
        raise Exception(f"'{file_path}' is not and .ini file or doesn't exist")

    with open(file_path, "r") as f: settings = f.readlines()
    pairs = {}
    for line in settings:
        try:
            key, value = line.split('=')
        except ValueError: continue
        
        if key.isspace() or key == "": continue
        # exclude comment lines too
        if key.strip().startswith(';'): continue
        # built-in boolean conversion
        temp_value = value.lower()
        if (temp_value == "true") or (temp_value == "false"):
            pairs[key] = True if temp_value == "true" else False if temp_value == "false" else -1
            continue
        pairs[key] = value.strip()
    return pairs


if __name__ == "__main__":
    import pprint
    data = load_init('sample.ini')
    pprint.pprint(data)
