from lib import BlueLib

client = BlueLib(base_url="http://localhost:2865")
if len(input("Autologin (Y=no input)")) == 0:
    client.login("example", "example123")

while True:
    command = input(">")
    if command == "":
        exit()
    try:
        print(eval("client." + command))
    except Exception as e:
        print(e)
        print(type(e))
