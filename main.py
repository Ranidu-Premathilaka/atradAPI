from atradAPI import AtradAPI

username = "90772"
password = "k@UD7QrmI2L!27y" 

api = AtradAPI(username, password)

print(api.getUserInfo())
print(api.genDuplicateOrderId)