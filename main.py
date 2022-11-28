import json


def json_file_to_dict(file_path: str) -> dict:
    '''convert json to dict
    
    Args:
        file_path (str): file path.
    Returns:
        dict: dict data
    '''
    dic=json.loads(file_path)
    dic = dic["users"]
    return dic
f =open("data.json")
file_path=f.read()

print(json_file_to_dict(file_path))


# assign dictionary from json_file_to_dict to data

def get_number_of_users(data: dict) -> int:
    '''all users' data.
    
    Args:
        data (dict): users data
    
    Returns:
        int: number of all users.
    '''
    dic=json.loads(data)
    dic =dic["users"]
    return len(dic)
f=open("data.json")
data=f.read()
print(get_number_of_users(data))


def get_all_countries(data: dict) -> list:
    '''all users' data.
    
    Args:
        data (dict): users data
    
    Returns:
        list: list of counrties
    '''
    dic=json.loads(data)
    dic=dic["users"]
    m=[]
    for i in dic:
        m.append(i["country"])
    return m
f = open("data.json")
data=f.read()
print(get_all_countries(data))


def get_all_users_fullname(data: str) -> list:
    '''all users' full name.
    
    Args:
        data (dict): users data
    
    Returns:
        list: list of all users' full name
    '''
    dic=json.loads(data)
    dic=dic["users"]
    m=[]
    for i in dic:
        m.append(i["first_name"])
    return m

f=open("data.json")
data=f.read()
print(get_all_users_fullname(data))
def get_user_by_id(data: dict, id: int) -> dict:
    '''get user by id
    
    Args:
        data (dict): users data
        id (int): user id.
        
    Returns:
        dict: user data
    '''
    dic=json.loads(data)
    dic=dic["users"]
    m=[]
    for i in dic:
        m.append(i["id"])
    return m
f=open("data.json")
data=f.read()


def get_user_by_firstname(data: dict, first_name: str) -> dict:
    '''get user by first name
    
    Args:
        data (dict): users data
        first_name (str): user's first name.
        
    Returns:
        dict: user data
    '''
    dic=json.loads(data)
    dic=dic["users"]
    m=[]
    n=[]
    for i in dic:
        m.append(i["id"])
        n.append(i["first_name"])
    k=dic(zip(m,n))
    return k
f =open("data.jsosn")
data=f.read()


def get_user_by_lastname(data: dict, flast_name: str) -> dict:
    '''get user by last name
    
    Args:
        data (dict): users data
        first_name (str): user's last name.
        
    Returns:
        dict: user data
    '''
    dic=json.loads(data)
    dic=dic["users"]
    m=[]
    n=[]
    for i in  dic:
        m.append(i["id"])
        n.append(i["last_name"])
    k=dict(zip(m,n))
    return k
f=open("data.json")
data=f.read()


def get_user_by_country(data: dict, fcountry: str) -> dict:
    '''get user by country
    
    Args:
        data (dict): users data
        country (str): name of user's country.
        
    Returns:
        dict: user data
    '''
    dic=json.loads(data)
    dic=dic["user"]
    m=[]
    n=[]
    for i in dic:
        m.append(i["id"])
        n.append(i["country"])
    k=dict(zip(m,n))
    return k
f=open("data.json")
data=f.read()
print(get_user_by_country(data))