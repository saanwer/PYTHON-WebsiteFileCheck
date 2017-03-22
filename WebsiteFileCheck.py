#Website Files & Links Lookup
#Coded by | WarLord
#https://github.com/saanwer
from bs4 import BeautifulSoup
import urllib2
from clint.textui import colored
website = raw_input("Enter website to look for files and links : ")#Input website (Ex:www.facebook.com)
read = urllib2.urlopen("http://"+website)
readall = read.read()
read.close()
pars = BeautifulSoup(readall, "html.parser")
reade = pars.find_all("a")
for links in pars.find_all("a"):
	print colored.yellow(links.get('href'))
