from win32com import client

a = client.Dispatch('SAPI.SpVoice')

a.speak('hello')