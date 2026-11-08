from socket import *
#پایتون به‌تنهایی بلد نیست با شبکه کار کند. سوکت یک جعبه‌ابزار آماده برای ارتباط شبکه‌ای است. این خط می‌گوید: «همه ابزارهای این جعبه را بیاور تا بتوانم استفاده کنم»
import random
#این هم یک جعبه‌ابزار دیگر است برای تولید عدد تصادفی. بعداً برای گم‌کردن عمدی بسته لازمش داریم.
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
#از هر ادرسی به ادرس 1200 این کامپیونر پیام میاد قبول کن
print("Server is ready...")

while True:
    data, clientAddress = serverSocket.recvfrom(2048)
    #سرور اینجا می‌ایستد و منتظر پیام می‌ماند
    text = data.decode()
    #پیام در شبکه به شکل بایت می‌آید که برای ما قابل خواندن نیست. دیکد آن را به متن معمولی تبدیل می‌کند
    seq, command, message = text.split("|", 2)
    #کلاینت پیام را به شکل شماره|دستور|متن می‌فرستد
    print("Received:", text)

    # شبیه‌سازی گم‌شدن بسته (۳۰٪ مواقع جواب نمی‌دهد)
    if random.random() < 0.3:
        print("  (packet lost on purpose!)")
        continue
#یک عدد تصادفی بین ۰ و ۱ می‌دهد. اگر کمتر از ۰.۳ باشد (یعنی ۳۰٪ مواقع) سرور وانمود می‌کند پیام گم شده،
    # ۱) ACK
    serverSocket.sendto(("ACK|" + seq).encode(), clientAddress)

    # ۲) پاسخ اصلی
    if command == "upper":
        reply = message.upper()
    elif command == "reverse":
        reply = message[::-1]
    elif command == "count":
        reply = "Number of words: " + str(len(message.split()))
    else:
        reply = "Unknown command"

    serverSocket.sendto(("DATA|" + seq + "|" + reply).encode(), clientAddress)
