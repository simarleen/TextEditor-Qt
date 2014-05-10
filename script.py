from evernote.api.client import EvernoteClient


dev_token = "S=s1:U=8dbab:E=14d062fa670:C=145ae7e7a73:P=1cd:A=en-devtoken:V=2:H=c2ba08432628c288ad9f4b11429adc1a"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username

                                                                           
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()

noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
for n in notebooks:
  print n.name

note = Types.Note()
note.title = "I'm a test note!"
note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote....ub/enml2.dtd">'
note.content += '<en-note>Hello, world!</en-note>'
note = noteStore.createNote(note)



