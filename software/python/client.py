#!/usr/bin/python
import socket,time,os,subprocess
VIDEO_DIR = "/tmp/cam"

while(True):
	list = os.listdir(VIDEO_DIR)
	busyfile = subprocess.check_output("lsof | grep raspivid | grep "+VIDEO_DIR+";exit 0",stderr=subprocess.STDOUT,shell=True)
	busyfile = busyfile[busyfile.find('/vid')+1:-1]

	out="files:{"
	for file in list:
		if(file!=busyfile):
			out += "'"+str(file)+"':'"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getmtime(VIDEO_DIR+"/"+file)))+"',"
		else:
			out += "'"+str(file)+"':'recording',"
	out += "}"
	s = socket.socket()
	try:
		s.connect(('hubsolar.cloudapp.net',2346))
		s.send(out)
		datafromserv = s.recv(1024)
		s.close()
		commandfromserv = datafromserv[datafromserv.find("command:")+9:datafromserv.find("'",datafromserv.find("command:")+9)]
		filelistfromservstr = datafromserv[datafromserv.find("diff_files:")+12:len(datafromserv)-2]
		if(filelistfromservstr!=""):
			filelistfromserv = eval(filelistfromservstr)
			#send files over SSH from 
			for ffs in filelistfromserv:
				try:
					subprocess.check_output("scp -p "+VIDEO_DIR+"/"+ffs+" azureuser@hubsolar.cloudapp.net:/tmp/video",stderr=subprocess.STDOUT,shell=True)
					print "file "+VIDEO_DIR+"/"+ffs+" peredan!\n"
				except subprocess.CalledProcessError:
					print "error file "+VIDEO_DIR+"/"+ffs+"\n"
		print "command-"+commandfromserv+"\n"
		time.sleep(5)
	except IOError:
		print('connecting')
		time.sleep(1)
