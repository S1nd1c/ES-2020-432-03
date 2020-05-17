import unittest
from User import User


user1 = User("Jesus Gil y Gil", "75245896W", "654879524", "Calle Alamo 23, Marbella", "jgil@gmail.com")
user2 = User("Jesus Gil y Gil", "75245896W", 654879524, "Calle Alamo 23, Marbella", "jgil@gmail.com")
users = [user1, user2]
user_flags = [True, False]

class test_user(unittest.TestCase):

    def test_validate(self):
        for i, user in enumerate(users):
            unittest.assertEqual(user.validateInput(), user_flags[i])