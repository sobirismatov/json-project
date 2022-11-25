import json

def json_file_to_dict(file_path: str) -> dict:
    '''convert json to dict
    
    Args:
        file_path (str): file path.
        
    Returns:
        dict: dict data
    '''
    data = open(file_path).read()
    data_dict = json.loads(data)

    return data_dict

data_dict = json_file_to_dict('data.json')

def get_number_of_users(data: dict) -> int:
    '''all users' data.
    
    Args:
        data (dict): users data
    
    Returns:
        int: number of all users.
    '''
    return len(data['users'])


def get_all_countries(data: dict) -> list:
    '''all users' data.
    
    Args:
        data (dict): users data
    
    Returns:
        list: list of counrties
    '''
    countries = []
    users = data['users']
    for user in users:
        countries.append(user['country'])
    return countries


def get_all_users_fullname(data: str) -> list:
    '''all users' full name.
    
    Args:
        data (dict): users data
    
    Returns:
        list: list of all users' full name
    '''
    full_names = []
    for user in data['users']:
        full_name = user['first_name'] + ' ' + user['last_name']
        full_names.append(full_name)

    return full_names


def get_user_by_id(data: dict, id: int) -> dict:
    '''get user by id
    
    Args:
        data (dict): users data
        id (int): user id.
        
    Returns:
        dict: user data
    '''
    for user in data['users']:
        if user['id'] == str(id):
            return user
 


def get_user_by_firstname(data: dict, first_name: str) -> dict:
    '''get user by first name
    
    Args:
        data (dict): users data
        first_name (str): user's first name.
        
    Returns:
        dict: user data
    '''
    for user in data['users']:
        if user['first_name'] == first_name:
            return user
    return "does not exist"



def get_user_by_lastname(data: dict, flast_name: str) -> dict:
    '''get user by last name
    
    Args:
        data (dict): users data
        first_name (str): user's last name.
        
    Returns:
        dict: user data
    '''
    for user in data['users']:
        if user['last_name'] == flast_name:
            return user
    return "no"



def get_user_by_country(data: dict, fcountry: str) -> dict:
    '''get user by country
    
    Args:
        data (dict): users data
        country (str): name of user's country.
        
    Returns:
        dict: user data
    '''
    for user in data['users']:
        if user['country'] == fcountry:
            return user
    return "no"

print(get_user_by_country(data_dict, 'China'))

