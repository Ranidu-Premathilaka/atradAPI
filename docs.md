# BASEURL -  https://online.softlogicstockbrokers.lk/atsweb        

## Endpoints
### '/login'

#### 'action=login POST'
**Parameter**
- `format`:json
- `txtUserName`:Username
- `txtPassword`:Password

**Response**
````json
{NEED TO BE UPDATED}
````

#### 'action=checkUserSession GET'
**Parameters**
- `format`:json
- `txtUserName`:90772

**Response**
````json
{"code":"0","description":"success","data":{'validation':[true]}}
````

### '/order'

#### 'action=getUserDetails GET'

**Parameters**
-   `format`:json

**Response**
````json
{
    "code": "0",
    "description": "success",
    "data": {
        'userids': [
            {
                'clientCode': 'ARR/90772-LI/0',
                'clientTitle': 'MR.',
                'initials': 'A.V.A.R.L.',
                'firstName': 'AHANGAMA VIDANE ARACHCHIGE RANINDU LAKSHAN',
                'lastName': 'PREMATHILAKA',
                'address': '779/3, PANNIPITIYA ROADPELAWATTABATTARAMULLAPELAWATTASRI LANKA',
                'isCustodisan': 'false',
                'exchangeId': 'CSE',
                'brokerId': 'ARR',
                'username': '90772',
                'advisor': 'DIALOG',
                'clientacntid': '5395275',
                'telephone': '761058113',
                'nic': '200314401353'
            }
        ]
    }
}
````
#### 'action=getMarketDetails GET'
**Parameter**
- `format` :json
- `market` :CSE

