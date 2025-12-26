class Security:
    MAX_ATTEMPTS = 3

    def __init__(self, credentials_file="data/user_credentials.txt"):
        self.credentials_file = credentials_file
        self.user_credentials = self.read_user_credentials()
        self.attempts = 0

    def read_user_credentials(self):
        credentials = {}
        try:
            with open(self.credentials_file, "r") as f:
                for line in f:
                    if ':' in line:
                        user_id, password = line.strip().split(":", 1)
                        credentials[user_id] = password
        except FileNotFoundError:
            print(f"File not found: {self.credentials_file}")
        return credentials

    def login(self):
        print("Welcome to the POS System")
        while self.attempts < self.MAX_ATTEMPTS:
            user_id = input("User ID: ")
            password = input("Password: ")
            if user_id in self.user_credentials and self.user_credentials[user_id] == password:
                print("Login successful.\n")
                return True
            else:
                print("Incorrect User ID or Password. Try again.")
                self.attempts += 1
        print("Your account has been locked out. Please contact system admin.")
        return False