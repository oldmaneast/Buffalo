import requests, json

def get_file_system(dir):
    base_url = 'http://62.15.96.45:9000/rpc/ls/'
    r = requests.get(f'{base_url}{dir}').json()
    return_obj = []
    for x in r:
        if x.get('name') == '.' or x.get('name') == '..':
            continue
        if x.get('directory'):
            return_obj.extend(get_file_system(x.get('path')))
        else:
            return_obj.append(x.get('path'))
    return return_obj


out = get_file_system('')