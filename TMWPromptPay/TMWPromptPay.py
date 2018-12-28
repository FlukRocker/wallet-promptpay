from .Config import Config
from urllib.parse import urlencode
import hashlib
import requests

class Wallet:

	isLogged = False

	fullname = None
	name = None
	mobileNumber = None
	email = None
	tmnId = None
	thaiId = None
	ewalletId = None

	def __init__(self, email, password):
		password = hashlib.sha1(("%s%s" % (email, password)).encode("utf-8")).hexdigest()

		jsonData = {
			"username": email,
			"password": password,
			"type": "email"
		}
		jsonResp = requests.post(Config.SIGNIN_URL, headers=Config.HEADERS, params=Config.PARAMS, json=jsonData).json()

		if jsonResp["code"] == "20000":
			self.accessToken = jsonResp["data"]["accessToken"]
			self.fullname = jsonResp["data"]["fullname"]
			self.name = jsonResp["data"]["title"] + " " + jsonResp["data"]["fullname"]
			self.mobileNumber = jsonResp["data"]["mobileNumber"]
			self.email = jsonResp["data"]["email"]
			self.currentBalance = jsonResp["data"]["currentBalance"]
			self.tmnId = jsonResp["data"]["tmnId"]
			self.thaiId = jsonResp["data"]["thaiId"]

			headers = Config.HEADERS
			headers["Authorization"] = "Bearer " + self.accessToken
			self.ewalletId = requests.get(Config.KYC_PROFILE_URL + "/" + self.mobileNumber, headers=headers).json()["data"]["ewallet_id"]
		else:
			raise Exception("Cannot signin")

	def updateCurrentBalance(self):
		self.currentBalance = requests.get(Config.PROFILE_URL + "/" + self.accessToken, headers=Config.HEADERS, params=Config.PARAMS).json()["data"]["currentBalance"]
		return self.currentBalance

	def lookup(self, receiverPromptpayAccountId, amount):
		params = {
			"access_token": self.accessToken
		}
		jsonData = {
			"amount": amount,
			"inputMethod": "keyIn",
			"receiverPromptpayAccountId": receiverPromptpayAccountId,
			"senderTmnProfile": {
				"ewalletId": self.ewalletId,
				"fullName": self.fullname,
				"mobileNumber": self.mobileNumber,
				"thaiId": self.thaiId,
				"tmnId": self.tmnId
			}
		}
		return requests.post(Config.PROMPTPAY_LOOKUP_URL, headers=Config.HEADERS, params=params, json=jsonData).json()["data"]

	def otp(self):
		return requests.get(Config.OTP_URL.format(self.accessToken), headers=Config.HEADERS, params=Config.PARAMS).json()["data"]

	def transfer(self, draftTransactionId, otpString, otpRefCode):
		params = {
			"access_token": self.accessToken
		}
		jsonData = {
			"channelId": "46",
			"draftTransactionId": draftTransactionId,
			"inputMethod": "keyIn",
			"otpRefCode": otpRefCode,
			"otpString": otpString,
			"senderMobileNumber": self.mobileNumber,
			"tmnId": self.tmnId
		}
		return requests.post(Config.PROMPTPAY_TRANSFER_URL, headers=Config.HEADERS, params=params, json=jsonData).json()["data"]
