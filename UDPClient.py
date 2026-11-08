from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)   # صبر ۱ ثانیه برای جواب
#بدون این خط، برنامه اگر جوابی نمی‌آمد تا ابد گیر می‌کرد.

print("Commands: upper / reverse / count   (type quit to exit)")
seq = 0

while True:
    command = input("Command: ")
    if command == "quit":
        break
    message = input("Message: ")

    seq = seq + 1
    packet = str(seq) + "|" + command + "|" + message 
#شماره را یکی بالا می‌بریم و بعد بسته را می‌سازیم.شماره لازم است تا ACK مربوط به همین پیام را از بقیه تشخیص بدهیم.
    got_reply = False
    #یک «پرچم» می‌سازیم با مقدار نادرست. یعنی هنوز جواب نگرفته‌ایم.
    for attempt in range(1, 6):          # حداکثر ۵ بار تلاش
        clientSocket.sendto(packet.encode(), (serverName, serverPort))
        print("Attempt", attempt, "- sent, waiting for ACK...")
        #بسته را به بایت تبدیل می‌کند و به آدرس سرور می‌فرستد. بعد چاپ می‌کند که چندمین تلاش است.
        try:
            while True:
                data, addr = clientSocket.recvfrom(2048)
                parts = data.decode().split("|", 2)
                if parts[0] == "ACK":
                    print("ACK received - server got my message!")
                elif parts[0] == "DATA":
                    print("Server says:", parts[2])
                    got_reply = True
                    break
        except timeout:
            print("Timeout! Sending again...")
        if got_reply:
            break

    if not got_reply:
        print("Failed: message not delivered.")

clientSocket.close()
