"""
@ Author : HotDrify
@ Type : alpaca 7B
@ GiT : https://github.com/HotDrify/freeAI
"""
import requests
import time
from fake_useragent import UserAgent

headers = {
  "User-Agent": UserAgent().random
}
class Running:
    @staticmethod
    def main(q, proxies = None):
        r = requests.post(
          "https://us-central1-arched-keyword-306918.cloudfunctions.net/run-inference-1",
          proxies = proxies,
          data = {
            "prompt": q
          }
        )
        
        output = {
          "created": time.time(),
          "model": "alpaca-7b",
          "result": [
            {
              "prompt": q,
              "content": resp['completion']
            }
          ]
        }
        return output