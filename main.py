def add_setting(add_dict,add_tuple):
    key,value = add_tuple
    key = key.lower()
    value = value.lower()
    if key in add_dict.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    add_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(update_dict,update_tuple):
    key,value = update_tuple
    key = key.lower()
    value = value.lower()
    if key in update_dict.keys():
        update_dict.update({key:value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(del_dict, key):
    key = key.lower()
    if key in del_dict.keys():
        del_dict.pop(key,None)
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"
def view_settings(view_dict):
    output=''
    if not view_dict:
        return 'No settings available.'
    for key, value in view_dict.items():
        output += f"{key.capitalize()}:"+f" {value}\n"
    return f"Current User Settings:\n"+output

test_settings ={
    'theme': 'dark',
    'notifications': 'enabled',
    'Volume': 'high'
}
test_tuple =('theme','dark')

print(view_settings(test_settings))