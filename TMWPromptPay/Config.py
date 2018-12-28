class Config:

	SCHEME = "https"
	HOST = SCHEME + "://mobile-api-gateway.truemoney.com"

	DEVICE_OS = "android"
	DEVICE_ID = "574e0139a8e4460dac351feac6157871"
	DEVICE_TYPE = "Zenfone Max"
	DEVICE_VERSION = "7.1.2"
	APP_NAME = "wallet"
	APP_VERSION = "4.18.0"

	HEADERS = {
		"User-Agent": "okhttp/3.9.0",
		"Connection": "close",
		"Accept-Encoding": "gzip, deflate"
	}

	PARAMS = {
		"device_os": DEVICE_OS,
		"device_id": DEVICE_ID,
		"device_type": DEVICE_TYPE,
		"device_version": DEVICE_VERSION,
		"app_name": APP_NAME,
		"app_version": APP_VERSION
	}

	SIGNIN_PATH = "/mobile-api-gateway/api/v1/signin"
	SIGNIN_URL = HOST + SIGNIN_PATH
	OTP_PATH = "/mobile-api-gateway/api/v1/{}/otp"
	OTP_URL = HOST + OTP_PATH
	PROFILE_PATH = "/mobile-api-gateway/api/v1/profile"
	PROFILE_URL = HOST + PROFILE_PATH
	KYC_PROFILE_PATH = "/mobile-api-gateway/api/v1/kyc/customer-profiles"
	KYC_PROFILE_URL = HOST + KYC_PROFILE_PATH
	PROMPTPAY_LOOKUP_PATH = "/mobile-api-gateway/api/v1/promptpay/sending/lookup"
	PROMPTPAY_LOOKUP_URL = HOST + PROMPTPAY_LOOKUP_PATH
	PROMPTPAY_TRANSFER_PATH = "/mobile-api-gateway/api/v1/promptpay/sending/transfer"
	PROMPTPAY_TRANSFER_URL = HOST + PROMPTPAY_TRANSFER_PATH
