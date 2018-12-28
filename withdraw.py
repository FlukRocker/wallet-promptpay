from TMWPromptPay import TMWPromptPay
from getpass import getpass
import hashlib
import os

print()
print("""----------------------------------
TRUEMONEY WALLET TO PROMPTPAY
by Noxturnix
https://github.com/Noxturnix
----------------------------------""")

try:
	while True:
		# Get an identification from a user
		print()
		print("[TrueMoney Wallet signin]")
		email = input("Email: ")
		password = getpass("Password: ")

		# Signin to TrueMoney Wallet
		try:
			wallet = TMWPromptPay.Wallet(email, password)
			break
		except Exception as e:
			print("ERROR <%s>" % (e))

	while True:
		# Prompt for withdrawal
		print()
		print("""----------------------------------
Name => %s
Current Balance => %s baht
----------------------------------""" % (wallet.name, float(wallet.currentBalance)))
		print("[Withdraw to PromptPay]")
		receiverId = input("Account number: ")
		amount = input("Amount: ")

		# Print transaction info
		transactionInfo = wallet.lookup(receiverId, amount)
		print()
		print("""----------------------------------
Receiver name => %s
Account No. => %s

Amount => %s
Fee => %s

Total => %s
----------------------------------""" % (transactionInfo["receiverName"], transactionInfo["receiverPromptpayAccountId"], transactionInfo["amount"], transactionInfo["fee"], transactionInfo["totalAmount"]))
		
		# Ask user to confirm the transaction
		print("[Confirmation]")
		while True:
			confirm = input("Confirm? [Y/n]: ").lower() or "y"
			if confirm in ["y", "n"]:
				break

		if confirm == "n":
			wallet.updateCurrentBalance()
			continue
		break

	# Request an OTP
	otpInfo = wallet.otp()

	# Print the OTP Information
	print()
	print("""----------------------------------
OTP has been sent to => ******%s
Ref. => %s
----------------------------------""" % (otpInfo["mobileNumber"][-4:], otpInfo["refCode"]))

	# Get an OTP from a user
	print("[OTP Confirmation]")
	otpString = input("OTP: ")

	# Confirm the OTP and complete the transaction
	transferInfo = wallet.transfer(transactionInfo["draftTransactionId"], otpString, otpInfo["refCode"])
	print()
	print("""----------------------------------
Amount => %s
Fee => %s
Total => %s

Balance => %s""" % (transferInfo["amount"], transferInfo["fee"], transferInfo["totalAmount"], transferInfo["balance"]))

	if "transactionDate" in transactionInfo and "transactionId" in transactionInfo:
		print("""
Transaction date => %s
Transaction ID => %s""" % (transferInfo["transactionDate"], transferInfo["transactionId"]))
	print("----------------------------------")
	print("[Withdrawal success]")
	print()

except (EOFError, KeyboardInterrupt):
	print()
	os._exit(0)
