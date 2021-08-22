import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)

        f= open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='-Mw059HNExQAAAAAAAAAAdLiKr_VFcSKa6jvcDleHx9tJKuRU8WH44q7xPeFw4zJ'
    transferData = TransferData(access_token)

    file_from = input("enter file path that you need to transfer here: ")
    file_to = input("enter the full path to upload to dropbox: ")
    transferData.upload_file(file_from, file_to)

    print("file has been moved")

main()


