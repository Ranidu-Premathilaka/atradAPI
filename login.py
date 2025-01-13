import requests
import json5

class AtradAPI:
    def __init__(self):
        self.session = requests.Session()
        self.loginStatus = False
        self.userInfo = {}

        self.login_url = "https://online.softlogicstockbrokers.lk/atsweb/login"
        self.order_url = "https://online.softlogicstockbrokers.lk/atsweb/order"

    def sendGetResponse(self,url,params,header=None):
        if header == None:
            header = {"Content-Type":"application/x-www-form-urlencoded"}
        
        rawResponse = self.session.get(url,headers=header,params=params)
        
        if rawResponse.status_code != 200:
            print("Failed to get response")
            return False
    
        dictResponse = self.responseParser(rawResponse)
        return dictResponse

    def sendPostResponse(self,url,data,header=None):
        if header == None:
            header = {"Content-Type":"application/x-www-form-urlencoded"}

        rawResponse = self.session.get(url,headers=header,data=data)

        if rawResponse.status_code != 200:
            print("Failed to get response")
            return False

        dictResponse = self.responseParser(rawResponse)
        return dictResponse

    def responseParser(self,response):
        try:
            dict_response = response.json()
            if(dict_response == None):
                raise Exception("Invalid Json Response")
            return dict_response
        except:
            print("Invalid Json Response. Trying to parse it manually")
            response_content = response.content
            response_content = response_content.decode("utf-8")
            response_content.replace("'",'"')
            try:
                dict_response = json5.loads(response_content)          
                return dict_response
            except:
                print("Couldn't parse json file. Printing response")
                print(response_content)
                return False


    def getUserInfo(self,username):
        print("Fetching cliend Account info")

        params = {
            "action":"getUserDetails",
            "format":"json"
        }

        response = self.sendGetResponse(self.order_url,params)
        
        if response["description"] == "success":
            userInfo = response["data"]["userids"][0]
            if userInfo["username"] == username:
                self.userInfo = userInfo
                return True

        return False



    def login(self,username,password):
        print("Logging in")

        data = {
            "action":"login",
            "format":"json",
            "txtUserName":username,
            "txtPassword":password
        }
        response = self.session.post(self.login_url,data=data)

        if (response == False or response["data"] !="success"):
            self.loginStatus = False
            print("Login failed")
            return False

        if(self.getUserInfo()):
            self.loginStatus = True
            print("Successfully Logged in")
            return True
        else:
            self.loginStatus = False
            print("Failed to fetch user info")
            return False

    #implmenet so that some stocks can be rounded up if the prce isn't rounded up properly 
    #try to reudce the hard codded values
    def buy(self,securityId,quantity,price):
        print("Processing Buy Order")
        securityProperties = self.getSecurityProperties(securityId)
        commision = self.calcCommision(quantity*price)

        if securityProperties:
            print("Security Properties fetched")
        else:
            print("Failed to fetch Security Properties")
            return False

        if commision:
            print("Commision calculated")
        else:
            print("Failed to calculate Commision")
            return False

        data = {
            "action":"submitOrder",
            "market":self.userInfo["exchangeId"],
            "broker":self.userInfo["brokerId"],
            "format":"json",
            "clientOrderId":"",
            "cseOrderId":"",
            "brokerClient":1,
            "orderStatus":securityProperties["tradestatus"],
            "filledQty":"",
            "acntid":self.userInfo["clientacntid"],
            "oldPrice":"",
            "oldQty":"",
            "remainder":"",
            "orderplacedate":"",
            "marketPrice":securityProperties["askprice"],
            "oldDisclose":"",
            "txtContraBroker":"",
            "txtapprovalReason":"",
            "txtsenttoapproval":"no",
            "txtCompId":"",
            "txtOdrStatus":"",
            "duplicateOrderId":"3E58KzgK7y",
            'clientAcc':f"{self.userInfo['clientCode']} ({self.userInfo['initials']} {self.userInfo['lastName']}-{self.userInfo['nic']})",
            "cmbClientAcc_end":"",
            "assetSelect":1,
            "actionSelect":1,
            "txtSecurity":securityId,
            "cmbBoard":1,
            "spnQuantity":quantity,
            "spnPrice":price,
            "spnMinFillQuantity":0,
            "spnDisclose":quantity,
            "cmbOrderType":2,
            "cmbTif":0,
            "cmbTifDays":1,
            "spnYeild":0,
            "spnEffectiveYield":0,
            "hiddenSpnCseFee":0.02,
            "spnCommission":0,
            "txtTradeId":"",
            "brokerClientVal":1,
            "confirm":1
        }
        response = self.session.post(self.order_url,data=data)
        dict_response = self.responseParser(response)

        if dict_response["data"] == "success":
            print("successfully placed the order")
            return True
        else:
            print("Failed to place the order")
            return False

    def quickBuy(self,securityId,quantity):
        print("Quick Buying for the market Value")

    def sell(self,securityId,quantity,price):
        print("Processing Sell Order")

    def quickSell(self,securityId,quantity):
        print("Quick Selling for the market Value")

    def getOrderBook(self,securityId):
        print("Fetching Order Book")
        params = {
            "action":"getOrderBook",
            "format":"json",
            "board":1,
            "security":securityId
        }
        response = self.session.get(self.order_url,params = params)
        dict_response = self.responseParser(response)
        if dict_response["description"] == "success":
            print("successfully fetched Order Book")
            return dict_response["data"]
        else:
            print("Failed to get Order Book ")
            return False

    def getSecurityProperties(self,securityId):
        print("Fetching Security Properties")
        params = {
            "action":"getSecurityProperties",
            "format":"json",
            "txtSecurityId":securityId
        }
        response = self.session.get(self.order_url,params = params)
        dict_response = self.responseParser(response)
        #always success check other attributes
        if dict_response["description"] == "success":
            print("successfully fetched Security properties")
            return dict_response["data"]["SecurityDetail"][0]
        else:
            print("Failed to get Security properties ")
            return False

    def calcCommision(self,orderValue):
        print("Calculating Commision")
        params = {
            "action":"calcCommission",
            "format":"json",
            "orderValue":orderValue,
            "accountType":"normal",
            "broker":self.userInfo["brokerId"],
            "exchange":self.userInfo["exchangeId"]
        }
        response = self.session.get(self.order_url,params = params)
        dict_response = self.responseParser(response)

        if dict_response["description"] == "success":
            print("successfully calculated Commision")
            return dict_response["data"]["commision"]
        else:
            print("Failed to calculate Commision ")
            return False

