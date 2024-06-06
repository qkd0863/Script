import telepot
import requests
import certifi

# 신뢰할 수 있는 인증서 번들 사용
token = "7204520635:AAHr0LSnYCcvw70SowiNTUF_55fV7UBH464"
chat_id = "7431693311"
message = "Hello from my bot!"


url = f"https://api.telegram.org/bot{token}/sendMessage"


# 요청 보내기
response = requests.post(url, data={
    'chat_id': chat_id,
    'text': message
}, verify=certifi.where())

# 응답 출력
print(response.json())