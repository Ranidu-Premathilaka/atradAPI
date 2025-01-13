import requests
import json5

class AtradAPI:
    def __init__(self):
        self.session = requests.Session()
        self.loginStatus = False
        self.userInfo = {}
        self.marketDetails = {}
        self.allSecurity = []
        self.bookDefId = 1
        self.tickerId = "0"
        
        #in getSecurityProperties there's the attibute on what market it is. 
        # thus you could fetch the proper one from market details
        self.boardId
        self.accountType = "normal"
        self.cseFee 

        self.login_url = "https://online.softlogicstockbrokers.lk/atsweb/login"
        self.order_url = "https://online.softlogicstockbrokers.lk/atsweb/order"
        self.watch_url = "https://online.softlogicstockbrokers.lk/atsweb/watch"
        self.market_url= "https://online.softlogicstockbrokers.lk/atsweb/market"
        self.marketdetails_url= "https://online.softlogicstockbrokers.lk/atsweb/marketdetails"

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

    def getMarketDetails(self):
        exchangeId = self.userInfo["exchangeId"]
        params = {
            "action":"getMarketDetails",
            "format":"json",
            "market":exchangeId
        }

        response = self.sendGetResponse(self.order_url,params)
        if response["description"] == "success":
            self.marketDetails = response["data"]["market"]
            self.boardId = self.marketDetails[0]["assets"][0]["code"]

            return True
        else:
            return False
    
    def getOrderRestrictions(self):
        print("Fetching Order Restrictions")

        params = {
            "action":"getOrderRestrictions",
            "format":"json",
            "clientAcc":self.userInfo["clientCode"],
            "exchange":self.userInfo["exchangeId"],
            "broker":self.userInfo["brokerId"],
            "clientAnctId":self.userInfo["clientacntid"],
            "security":""
        }

        response = self.sendGetResponse(self.order_url,params)
        if response["description"] == "success":
            print("successfully fetched Order Restrictions")
            return response["data"]["orderlimits"]
        else:
            print("Failed to get Order Restrictions ")
            return False
        
    def getMarketStatus(self,securityId):
        print("Fetching Market Status")

        params = {
            "action":"getMarketStatus",
            "format":"json",
            "securityid":securityId,
            "bordId":self.boardId,
            "exchange":self.userInfo["exchangeId"]
        }

        response = self.sendGetResponse(self.order_url,params)
        if response["description"] == "success":
            print("successfully fetched Market Status")
            return response["data"]
        else:
            print("Failed to get Market Status ")
            return False
    
    def getSecurityProperties(self,securityId):
        print("Fetching Security Properties")
        params = {
            "action":"getSecurityProperties",
            "format":"json",
            "txtSecurityId":securityId
        }

        response = self.sendGetResponse(self.order_url,params)

        #always success check other attributes
        if response["description"] == "success":
            print("successfully fetched Security properties")
            return response["data"]["SecurityDetail"][0]
        else:
            print("Failed to get Security properties")
            return False

    def getOrderRestrictions(self,securityId):
        print("Fetching Order Restrictions")

        params = {
            "action":"getOrderRestrictions",
            "format":"json",
            "clientAcc":self.userInfo["clientCode"],
            "exchange":self.userInfo["exchangeId"],
            "broker":self.userInfo["brokerId"],
            "clientAnctId":self.userInfo["clientacntid"],
            "security":securityId
        }

        response = self.sendGetResponse(self.order_url,params)
        if response["description"] == "success":
            print("successfully fetched Order Restrictions")
            return response["data"]["orderlimits"]
        else:
            print("Failed to get Order Restrictions ")
            return False

    def calcCommision(self,orderValue):
        print("Calculating Commision")

        params = {
            "action":"calcCommission",
            "format":"json",
            "orderValue":orderValue,
            "accountType":self.accountType,
            "broker":self.userInfo["brokerId"],
            "exchange":self.userInfo["exchangeId"]
        }
        response = self.session.get(self.order_url,params)

        if response["description"] == "success":
            print("successfully calculated Commision")
            return response["data"]["commision"][0]
        else:
            print("Failed to calculate Commision")
            return False

    def getAllSecurities(self):
        print("Fetching All Securities")

        params = {
            "action":"getAllSecurities",
            "format":"json",
            "exchange":self.userInfo["exchangeId"]
        }

        response = self.sendGetResponse(self.watch_url,params)
        if response["description"] == "success":
            print("successfully fetched All Securities")
            return response["data"]["items"]
        else:
            print("Failed to get All Securities ")
            return False

    def getWatchForSecurity(self,securityId):
        print("Fetching Watch for Security")

        params = {
            "action":"getWatchForSecurity",
            "format":"json",
            "security":securityId,
            "exchange":self.userInfo["exchangeId"],
            "bookDefId":self.bookDefId
        }

        response = self.sendGetResponse(self.watch_url,params)
        if response["description"] == "success":
            print("successfully fetched Watch for Security")
            return response["data"]
        else:
            print("Failed to get Watch for Security ")
            return False
        
    def getTickerData(self):
        print("Fetching Ticker Data")

        params = {
            "action":"getTickerData",
            "format":"json",
            "tickerId":self.tickerId
        }

        response = self.sendGetResponse(self.market_url,params)
        if response["description"] == "success":
            print("successfully fetched Ticker Data")
            return response["data"]["ticker"]
        else:
            print("Failed to get Ticker Data ")
            return False

    def getCSEFeesForDebt(self):
        print("Fetching CSE Fees for Debt")

        params = {
            "action":"getCSEFeesForDebt",
            "format":"json"
            "market":self.userInfo["exchangeId"]
        }

        response = self.sendGetResponse(self.marketdetails_url,params)
        if response["description"] == "success":
            print("successfully fetched CSE Fees for Debt")
            self.cseFee = response["data"]["cseFees"].split(",")[0]
        else:
            print("Failed to get CSE Fees for Debt ")
            return False

    def getOrderBook(self,securityId):
        print("Fetching Order Book")

        params = {
            "action":"getOrderBook",
            "format":"json",
            "board":self.boardId,
            "security":securityId
        }
        response = self.sendGetResponse(self.marketdetails_url,params)

        if response["description"] == "success":
            print("successfully fetched Order Book")
            return response["data"]["orderbook"][0]
        else:
            print("Failed to get Order Book ")
            return False


    def checkUserSession(self):
        params = {
            "action":"checkUserSession",
            "format":"json",
            "txtUserName":self.userInfo["username"]
        }

        response = self.sendGetResponse(self.login_url,params)
        if response["description"] == "success" and response["data"]["validation"][0] == "true":
            print("User Session is active")
            return True
        else:
            print("User Session is inactive")
            return False

    #def checkBuyDisable(self):
    #def getAvlSahres(self):
    #def getBlotterData(self):
    #def getSectorData(self):
    #def getCustomWatches(self):
    #def getOrderStatuses(self):
    #def getPriceChange(self):

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
username = "90772"
password = "k@UD7QrmI2L!27y" 

#bloter
#https://online.softlogicstockbrokers.lk/atsweb/order?action=getBlotterData&format=json&clientAcc=all&exchange=all&ordStatus=all&ordType=all&lstUpdateTime=2024-12-31%2014:47:43&assetClass=all&otherAcc=false&dojo.preventCache=1735636668002

#order cancelation
#https://online.softlogicstockbrokers.lk/atsweb/order?action=cancelOrder&format=json&order=%7B%22cancel%22:%5B%7B%22exchangeid%22:%22CSE%22,%22clientaccountcode%22:%22ARR/90772-LI/0%22,%22securitycode%22:%22AEL.N0000%22,%20%22board%22:%20%22REGULAR%22,%20%22clientorderid%22:%2290772-woV0Ab478%22,%22orderid%22:%2200000%22,%22exchangeorderid%22:%22%22,%22orderplacedate%22:%222024-12-31%2014:47:35%22,%22action%22:%22BUY%22,%22orderstatus%22:%22QUEUED%22%7D%5D%7D&dojo.preventCache=1735636670984


#get order book 
#https://online.softlogicstockbrokers.lk/atsweb/marketdetails?action=getOrderBook&format=json&board=1&security=AAIC.N0000&dojo.preventCache=1735445973386

