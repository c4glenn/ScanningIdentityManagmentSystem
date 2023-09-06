import requests
import json
from users import User

TESTID = 0

class NinerEngageHandler:
    def __init__(self, token, session) -> None:
        self.token = token
        self.session = session
    
    def log_attendance(self, ID) -> User:
        contents = {
            "swipe":ID,
            "token":self.token
        }
        header = {
            "content-length": "64",
            "sec-ch-ua": "",
            "request-context": "appId=cid-v1:85710323-a3e3-4fe7-a1f3-5db4b33ce79e",
            "x-xsrf-token": "CfDJ8Az9GcAD4TpIm2NmyW6ywWHEt49DCWQiGiZEH_w1n4BmVOiTXTlUBkdFii6GT4LRuggsD73tgqvAP-A6as9veYr4PdQ79yIFk7FdUTWGIQdBzs2HAkV3WByQ6UYWIbqSAOunKQ4DvHD-mk3c_WCnDeQ",
            "traceparent": "00-1744f42d87414636b4e869963d818103-30c875d5dc1546ce-01",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36",
            "credentials": "same-origin",
            "content-type": "application/json",
            "accept": "application/json, text/plain, */*",
            "x-requested-with": "XMLHttpRequest",
            "request-id": "|1744f42d87414636b4e869963d818103.30c875d5dc1546ce",
            "sec-ch-ua-platform": "",
            "origin": "https://ninerengage.charlotte.edu",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": f"https://ninerengage.charlotte.edu/card-swipe/token/{self.token}",
            "accept-encoding": "gzip, deflate",
            "accept-language": "en-US,en;q=0.9"
        }
        res = requests.post("https://ninerengage.charlotte.edu/api/discovery/swipe/attendance",json=contents, cookies=self.session.cookies,headers=header)        
        
        if(res.status_code != 200):
            raise SystemError(f"{res.status_code} - {res.content}")
        contents = res.json()
        
        u = User(ID, contents["user"]["firstName"], contents["user"]["lastName"], contents["user"]["campusEmail"])
        return u
        
        
        
if __name__ == "__main__":
    s = requests.session()
    s.cookies.set(".AspNetCore.Antiforgery.Pnjfq5WAl6o", "cookie")
    handler = NinerEngageHandler("token", s)
    user = handler.log_attendance(TESTID)
    print(user)
