from cryptography.fernet import Fernet
from rich.console import Console
from tomlkit import key

console = Console()
debug = False
def verboseprint(message):
    if debug == True:
        print(message)


"""
Warning! The key resets each time you create a new instance of the 
class.

Example Usage Below:
U = Encryption()
U.encrypt_message("Hi mom") | gives long encrypted string
U.get_key() | gives long byte type key
U.decrypt_message(<encryptedstring>, <encryption_key>)
"""
class Encryption: 
    def __init__(self, decrypted_message=None, encrypted_message=None, recieved_key=None) -> None:
        self.key = Fernet.generate_key()
        self.secretkey = Fernet(self.key)
        self.decrypted_message = decrypted_message
        self.encrypted_message = encrypted_message
        self.recieved_key = recieved_key

    def encrypt_message(self, message):
        message = bytes(message, "utf-8")
        self.encrypted_message = self.secretkey.encrypt(message)
        verboseprint(f"Encrypted Message: {self.encrypted_message}")
        verboseprint(f"Encryption Key: {self.key}")
        console.print(f"[bold cyan]Encrypted Message:[/][red] {self.encrypted_message}[/]")
        return self.encrypted_message
    
    def decrypt_message(self, encrypted_message, different_key=None):
        if different_key != None:
            tempkey = Fernet(different_key)
            self.decrypted_message = str(tempkey.decrypt(encrypted_message))
            self.decrypted_message = self.decrypted_message.replace("b'", "").replace("'", "")
            print(f"Decrypted: {str(self.decrypted_message)}")
        elif different_key == None:
            self.decrypted_message = str(self.secretkey.decrypt(encrypted_message))
            self.decrypted_message = self.decrypted_message.replace("b'", "").replace("'", "")
            print(f"Decrypted: {str(self.decrypted_message)}")
        
    def get_key(self):
        console.print(f"[bold cyan]Key:[/] [red]\n{self.key}[/]")
        return self.key