**Response**
````json
{
    "code": "0",
    "description": "success",
    "data": {
        'market': [
            {
                'assets': [
                    {
                        'name': 'Equity',
                        'code': '1',
                        'boards': [
                            {
                                'name': 'REGULAR',
                                'value': '1',
                                'qtymultiply': '1',
                                'pricemultiply': '0.10',
                                'ammend': 'false',
                                'disclose': '10',
                                'pricemultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '100',
                                        'multiplier': '0.10'
                                    },
                                    {
                                        'startValue': '100',
                                        'endValue': '',
                                        'multiplier': '0.25'
                                    }
                                ],
                                'qtymultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '1'
                                    }
                                ]
                            },
                            {
                                'name': 'CROSSING',
                                'value': '4',
                                'qtymultiply': '1',
                                'pricemultiply': '0.10',
                                'ammend': 'false',
                                'disclose': '20',
                                'pricemultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '100',
                                        'multiplier': '0.10'
                                    },
                                    {
                                        'startValue': '100',
                                        'endValue': '',
                                        'multiplier': '0.25'
                                    }
                                ],
                                'qtymultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '1'
                                    }
                                ]
                            },
                            {
                                'name': 'AON',
                                'value': '5',
                                'qtymultiply': '1',
                                'pricemultiply': '0.10',
                                'ammend': 'false',
                                'disclose': '40',
                                'pricemultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '100',
                                        'multiplier': '0.10'
                                    },
                                    {
                                        'startValue': '100',
                                        'endValue': '',
                                        'multiplier': '0.25'
                                    }
                                ],
                                'qtymultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '1'
                                    }
                                ]
                            },
                            {
                                'name': 'AUCTION',
                                'value': '7',
                                'qtymultiply': '1',
                                'pricemultiply': '0.10',
                                'ammend': 'false',
                                'disclose': '10',
                                'pricemultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '100',
                                        'multiplier': '0.10'
                                    },
                                    {
                                        'startValue': '100',
                                        'endValue': '',
                                        'multiplier': '0.25'
                                    }
                                ],
                                'qtymultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '1'
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'name': 'Bill',
                        'code': '2',
                        'boards': [
                            {
                                'name': 'REGULAR',
                                'value': '1',
                                'qtymultiply': '1',
                                'pricemultiply': '0.0001',
                                'ammend': 'false',
                                'disclose': '10',
                                'pricemultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '0.0001'
                                    }
                                ],
                                'qtymultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '1'
                                    }
                                ]
                            },
                            {
                                'name': 'CROSSING',
                                'value': '4',
                                'qtymultiply': '1',
                                'pricemultiply': '0.0001',
                                'ammend': 'false',
                                'disclose': '20',
                                'pricemultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '0.0001'
                                    }
                                ],
                                'qtymultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '1'
                                    }
                                ]
                            },
                            {
                                'name': 'TOM',
                                'value': '6',
                                'qtymultiply': '1',
                                'pricemultiply': '0.0001',
                                'ammend': 'false',
                                'disclose': '40',
                                'pricemultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '0.0001'
                                    }
                                ],
                                'qtymultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '1'
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'name': 'Bond',
                        'code': '3',
                        'boards': [
                            {
                                'name': 'REGULAR',
                                'value': '1',
                                'qtymultiply': '1',
                                'pricemultiply': '0.0001',
                                'ammend': 'false',
                                'disclose': '10',
                                'pricemultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '0.0001'
                                    }
                                ],
                                'qtymultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '1'
                                    }
                                ]
                            },
                            {
                                'name': 'CROSSING',
                                'value': '4',
                                'qtymultiply': '1',
                                'pricemultiply': '0.0001',
                                'ammend': 'false',
                                'disclose': '20',
                                'pricemultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '0.0001'
                                    }
                                ],
                                'qtymultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '1'
                                    }
                                ]
                            },
                            {
                                'name': 'TOM',
                                'value': '6',
                                'qtymultiply': '1',
                                'pricemultiply': '0.0001',
                                'ammend': 'false',
                                'disclose': '40',
                                'pricemultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '0.0001'
                                    }
                                ],
                                'qtymultiplies': [
                                    {
                                        'startValue': '0',
                                        'endValue': '',
                                        'multiplier': '1'
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                'brokerclient': [
                    {
                        'name': 'local local',
                        'value': '1',
                        'description': 'Desc',
                        'ammend': 'false'
                    },
                    {
                        'name': 'local foreign',
                        'value': '2',
                        'description': 'Desc1',
                        'ammend': 'false'
                    },
                    {
                        'name': 'foreign foreign',
                        'value': '3',
                        'description': 'Desc2',
                        'ammend': 'false'
                    }
                ]
            },
            {
                'ordertype': [
                    {
                        'name': 'LIMIT',
                        'value': '2',
                        'description': '',
                        'ammend': 'false'
                    },
                    {
                        'name': 'MARKET',
                        'value': '1',
                        'description': '',
                        'ammend': 'false'
                    },
                    {
                        'name': 'STOP',
                        'value': '3',
                        'description': '',
                        'ammend': 'false'
                    },
                    {
                        'name': 'STOP LIMIT',
                        'value': '4',
                        'description': '',
                        'ammend': 'false'
                    }
                ]
            },
            {
                'tif': [
                    {
                        'name': 'DAY',
                        'value': '0',
                        'description': '',
                        'ammend': 'false',
                        'days': [
                            {
                                'day': '1'
                            }
                        ]
                    },
                    {
                        'name': 'GTD',
                        'value': '6',
                        'description': '',
                        'ammend': 'false',
                        'days': [
                            {
                                'day': '1'
                            },
                            {
                                'day': '2'
                            },
                            {
                                'day': '3'
                            },
                            {
                                'day': '4'
                            },
                            {
                                'day': '5'
                            }
                        ]
                    },
                    {
                        'name': 'GTC',
                        'value': '1',
                        'description': '',
                        'ammend': 'false',
                        'days': [
                            {
                                'day': '5'
                            }
                        ]
                    },
                    {
                        'name': 'OPG',
                        'value': '2',
                        'description': '',
                        'ammend': 'false',
                        'days': [
                            {
                                'day': '1'
                            }
                        ]
                    },
                    {
                        'name': 'IOC',
                        'value': '3',
                        'description': '',
                        'ammend': 'false',
                        'days': [
                            {
                                'day': '1'
                            }
                        ]
                    },
                    {
                        'name': 'FOK',
                        'value': '4',
                        'description': '',
                        'ammend': 'false',
                        'days': [
                            {
                                'day': '1'
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
````
#### 'action=userWatch GET'
**Parameter**
- `format` :json
- `exchange`:CSE
- `bookDefId`:1
- `watchId` :12254

**Response**
````json
{
    "code": "0",
    "description": "success",
    "data": {
        'watch': [
            {
                'id': '351978',
                'security': 'SAMP.N0000',
                'bookdefid': '1',
                'sector': '4010',
                'bidqty': '100',
                'bidprice': '117.75',
                'askqty': '1,710',
                'askprice': '119.50',
                'tradesize': '4,000',
                'tradeprice': '118.00',
                'netchange': '0.50',
                'perchange': '0.43',
                'highpx': '119.00',
                'lowpx': '116.00',
                'avgprice': '118.23',
                'totvolume': '2,276,245',
                'totturnover': '269,129,766.25',
                'tottrades': '946',
                'vwap': '117.50',
                'lasttradedtime': '14:29:59.847177',
                'foreignbuys': '',
                'foreignsells': '',
                'companyname': 'SAMPATH BANK PLC',
                'isnew': '',
                'isammend': '',
                'iscancel': '',
                'tradestatus': 'Market Close',
                'closingprice': '118.25',
                'marketSegment': 'Main',
                'assetClass': 'EQUITY',
                'securityType': 'CS',
                'AONSide': 'null',
                'AONStatus': 'null',
                'AONDATE': 'null',
                'openingprice': '117.50',
                'cashIn': '55.35384525451286'
            },{...}
        ],
        'size': [
            {
                'size': '16'
            }
        ]
    }
}
````

#### 'action=getOrderRestrictions GET'
**Parameter**
- `format` :json
- `clientAcc`: ARR/90772-LI/0
-`exchange`: CSE
- `broker`: ARR*
-`clientAnctId`: 5395275
- `security`: 

**Response**
````json
{
    "code": "0",
    "description": "success",
    "data": {
        'orderlimits': {
            'perdaylimitremaining': '499999997.9776',
            'perorderlimit': '50000000',
            'buyingpower': '34002.4976',
            'isCustodian': 'false',
            'foreignbroker': '0',
            'availableQty': '0',
            'pendingBuyQty': '0',
            'clientName': 'MR. A.V.A.R.L. PREMATHILAKA',
            'validateCusBuyPowr': '1',
            'isSystemClient': 'true',
            'isEnableMangerApproval': '0'
        }
    }
}
````
#### 'action=getMarketStatus GET'
**Parameter**
- `format` :json
- `securityid` :AAF.R0001
- `boardId` :1
- `exchange` :CSE

**Response**  
````json
{"code":"0","description":"success","data":{'security':'AAF.R0001','isnew':'false','isammend':'false','iscancel':'false','securitystatus':'Market Close','tradestatus':'Market Close'}}
````   

#### 'action=getWatchForSecurity GET'
**Parameter**
- `format` :json
- `securityid` :AAF.R0001
- `exchange` :CSE
- `bookDefId` :1

**Response**
````json
{
    "code": "0",
    "description": "success",
    "data": {
        'id': '328955',
        'security': 'AAF.R0001',
        'bookdefid': '1',
        'sector': '4020',
        'bidqty': '',
        'bidprice': '',
        'askqty': '',
        'askprice': '',
        'tradesize': '',
        'tradeprice': '',
        'netchange': '0.00',
        'perchange': '0.00',
        'highpx': '',
        'lowpx': '',
        'avgprice': '0.00',
        'totvolume': '0',
        'totturnover': '',
        'tottrades': '',
        'vwap': '0.00',
        'lasttradedtime': '',
        'foreignbuys': '',
        'foreignsells': '',
        'companyname': 'AAF.R0001',
        'isnew': '',
        'isammend': '',
        'iscancel': '',
        'tradestatus': 'Market Close',
        'closingprice': '',
        'marketSegment': 'Main',
        'assetClass': 'null',
        'securityType': 'CS',
        'AONSide': 'null',
        'AONStatus': 'null',
        'AONDATE': 'null',
        'openingprice': '',
        'cashIn': ''
    }
}
```` 

#### 'action=calcCommission GET'
**Parameter**
- `format` :json
- `orderValue` :0.0000
- `accountType` :normal
-`exchange`: CSE
- `broker`: ARR

**Response**
````json
{"code":"0","description":"success","data":{'commision':[0.0]}}
````

### '/watch'
#### 'action=getAllSecurities GET'
**Parameters**
- `format` :json
- `exchange` :CSE

**Response**
````json
{
    "code": "0",
    "description": "success",
    "data": {
        'identifier': 'security',
        'label': 'securityDetails',
        'items': [
            {
                'security': 'AAF-BD-18/12/27-C2556-12.2',
                'securityDes': 'AAF-BD-18/12/27-C2556-12.2',
                'assetClass': 'CORP',
                'maturitydate': 'null',
                'sectorCode': ''
            },{...}
    }
}
````

#### 'action=getSectorData GET'
**Parameters**
-`format` :json
-`bookDefId` :1
-`exchange` :CSE

**Response**
````json
{
    "code": "0",
    "description": "success",
    "data": {
        'sectorInfo': [
            {
                'code': '1010',
                'desc': 'ENERGY'
            },
            {
                'code': '1510',
                'desc': 'MATERIALS'
            },
            {
                'code': '2010',
                'desc': 'CAPITAL GOODS'
            },
            {
                'code': '2020',
                'desc': 'COMMERCIAL  SERVICES'
            },
            {
                'code': '2030',
                'desc': 'TRANSPORTATION'
            },
            {
                'code': '2510',
                'desc': 'AUTOMOBILES '
            },
            {
                'code': '2520',
                'desc': 'CONSUMER DURABLES '
            },
            {
                'code': '2530',
                'desc': 'CONSUMER SERVICES'
            },
            {
                'code': '2540',
                'desc': 'MEDIA'
            },
            {
                'code': '2550',
                'desc': 'RETAILING'
            },
            {
                'code': '3010',
                'desc': 'FOOD  RETAILING'
            },
            {
                'code': '3020',
                'desc': 'FOOD, BEVERAGE '
            },
            {
                'code': '3030',
                'desc': 'HOUSEHOLD  PRODUCTS'
            },
            {
                'code': '3510',
                'desc': 'HEALTH CARE EQUIPMENT '
            },
            {
                'code': '3520',
                'desc': 'PHARMACEUTICALS, BIOTECHNOLOGY  SCIENCES'
            },
            {
                'code': '4010',
                'desc': 'BANKS'
            },
            {
                'code': '4020',
                'desc': 'DIVERSIFIED FINANCIALS'
            },
            {
                'code': '4030',
                'desc': 'INSURANCE'
            },
            {
                'code': '6020',
                'desc': 'Real Estate Management and Development'
            },
            {
                'code': '4510',
                'desc': 'SOFTWARE & SERVICES'
            },
            {
                'code': '4520',
                'desc': 'TECHNOLOGY HARDWARE '
            },
            {
                'code': '4530',
                'desc': 'SEMICONDUCTORS  EQUIPMENT'
            },
            {
                'code': '5010',
                'desc': 'TELECOMMUNICATION SERVICES'
            },
            {
                'code': '5510',
                'desc': 'UTILITIES'
            },
            {
                'code': '0000',
                'desc': 'UNCLASSIFIED'
            },
            {
                'code': '6010',
                'desc': 'Equity Real Estate Investment Trusts (REITs)'
            }
        ],
        'size': [
            {
                'size': '26'
            }
        ]
    }
}
````

#### 'action=getCustomWatches GET'
**Parameters**
- `format` :json
- `exchange`:CSE

**Response**
````json
{
    "code": "0",
    "description": "success",
    "customwatches": {
        'watchListName': [
            {
                'watchListID': '12254',
                'watchListName': 'default watch',
                'exchangeID': 'CSE'
            },{...}
        ],
        'size': [
            {
                'size': 'NUMBER OF WATCHLISTS'
            }
        ]
    }
}
````

#### 'action=getTickerData GET'
**Parameters**
- `format` :json
- `tickerId`:0

**Response**
````json
{
    "code": "0",
    "description": "success",
    "data": {
        'ticker': [
            {
                'id': '40235',
                'security': 'SAMP.N0000',
                'qty': '4000',
                'price': '118.00',
                'netchange': '0.50',
                'bookdefid': '1',
                'time': '02:29'
            },{....}
        ],
        'size': [
            {
                'size': 'amount of ids'
            }
        ]
    }
}
````
### '/client'

#### 'action=getUsersBrokerAndExchange GET'
**Parameters**
- `format` :json
- `username`:90772

**Response**
````json
{"code":"0","description":"success","data":{'userDetails':[{'userId':'null','userName':'90772','firstName':'','lastName':'','profile':'','telephone1':'','telephone2':'','email':'','isActive':'false','broker':'ARR','createdby':'null','createddate':'null','exchange':'CSE','status':'null','newUser':'0','pwLastChanged':'null','primaryAcc':'null','pwMailStatus':'null','secQuestion':'','secAnswer':'','isEnabledShortSell':'false'}],'pagecount':[1]}}
````

### '/marketdetails'

#### 'action=getCSEFeesForDebit'
**Parameter**
- `format` :json
- `market` :CSE

**Response**
````json
{"code":"0","description":"success","data":{'cseFee':'0.02,0.0'}}
````


#### 'action=getOrderStatuses GET'
**Parameter**
- `format` :json
- `market` :CSE

**Response**
````json
{
    "code": "0",
    "description": "success",
    "data": {
        'orderstatuses': [
            {
                'orderstatus': 'NEW',
                'board': '',
                'exchange': '',
                'desciption': 'NEW order',
                'code': '0'
            },
            {
                'orderstatus': 'P.FILLED',
                'board': '',
                'exchange': '',
                'desciption': 'P.FILLED order',
                'code': '1'
            },
            {
                'orderstatus': 'FILLED',
                'board': '',
                'exchange': '',
                'desciption': 'FILLED order',
                'code': '2'
            },
            {
                'orderstatus': 'CANCELED',
                'board': '',
                'exchange': '',
                'desciption': 'CANCELED order',
                'code': '4'
            },
            {
                'orderstatus': 'AMENDED',
                'board': '',
                'exchange': '',
                'desciption': 'AMENDED order',
                'code': '5'
            },
            {
                'orderstatus': 'QUEUED',
                'board': '',
                'exchange': '',
                'desciption': 'QUEUED order',
                'code': '6'
            },
            {
                'orderstatus': 'Q.AMEND',
                'board': '',
                'exchange': '',
                'desciption': 'Q.AMEND order',
                'code': '7'
            },
            {
                'orderstatus': 'Q.CANCEL',
                'board': '',
                'exchange': '',
                'desciption': 'Q.CANCEL order',
                'code': '9'
            },
            {
                'orderstatus': 'EXPIRED',
                'board': '',
                'exchange': '',
                'desciption': 'EXPIRED order',
                'code': 'c'
            },
            {
                'orderstatus': 'REJECTED',
                'board': '',
                'exchange': '',
                'desciption': 'REJECTED order',
                'code': '8'
            },
            {
                'orderstatus': 'PENDING',
                'board': '',
                'exchange': '',
                'desciption': 'PENDING order',
                'code': '-1'
            },
            {
                'orderstatus': 'PENDING REPLACE',
                'board': '',
                'exchange': '',
                'desciption': 'PENDING REPLACE order',
                'code': 'E'
            },
            {
                'orderstatus': 'PENDING NEW',
                'board': '',
                'exchange': '',
                'desciption': 'PENDING NEW order',
                'code': 'A'
            }
        ]
    }
}
````