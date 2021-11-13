import dropbox
import os

from dropbox.files import WriteMode


class TransferData:

    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFiles(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
       
        for root, dirs, files in os.walk(file_from):
            for allFiles in files:

                local_path = os.path.join(root, allFiles)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'sl.A8Ed_Lxx-V9H-A90ZqX4iKVtAitV7p1fml_y3YOY_zRehqmoWdLNcNI2NLrkZ2BwklUSYjGhZwR4-MSrCbadAvbiiel5am_ivppw7yoMxBlyipGeK4OZvYkmgd_PWjQ3qGQBuEVCU8E'

    transferData = TransferData(access_token)

    file_from = input("Enter the file path to Transfer -")
    file_to = input("Enter the full path to transfer files to dropbox - ")

    transferData.uploadFiles(file_from, file_to)
    print("File has been moved!!")


main()

