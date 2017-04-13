import dropbox

from dropbox import client, rest, session

def uploading():
	folder = open('working-draft.txt', 'rb')
	response = client.put_file('/magnum-opus.txt', folder)
	print 'uploaded: ', response

def retrieving():
	folder_metadata = client.metadata('/')
	print 'metadata: ', folder_metadata

	folder, metadata = client.get_file_and_metadata('/magnum-opus.txt')
	out = open('magnum-opus.txt', 'wb')
	out.write(folder.read())
	out.close()
	print metadata

APP_KEY = 'xary9q5nh6dhoqw'
APP_SECRET = 'cdl3dod2vuj16im'
 
ACCESS_TYPE = 'app_folder'
 
sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

request_token = sess.obtain_request_token()
url = sess.build_authorize_url(request_token)
 
print "url:", url
print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
raw_input() 

access_token = sess.obtain_access_token(request_token)
print access_token
uploading()
retrieving()




