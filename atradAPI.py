import requests
import json5
import random

class AtradAPI:
    def __init__(self,username,password):
        self.login_url = "https://online.softlogicstockbrokers.lk/atsweb/login"
        self.order_url = "https://online.softlogicstockbrokers.lk/atsweb/order"
        self.watch_url = "https://online.softlogicstockbrokers.lk/atsweb/watch"
        self.market_url= "https://online.softlogicstockbrokers.lk/atsweb/market"
        self.marketdetails_url= "https://online.softlogicstockbrokers.lk/atsweb/marketdetails"

        self.userInfo = {}
        self.allSecurity = []
        self.orderType = {}
        self.tif = {}
        self.boardId = 0
        self.cseFee = 0

        self.username = username
        self.password = password

        self.loginStatus = False
        self.bookDefId = 1
        self.tickerId = "0"
        self.accountType = "normal"

        self.session = requests.Session()

        if not self.login(username,password):
            print("Failed to login")
            raise Exception("Invalid Credentials") 
        
        if not self.initVariables():
            print("Failed to initialize variables")
            raise Exception("Failed to initialize variables")
        
        print("Successfully Initialized and Logged In")


    def initVariables(self):
        userInfo = self.getUserInfo()
        if (not userInfo) or (userInfo["username"] != self.username):
            print("Failed to get User Info")
            return False
        self.userInfo = userInfo 

        marketDetails = self.getMarketDetails() 
        if not marketDetails:
            print("Failed to get Market Details")
            return False

        #in getSecurityProperties there's the attibute on what market it is. 
        # thus you could fetch the proper one from market details
        #setting the board it to equity market
        self.boardId = marketDetails[0]["assets"][0]["code"]

        #setting up local local to be the default broker
        self.brokerclientval = marketDetails[1]["brokerclient"][0]["value"]

        #setting up the order type with the values (limit,market,stop)
        for order in marketDetails[2]["ordertype"]:
                self.orderType[order["name"]] = order["value"]

        #setting up the tif with the values (day,gtc...)
        for tif in marketDetails[3]["tif"]:
            self.tif[tif["name"]] = {"value":tif["value"],"days":[]}
            for day in tif["days"]:
                self.tif[tif["name"]]["days"].append(int(day["day"]))


        allSecurity = self.getAllSecurities()
        if not self.allSecurity:
            print("Failed to get All Securities")
            return False
        self.allSecurity = allSecurity 

        cseFee = self.getCSEFeesForDebt()
        if not cseFee:
            print("Failed to get CSE Fees for Debt")
            return False
        self.cseFee = cseFee

    def reLogin(self):
        if not self.checkUserSession(checkReLogin=False):
            print("User Session Expired")
            if not self.login(self.username,self.password):
                print("Failed to re-login")
                return False
        return True    

    def sendGetResponse(self,url,params,header=None,checkReLogin = True):
        if checkReLogin:
            self.reLogin()

        if header == None:
            header = {"Content-Type":"application/x-www-form-urlencoded"}
        
        rawResponse = self.session.get(url,headers=header,params=params)
        
        if rawResponse.status_code != 200:
            print("Failed to get response")
            return False
    
        dictResponse = self.responseParser(rawResponse)
        return dictResponse

    def sendPostResponse(self,url,data,header=None,checkReLogin = True):
        if checkReLogin:
            self.reLogin()

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
                print("successfully parced using json5")
                return dict_response
            except:
                print("Couldn't parse json file. Printing response")
                print(response_content)
                return False


    def getUserInfo(self):
        print("Fetching cliend Account info")

        params = {
            "action":"getUserDetails",
            "format":"json"
        }

        response = self.sendGetResponse(self.order_url,params)
        
        if response["description"] == "success":
            userInfo = response["data"]["userids"][0]
            if userInfo["username"]:
                return userInfo

        return False



    def login(self,username,password):
        print("Logging in")

        data = {
            "action":"login",
            "format":"json",
            "txtUserName":username,
            "txtPassword":password
        }
        response = self.sendPostResponse(self.login_url,data,checkReLogin=False)

        if (response != False and response["data"] =="success"):
            self.loginStatus = True
            print("Successfully Logged in")
            return True
        else:
            self.loginStatus = False
            print("Failed to login")
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
            return response["data"]["market"]
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
        response = self.sendGetResponse(self.order_url,params)

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
            "format":"json",
            "market":self.userInfo["exchangeId"]
        }

        response = self.sendGetResponse(self.marketdetails_url,params)
        if response["description"] == "success":
            return response["data"]["cseFees"].split(",")[0]
        else:
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


    def checkUserSession(self,checkReLogin = True):
        params = {
            "action":"checkUserSession",
            "format":"json",
            "txtUserName":self.username
        }

        response = self.sendGetResponse(self.login_url,params,checkReLogin=checkReLogin)
        if response["description"] == "success" and response["data"]["validation"][0] == "true":
            return True
        return False

    def checkBuyDisable(self,securityId,orderPrice,orderQty):
        params = {
            "action":"checkBuyDisable",
            "format":"json",
            "txtCDSActCode":self.userInfo["clientCode"],
            "txtSecuritycode":securityId,
            "exchange":self.userInkfo["exchangeId"],
            "broker":self.userInfo["brokerId"],
            "accountid":self.userInfo["clientacntid"],
            "ordPrice":orderPrice,
            "ordQty":orderQty
        }

        response = self.sendGetResponse(self.order_url,params)
        if response["description"] == "success" and response["data"]["buyDisable"] == "false":
            return False
        else:
            return True

    def genDuplicateOrderId(self):
        chars = "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        length = 10
        order_id = ""
        while(length):
            order_id += chars[random.randint(0,len(chars)-2)]
            length -= 1
        order_id = order_id.replace(" ","0")
        return order_id

    def getBlotterData(self):
        params = {
            "action":"getBlotterData",
            "format":"json",
            "clientAcc":"all",
            "exchange":"all",
            "ordStatus":"all",
            "ordType":"all",
            "assetClass":"all",
            "otherAcc":"false"
        }

        response = self.sendGetResponse(self.order_url,params)
        if response["description"] == "success":
            return response["data"]["blotterdata"]
    
    def buy(self,securityId,quantity,price,orderType="limit",tif="day",day=1,minfillqty=0,discloseqty=None):
        print("Processing Buy Order")
        
        securityProperties = self.getSecurityProperties(securityId)
        if securityProperties:
            print("Security Properties fetched")
        else:
            print("Failed to fetch Security Properties")
            return False

        orderStatus = self.getMarketStatus(securityId)["tradestatus"]

        #checking if buyingpower is enough
        buyingPower = self.getOrderRestrictions(securityId)["buyingpower"]
        orderValue = quantity * price + int(self.calcCommision(quantity * price)["commission"])
        if orderValue > buyingPower:
            print("Not enough buying power")
            return False

        #checking if buying is disabled
        if self.checkBuyDisable(securityId,price,quantity):
            print("Buying is disabled")
            return False

        duplicateOrderId = self.genDuplicateOrderId()

        if discloseqty == None:
            discloseqty = quantity

        if orderType.upper() in self.orderType:
            orderTypeValue = self.orderType[orderType.upper()]
        else:
            print("Invalid Order Type")
            return False
        
        if (tif.upper() in self.tif) and (day in self.tif[tif.upper()]["days"]):
            tifValue = self.tif[tif.upper()]["value"]
        else:
            print("Invalid TIF")
            return False

        data = {
            "action":"submitOrder",
            "market":self.userInfo["exchangeId"],
            "broker":self.userInfo["brokerId"],
            "format":"json",
            "clientOrderId":"",
            "cseOrderId":"",
            "brokerClient":self.brokerclientval,
            "orderStatus":orderStatus,
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
            "duplicateOrderId":duplicateOrderId,
            'clientAcc':f"{self.userInfo['clientCode']} ({self.userInfo['initials']} {self.userInfo['lastName']}-{self.userInfo['nic']})",
            "cmbClientAcc_end":"",
            "assetSelect":1,
            "actionSelect":1,
            "txtSecurity":securityId,
            "cmbBoard":self.boardId,
            "spnQuantity":quantity,
            "spnPrice":price,
            "spnMinFillQuantity":minfillqty,
            "spnDisclose":discloseqty,
            "cmbOrderType":orderTypeValue,
            "cmbTif":tifValue,
            "cmbTifDays":day,
            "spnYeild":0,
            "spnEffectiveYield":0,
            "hiddenSpnCseFee":self.cseFee,
            "spnCommission":0,
            "txtTradeId":"",
            "brokerClientVal":self.brokerclientval,
            "confirm":1
        }
        
        response = self.sendPostResponse(self.order_url,data)

        if response["data"] == "success":
            print("successfully placed the order")
            return True
        else:
            print("Failed to place the order")
            return False

    def cancelOrder(self,orderId):
        print("Cancelling Order")
        params = {
            "action":"cancelOrder",
            "format":"json",
            "order":{
                "cancel":[
                    {
                        "exchangeid":self.userInfo["exchangeId"],
                        "clientaccountcode":self.userInfo["clientCode"],
                        "securitycode":"",
                        "board":"",
                        "clientorderid":orderId,
                        "orderid":"",
                        "exchangeorderid":"",
                        "orderplacedate":"",
                        "action":"",
                        "orderstatus":""
                    }
                ]
            }
        }

        response = self.sendGetResponse(self.order_url,params)
        if response["data"] == "success":
            print("successfully cancelled the order")
            return True
        else:
            print("Failed to cancel the order")
            return False
    #def getAvlSahres(self):
    #def getBlotterData(self):
    #def getSectorData(self):
    #def getCustomWatches(self):
    #def getOrderStatuses(self):
    #def getPriceChange(self):



    def sell(self,securityId,quantity,price):
        print("Processing Sell Order")

    def quickSell(self,securityId,quantity):
        print("Quick Selling for the market Value")
