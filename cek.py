import requests
import json

print """
####################
    Bank Checker
####################
"""

print """
1. BCA
2. Mandiri
3. BNI
4. BRI
5. BSI
6. BCA Syariah
7. BTN / BTN Syariah
8. CIMB / CIMB Niaga Syariah
9. DBS Bank Indonesia
10. BTPN / Jenius / BTPN Wow!
11. Seabank / Bank BKE
12. Danamon / Danamon Syariah
13. Muamalat
14. Bank Jago
15. LINE Bank / KEB Hana
16. blu by BCA Digital
17. Nobu (Nationalnobu) Bank
18. Bank Permata
19. Maybank Indonesia
20. Panin Bank
21. TMRW / UOB
22. OCBC NISP
23. Citibank
24. Bank Artha Graha Internasional
25. HSBC Indonesia
26. Bank Mayapada
27. Bank Sinarmas
28. Bank Maspion Indonesia
29. Bank Mega
30. Bank Mega Syariah
31. OVO (Required 62...)
32. DANA (Required 62...)
33. LinkAja (Required 62...)
34. GoPay (Required 62...)
35. ShoopePay (Required 62...)
*Note: Enter number character!!!
"""
account_bank = [
"bca",
"mandiri",
"bni",
"bri",
"bsm",
"bca_syr",
"btn",
"cimb",
"dbs",
"btpn",
"kesejahteraan_ekonomi",
"danamon",
"muamalat",
"artos",
"hana",
"royal",
"nationalnobu",
"permata",
"bii",
"panin",
"uob",
"ocbc",
"citibank",
"artha",
"hsbc",
"mayapada",
"sinarmas",
"maspion",
"mega",
"mega_syr",
"ovo",
"dana",
"linkaja",
"gopay",
"shopeepay"
]
try:
    raw_bank = input("Your Account Bank: ")
    raw_acc = input("Your Account Number: ")
    no_acc = raw_bank-1
    req = requests.post("https://netovas.com/api/cekrek/v1/account-inquiry", data={"account_bank":account_bank[no_acc],"account_number":raw_acc}).text
    req_arr = json.loads(req)
    print "Status: " + str(req_arr["success"]).upper()
    print "Message: " + str(req_arr["message"]).upper()
    print "Bank Name: " + str(req_arr["data"]["account_bank"]).upper()
    print "Account Number: " + str(req_arr["data"]["account_number"])
    print "Account Name: " + str(req_arr["data"]["account_holder"]).upper() + "\n"
except NameError:
    print "Enter Number Character!!!\n"
except SyntaxError:
    print "Input Cannot Be Empty!!!\n"
except KeyError:
    print "Account Not Found!!!\n"
    exit()
