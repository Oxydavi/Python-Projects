import qrcode

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"

img = qrcode.make(url)
img.save("123.png")
print("[+] QR code done")