username = "90772"
password = "k@UD7QrmI2L!27y" 

#bloter
#https://online.softlogicstockbrokers.lk/atsweb/order?action=getBlotterData&format=json&clientAcc=all&exchange=all&ordStatus=all&ordType=all&lstUpdateTime=2024-12-31%2014:47:43&assetClass=all&otherAcc=false&dojo.preventCache=1735636668002

#order cancelation
#https://online.softlogicstockbrokers.lk/atsweb/order?action=cancelOrder&format=json&order=%7B%22cancel%22:%5B%7B%22exchangeid%22:%22CSE%22,%22clientaccountcode%22:%22ARR/90772-LI/0%22,%22securitycode%22:%22AEL.N0000%22,%20%22board%22:%20%22REGULAR%22,%20%22clientorderid%22:%2290772-woV0Ab478%22,%22orderid%22:%2200000%22,%22exchangeorderid%22:%22%22,%22orderplacedate%22:%222024-12-31%2014:47:35%22,%22action%22:%22BUY%22,%22orderstatus%22:%22QUEUED%22%7D%5D%7D&dojo.preventCache=1735636670984


#get order book 
#https://online.softlogicstockbrokers.lk/atsweb/marketdetails?action=getOrderBook&format=json&board=1&security=AAIC.N0000&dojo.preventCache=1735445973386


api = AtradAPI()

api.login(username,password)
api.buy("AEL.N0000",2,10)