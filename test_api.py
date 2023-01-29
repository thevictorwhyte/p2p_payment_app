import unittest
import json
from app import app

class P2PAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_user(self):
        user1 = {'name': 'Victor Whyte', 'email': 'victorwhyte@gmail.com'}
        user2 = {'name': 'David Whyte', 'email': 'davidwhyte@gmail.com'}
        response1 = self.app.post('/users', data=json.dumps(user1), content_type='application/json')
        response2 = self.app.post('/users', data=json.dumps(user2), content_type='application/json')
        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 201)
    
    def test_deposit(self):
        deposit_data = {'email': 'victorwhyte@gmail.com', 'amount': 20}
        response = self.app.post('/deposit', data=json.dumps(deposit_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_withdraw(self):
        withdraw_data = {'email': 'victorwhyte@gmail.com', 'amount': 10}
        response = self.app.post('/withdraw', data=json.dumps(withdraw_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_send_money(self):
        send_money_data = {'senderEmail': 'victorwhyte@gmail.com', 'receiverEmail': 'davidwhyte@gmail.com', 'amount': 10}
        response = self.app.post('/send_money', data=json.dumps(send_money_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
    def test_insufficient_funds(self):
        send_money_data = {'senderEmail': 'victorwhyte@gmail.com', 'receiverEmail': 'davidwhyte@gmail.com', 'amount': 1000}
        response = self.app.post('/send_money', data=json.dumps(send_money_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        
    def test_balance(self):
        check_balance_data = { 'email': 'victorwhyte@gmail.com'}
        response = self.app.post('/balance', data=json.dumps(check_balance_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
