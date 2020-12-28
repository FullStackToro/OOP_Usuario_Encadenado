if __name__ == '__main__':
    class usuario:
        def __init__(self, users, email):
            self.name = users
            self.email = email
            self.cuenta = 0

        def make_deposit(self, monto):
            self.cuenta += monto
            print(self.name, 'ha hecho un deposito por', '$', monto)
            return self

        def make_withdrawal(self, retiro):
            self.cuenta -= retiro
            print(self.name, 'ha hecho un retiro de', '$', retiro)
            return self

        def display_user_balance(self):
            print('*'*45, '\n', self.name, 'tiene un saldo de:\n', '$', self.cuenta, '\n', '*'*45)
            return self

        def transfer_money(self, u, monto):
            self.cuenta -= monto
            u.cuenta += monto
            print('*' * 45, '\n', self.name, 'ha hecho una transferencia a',u.name, 'por un monto de:\n',  '$', monto, '\n', '*' * 45)
            print('\n Usuario:', self.name, '\n Email:', self.email, '\n Estado cuenta:', self.cuenta, '\n\n\n', ' Usuario:', u.name, '\n Email:', u.email, '\n Cuenta:', u.cuenta)
            return self


    u1 = usuario('usuario01', 'usuario01@gmail.com')
    u2 = usuario('usuario02', 'usuario02@gmail.com')
    u3 = usuario('usuario03', 'usuario03@gmail.com')

    u1.make_deposit(1000).make_deposit(2000).make_deposit(3000).make_withdrawal(500).display_user_balance()
    u2.make_deposit(5000).make_deposit(6000).make_withdrawal(3500).make_withdrawal(199).display_user_balance()
    u3.make_deposit(10000).make_withdrawal(500).make_withdrawal(1500).make_withdrawal(3000).display_user_balance()

    u1.transfer_money(u3, 5000)
