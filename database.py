import numpy as np

class Database():
    def __init__(self):
        self.db = {}
    
    def add(self, user, samples:list):
        assert len(samples) >2, "Password init requires at least 3 samples."
        samples = np.array(samples).mean(axis=0)
        self.db[user] = samples

    def _update(self, user, sample, beta=0.9):
        old_password = self.db[user]
        self.db[user] = beta*old_password + (1-beta)*sample
    
    def verify(self, user, sample) -> bool:
        assert user in self.db.keys(), "User not found"
        password = self.db[user]
        corrcoef = np.array([np.abs(np.corrcoef(password[i], sample[i])) for i in range(64)]).mean()
        if corrcoef < 0.6:
            return False
        else:
            self._update(user, sample)
            return True
