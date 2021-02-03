import bcrypt


class PasswordHasher:
    def __init__(self, password):
        self.password = password

    def hash(self):
        hashed = bcrypt.hashpw(b'{self.password}', bcrypt.gensalt())
        return hashed
