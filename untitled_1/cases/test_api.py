import json
import unittest
import config
from lib.client import HttpHandler

class TestDoctorsApi(unittest.TestCase):
    http = None
    '''平安出行接口'''

    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        # cls.hcn_url = config.Config.enum.get('url').get('hcn_url')
        # cls.pcn_url = config.Config.enum.get('url').get('pcn_url')
        # cls.shop_url = config.Config.enum.get('url').get('shop_url')

    @classmethod
    def tearDownClass(cls):
        cls.http.session.close()

    # def test_api1(self):
    #     '''身份认证-身份证已存在'''
    #     url = 'http://121.199.23.170:8083/carshare/member/authIdAndDriver'
    #
    #     data = {
    #     "mobile":"17681801533",
    #     "aCertifyNum":"412724199010026123",
    #     "aRealName":"刘金平",
    #     "aSex":"1",
    #     "certifyType":"1",
    #     "certifyImg":"test",
    #     "certifyImgPositive":"test",
    #     "nation":"女",
    #     "birthday":"19901002",
    #     "addr":"xxx",
    #     "idCardEndTime":"20100221-20200221",
    #     "pubOrg":"太康县公安局",
    #     "orderNo":"test123456789test"
    #         }
    #     headers= {
    #
    #         'Content-Type':'application/json'
    #         }
    #     response = self.http.post(url=url, json=data, headers=headers)
    #     print(response)
    #
    # def test_api2(self):
    #     '''身份认证-身份证非法'''
    #     url = 'http://121.199.23.170:8083/carshare/member/authIdAndDriver'
    #
    #     data = {
    #     "mobile":"13588293143",
    #     "aCertifyNum":"360781199201013410",
    #     "aRealName":"王鹏",
    #     "aSex":"2",
    #     "certifyType":"1",
    #     "certifyImg":"test",
    #     "certifyImgPositive":"test",
    #     "nation":"女",
    #     "birthday":"19901002",
    #     "addr":"xxx",
    #     "idCardEndTime":"20100221-20200221",
    #     "pubOrg":"太康县公安局",
    #     "orderNo":"test123456789test"
    #         }
    #     headers= {
    #
    #         'Content-Type':'application/json'
    #         }
    #     response = self.http.post(url=url, json=data, headers=headers)
    #     print(response)
    #
    def test_api3(self):
        '''身份认证-身份证已认证'''

        url = 'http://121.199.23.170:8083/carshare/member/authIdAndDriver'

        data = {
        "mobile":"13500000999",
        "aCertifyNum":"623022198310042226",
        "aRealName":"王鹏1",
        "aSex":"2",
        "certifyType":"1",
        "certifyImg":"test",
        "certifyImgPositive":"test",
        "nation":"女",
        "birthday":"19901002",
        "addr":"xxx",
        "idCardEndTime":"20100221-20200221",
        "pubOrg":"太康县公安局",
        "orderNo":"test123456789test"
            }
        headers= {
            'Content-Type':'application/json'
            }
        response = self.http.post(url=url, json=data, headers=headers)
        print(response)

    # def test_api4(self):
    #     '''身份认证-未认证身份证认证通过获取驾驶证信息'''
    #     url = 'http://121.199.23.170:8083/carshare/member/authIdAndDriver'
    #
    #     data = {
    #     "mobile":"13588293143",
    #     "aCertifyNum":"330051199404138235",
    #     "aRealName":"傅云波",
    #     "aSex":"2",
    #     "certifyType":"1",
    #     "certifyImg":"test",
    #     "certifyImgPositive":"test",
    #     "nation":"男",
    #     "birthday":"19901002",
    #     "addr":"xxx",
    #     "idCardEndTime":"20100221-20200221",
    #     "pubOrg":"太康县公安局",
    #     "orderNo":"test123456789test"
    #         }
    #     headers= {
    #
    #         'Content-Type':'application/json'
    #         }
    #     response = self.http.post(url=url, json=data, headers=headers)
    #     print(response)
    #     self.assertEquals(self.http.get_value(response, 'code'),'3001')

    def test_api5(self):
        '''身份认证-身份证与驾驶证不匹配'''
        url = 'http://121.199.23.170:8083/carshare/member/authIdAndDriver'
        data = {
            "mobile":"18244193779",
            "aDriverNum":"330327199202124516",
            "aDriverName":"",
            "aDriverType":"A1",
            "driverImage":"test2",
            "driverImageVice":"test2",
            "aDriverEndDate":"10年",
            "aDriverStartDate":"20120713",
            "driverAddr":"温州苍南灵溪镇"
}
        headers = {
            'Content-Type':'application/json'
            }
        response = self.http.post(url=url, json=data, headers=headers)
        print(response)
        self.assertEquals(self.http.get_value(response, 'code'),'2001')

    def test_api6(self):
        '''身份认证-身份已认证驾驶证信息不存在'''
        url = 'http://121.199.23.170:8083/carshare/member/authIdAndDriver'
        data = {
            "mobile":"13588293143",
            "aDriverNum":"500223199401257646",
            "aDriverName":"王鹏1",
            "aDriverType":"A1",
            "driverImage":"test2",
            "driverImageVice":"test2",
            "aDriverEndDate":"10年",
            "aDriverStartDate":"20120713",
            "driverAddr":"温州苍南灵溪镇"
            }
        headers = {
            'Content-Type':'application/json'
            }
        response = self.http.post(url=url, json=data, headers=headers)
        print(response)

    def test_api7(self):
        '''身份认证-驾驶证认证'''
        url = 'http://121.199.23.170:8083/carshare/member/authIdAndDriver'
        data = {
            "mobile":"13500000999",
            "aDriverNum":"623022198310042226",
            "aDriverName":"王鹏1",
            "aDriverType":"A1",
            "driverImage":"test2",
            "driverImageVice":"test2",
            "aDriverEndDate":"10年",
            "aDriverStartDate":"20120713",
            "driverAddr":"温州苍南灵溪镇"
            }
        headers = {
            'Content-Type':'application/json'
            }
        response = self.http.post(url=url, json=data, headers=headers)
        print(response)

    def test_api8(self):
        '''订单'''
        url = 'http://121.199.23.170:8083/carshare/order/calc'
        data = {
            'access_token ': 'a8a84cf901bd4c61ab5b53304a3bd7cb',
            'orderId':'4285',
            'orderType ':'1'
            }
        headers={
             'Content-Type':'application/json'
            }
        response = self.http.post(url=url, json=data, headers=headers)
        print(response)

    def test_api9(self):
        '''企业即行卷开票'''
        url='http://121.199.23.170:8083/carshare/member/invoice/commit'
        data = {
	"access_token": "73339d03b6034564aaf128d332d33431",
	"invoiceHeader": "重庆长安车联科技有限公司",
	"bankAccount": "3100022409022102311",
	"address": "建新东路246号，13588293143",
	"records": [{
		"groupType": 3,
		"invoiceAmount": 1.0,
		"invoiceId": 0,
		"invoiceStatus": 0,
		"invoiceTime": "2018-08-01 15:34:31",
		"orderCheck": True,
		"outletsName": "充值时间",
		"recordId": 6254
	}],
	"invoiceType": 1,
	"taxpaperNo": "915001052028980903"
}
        headers={
             'Content-Type':'application/json'
            }
        response = self.http.post(url=url,json=data,headers=headers)
        print(response)

    def test_api10(self):
        '''企业即行订单开票'''
        url = 'http://121.199.23.170:8083/carshare/member/invoice/commit'
        data ={
	"access_token": "ec2c7b1ba119451b8ea6cbb0d85f2516",
	"invoiceHeader": "重庆长安车联科技有限公司",
	"bankAccount": "3100022409022102311",
	"address": "建新东路，023_67591187",
	"records": [{
		"carNo": "渝A55555",
		"groupType": 1,
		"invoiceAmount": 5.1,
		"invoiceId": 0,
		"invoiceStatus": 0,
		"invoiceTime": "2018-08-01 16:01:13",
		"orderCheck": True,
		"outletsName": "王道公园cjb",
		"recordId": 4287
	}],
	"invoiceType": 1,
	"taxpaperNo": "915001052028980903"
}
        headers = {
             'Content-Type':'application/json'
            }
        response = self.http.post(url=url,json=data,headers=headers)
        print(response)

    def test_api11(self):
        '''个人即行卷开票'''
        url = 'http://121.199.23.170:8083/carshare/member/invoice/commit'
        data = {
	"access_token": "73339d03b6034564aaf128d332d33431",
	"invoiceHeader": "王鹏",
	"bankAccount": "3100022409022102311",
	"address": "建新东路，13588293143",
	"records": [{
		"groupType": 3,
		"invoiceAmount": 1.0,
		"invoiceId": 0,
		"invoiceStatus": 0,
		"invoiceTime": "2018-08-01 16:55:06",
		"orderCheck": True,
		"outletsName": "充值时间",
		"recordId": 6264
	}],
	"invoiceType": 2,
	"taxpaperNo": "",
	"remarks": "报销"
}
        headers = {
             'Content-Type':'application/json'
            }

        response = self.http.post(url=url,json=data,headers=headers)
        print(response)
    def test_api12(self):
        '''个人即行订单开票'''