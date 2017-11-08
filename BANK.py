class Bank(object):
    def __init__(self, BankId, Bankname, Location):
        self.BankId = BankId
        self.Bankname = Bankname
        self.Location = Location


class Customer(Bank):
    def __init__(self,BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo):
        super(Customer, self).__init__(BankId, Bankname, Location)
        self.accounts = {}
        self.CustomerId = CustomerId
        self.AcctNo = AccountNo
        self.Name = Name
        self.Address = Address
        self.PhoneNo = PhoneNo

    def GeneralInquiry(self):
        try:
            g = self.accounts[self.CustomerId]['CustomerId']
            h = self.accounts[self.CustomerId]['Name']
            j = self.accounts[self.CustomerId]['Address']
            k = self.accounts[self.CustomerId]['PhoneNo']
            l = self.accounts[self.CustomerId][self.AcctNo]['accountNumber']
            m = self.accounts[self.CustomerId][self.AcctNo]['AccountBalance']
            print('Bank ID:%s\nBank Name: %s\nBank Location: %s\n' % (self.BankId, self.Bankname, self.Location))
            print('CustomerId: %s\nCustomer_Name: %s\nAddress: %s\nPhoneNo.: %s \n' % (g, h, j, k))
            print('AccountNo: %s\nAccountBalance: %s\n' % (l, m))
            try:
                y = self.accounts[self.CustomerId]['loan']['loanbalance']
                z = self.accounts[self.CustomerId]['loan']['loanType']
                print('Active_Loan: %s\n' % y)
                print('loan Type: %s\n' % z)
            except:
                print('Loan is not available')
        except:
            print('Account unavailable!')

    def DepositMoney(self, Amount):
        self.Amount = Amount
        if self.Amount > 0:
            self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] += self.Amount

    def WithdrawMoney(self, amount):
        self.amount = amount
        if 0 < self.amount < self.accounts[self.CustomerId][self.AcctNo]['AccountBalance']:
            self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] -= self.amount
        else:
            print('Not enough balance')

    def OpenAccount(self):
        self.accounts[self.CustomerId] = {}
        self.accounts[self.CustomerId]['Name'] = self.Name
        self.accounts[self.CustomerId]['CustomerId'] = self.CustomerId
        self.accounts[self.CustomerId]['Address'] = self.Address
        self.accounts[self.CustomerId]['PhoneNo'] = self.PhoneNo
        self.accounts[self.CustomerId][self.AcctNo] = {}
        self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] = 0
        return self.accounts

    def CloseAccount(self):
        del self.accounts[self.CustomerId]

    def ApplyForLoan(self, loanAmount):
        self.loanAmount = loanAmount
        try:
            self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        except:
            print('Loan can not be offered')
        if self.loanAmount > (1.5 * (self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'])):
            print('You are not eligible')
        else:
            print('Successful')

    def RequestCard(self):
        try:
            self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        except:
            print('Account needed first')


class Teller(Customer, Bank):
    def __init__(self,TellerName, TellerId, BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo):
        super(Teller, self).__init__(BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo)
        self.TellerName = TellerName
        self.TellerId = TellerId

    def CollectMoney(self):
        if self.Amount > 0:
            self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] += self.Amount
        else:
            print('Input amount greater than zero')

    def LoanRequest(self, loanId ,Type):
        self.loanType = Type
        self.loanId = loanId
        try:
            self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        except:
            print('Loan can not be offered')
        if self.loanAmount > (1.5*(self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'])):
            print('You are not eligible')
        else:
            self.accounts[self.CustomerId]['loan'] = {}
            self.accounts[self.CustomerId]['loan']['loanId'] = self.loanId
            self.accounts[self.CustomerId]['loan']['loanType'] = self.loanType
            self.accounts[self.CustomerId]['loan']['loanbalance'] = -self.loanAmount
            print('loan account successfully created!')

    def ProvideInfo(self):
        print('Bank ID:%s\nBank Name: %s\nBank Location: %s\n' % (self.BankId, self.Bankname, self.Location))
        print('Teller Id: %s\nTeller Name: %s\n' % (self.TellerId, self.TellerName))

    def IssueCard(self):
        if self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] == self.AcctNo:
            print('Your Information and ATM card were successfully processed')
        else:
            print('ATM card can not be offered')


class Account(Customer):
    pass


class Loan(Customer):
    def __init__(self, LoanId, Type, AccountId, BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo):
        super(Loan, self).__init__(BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo)
        self.LoanId = LoanId
        self.Type = Type
        self.AcctNo = AccountId


BANK_one = Bank(1, 'EQUITY BANK', 'WANDEGEYA')
BANK_two = Bank(2, 'KCB BANK', 'GULU')


a = int(input('Enter the BankId:\n'))
b = input('Enter the name of the Bank: \n')
c = input('Enter the bank location:\n')
d = input('if your a customer enter C or if a teller enter T:\n')
if d == 'C':
    q = 1
    while q < 11:
        q += 1
        R, S, W, U = input('Enter the Name of the customer:\n'), input('Enter customer Address:\n'), \
                     int(input('Enter  customer phone number')), input('Enter customer Account Number:\n')
        Cus_1 = Customer(a, b, c, q, U, R, S, W)
        while True:
            M = int(input('Enter: 1 for General inquiry , 2 for Depositing , 3 for withdrawal, 4 for Request,'
                          ' 5 for Loan Application, 6 Open Account, 7 Close Account, 8 Quit'))
            if M == 1:
                Cus_1.GeneralInquiry()
            elif M == 2:
                F = int(input('Enter the amount you want to deposit \n'))
                Cus_1.DepositMoney(F)
            elif M == 3:
                G = int('Enter the amount you want to withdraw\n')
                Cus_1.WithdrawMoney(G)
            elif M == 4:
                Cus_1.RequestCard()
            elif M == 5:
                H = input('Enter the amount of loan you need \n')
                Cus_1.ApplyForLoan(H)
            elif M == 6:
                Cus_1.OpenAccount()
            elif M == 7:
                Cus_1.CloseAccount()
            elif M == 8:
                break
elif d == 'T':
    t, p, h, d, e, f, g = input('Teller Name:\n'), input('TellerID:\n'), input('Enter Customer Name:\n'),\
                          input('Enter your Address:\n'), int(input('Enter your phone Number')),\
                        input('Enter Your Account Number:\n'), input('Enter CustomerId:')
    Teller = Teller(t, p, n, b, c, g, f, h, d, e)

    while True:
        while True:
            h = int(input('Enter: 1 for General inquiry\n , 2 for Depositing\n , 3 for withdrawing\n, 4 for Requesting\n,'
                          ' 5 for Loan Application\n, 6 Open Account\n, 7 Close Account\n, 8 Quit\n, 9 Provide Info\n, '
                          '10  Work on loan Request\n, 11 IssueCard\n,'))
            if h == 1:
                Teller.GeneralInquiry()
            elif h == 2:
                F = int(input('Enter the amount you want to deposit in figure\n'))
                Teller.DepositMoney(F)
            elif h == 3:
                G = int('Enter the amount you want to withdraw\n')
                Teller.WithdrawMoney(G)
            elif h == 4:
                Teller.RequestCard()
            elif h == 5:
                H = input('Enter the amount of loan you need in figures\n')
                Teller.ApplyForLoan(H)
            elif h == 6:
                Teller.OpenAccount()
            elif h == 7:
                Teller.CloseAccount()
            elif h == 8:
                break
            elif h == 9:
                Teller.ProvideInfo()
            elif h == 10:
                U = int(input('Enter loanId for the  Customer:'))
                t = input('Enter loan type requested by Customer:')
                Teller.LoanRequest(U, t)
            elif h == 11:
                Teller.IssueCard()




























