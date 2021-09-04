from pydub import AudioSegment
import youtube_dl as yt
import os, shutil
import subprocess as sub

#  https://m.youtube.com/watch?v=IbAzMLPbfyU

#  https://m.youtube.com/watch?v=wtIs_PNk16E

# https://m.youtube.com/watch?v=HGEDxrNS9LU

#  /storage/6166-3162/Musica>

# https://www.google.com/search?q=https%3A%2F%2Fwww.youtube.com%2F
#gemitaiz%20mondo%20di%20fango&ie=utf-8&oe=utf-8&client=firefox-b-m

# https://m.youtube.com/watch?v=wtIs_PNk16E


def ChangeTitle(ytdwPath):
	tempPath = os.getcwd()
	os.chdir(ytdwPath)
	tempList = os.listdir()
	counter = 0
	for c in tempList:
		counter += 1
	title = 'download' + str(counter)
	os.chdir(tempPath)
	return  title


def Rename(title):
	path = os.getcwd() + '/'
	file = os.listdir()
	old_name = ''
	for f in file:
		old_name = f
	os.rename(path + os.path.basename(old_name), path + title + '.webm')
	
	
def Download(title, link, ytdwPath):
	tempPath = os.getcwd()
	print('*** Downloading....')
	audio_downloader = yt.YoutubeDL({'format':'bestaudio'})	
	try:
		audio_downloader.extract_info(link)
	except Exception as e:
		print('*** Exe: ' + str(e))
		print('*** Filed to download.')
		return 
	print('*** Renaming...')
	Rename(title)
	
	print('*** Converting...')
	try:
		sub.check_call("ffmpeg -i " + title + ".webm -vn -ab 128k -ar 44100 -y " + title + ".mp3", shell=True)
	except Exception as e:
		print('*** Exe: ' + str(e))
	
	print('*** Setting...')
	os.remove(tempPath + '/' + title + '.webm')
	shutil.move(tempPath + '/' + title + ".mp3", ytdwPath)
	os.chdir(ytdwPath)
	nameFile = title + '.mp3'
	newNameFile = title.replace('_', ' ') + '.mp3'
	os.rename(nameFile, newNameFile)
	print('*** Done')


def Main():
	tempPath = '/storage/emulated/0/Download/ytDownload/.temps'
	ytdwPath = '/storage/emulated/0/Download/ytDownload'
	try:
		os.chdir(tempPath)
	except FileNotFoundError:
		os.makedirs(tempPath)
		os.chdir(tempPath)
	link = input('Insert link: ')
	title = input('Insert the title: ')	
	if (title == ''):
		title = ChangeTitle(ytdwPath)
	else:
		title = title.replace(' ', '_')
	Download(title, link, ytdwPath)
	inp = input('Press any key to continue or press 2 to exit: ')
	if (inp == "2"):
		os.removedirs(tempPath)
		print('Bye bye!')
		return True
	else:		
		return False


if __name__ == '__main__':
	exit = False
	while(exit == False):
		exit = Main()


#gui = g.GUI()
#gui.label('ciao', 1, 1)
#gui.start()