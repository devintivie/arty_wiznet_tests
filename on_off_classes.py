
def on_off_to_string(setting):
    if isinstance(setting, bool):
        if setting:
            return 'on'
        return 'off'
    raise TypeError("Requires boolean")
    

def string_to_on_off(string):
    if string.lower() == 'on':
        return True
    return False
# class on_off_string:
#     def __init__(self, iString):
#         if iString.lower == 'on':
#             return True
#         else:
#             return False

# class on_off_bool:
#     def __init__(self, setting):
#         super().__init__()
