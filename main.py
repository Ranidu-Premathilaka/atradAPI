from atradAPI import AtradAPI

username = "90772"
password = "k@UD7QrmI2L!27y" 

api = AtradAPI(username, password)
api.buy("AAIC.N0000",2,13.2,day=1)

print(api.getUserInfo())
print(api.genDuplicateOrderId())