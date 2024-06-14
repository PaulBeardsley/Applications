fin = open("./unprocessed.txt")
fout = open("./processed.txt", "w")

details = []    # To contain Email, Password and Access Code
seeking = True  # Looking for details
urls = []       # To contain AFA no and URL
email = ""
password = ""
access = ""
tempcount = 0

while seeking:
    line = fin.readline()
    if not line:
        break
    line = line.strip()
    
    if "Email:" in line:
        email = line
    if "Password:" in line:
        password = line
    if "Access Code:" in line:
        access = line
        if email != "" and password != "":
            seeking = False

details.append(email + '\n')
details.append(password + '\n')
details.append(access + '\n\n')

for detail in details:
    fout.write(detail)

while True:
    line = fin.readline()
    if not line:
        break
    line = line.strip()
    if "AFA" in line:
        urls.append(line + '\n')
    if "https://www.gotomypc.com" in line:
        urls.append(line + '\n---\n')

for url in urls:
    fout.write(url)

fin.close()
fout.close()