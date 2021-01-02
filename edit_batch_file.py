from imapclient import IMAPClient

username = 'calebwebster531@gmail.com'
password = 'G.hoenn531'
commands = """
@echo off
cd C:\\GayApe
gay_ape.exe
"""

with open('C:\\GayApe\\enabled.txt', 'r') as enabled_file_in:
    if enabled_file_in.read().strip() == 'True':
        with IMAPClient('imap.gmail.com') as gmail:
            gmail.login(username, password)
            gmail.select_folder('INBOX', readonly=True)
            sender = b'calebwebsteredge@gmail.com'
            msg_ids = gmail.search([b'FROM', sender, b'UNSEEN'])
            if msg_ids:
                with open('C:\\GayApe\\run_gay_ape.bat', 'w') as batch_file:
                    print(commands, file=batch_file)
                with open('C:\\GayApe\\enabled.txt', 'w') as enabled_file_out:
                    print('False', file=enabled_file_out)
