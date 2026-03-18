import csv
from datetime import datetime
from sqlalchemy import DateTime
from app.db.database import *
from app.dal.app_dal.interface_app_dal import IAppDal


class AppDal(IAppDal):
    async def read_csv(self) -> dict:
        data_dict: dict = {}
        with open('data.csv', newline='', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('#'):
                    current_table = line[1:]
                    data_dict[current_table] = []
                else:
                    data_dict[current_table].append(line)

        return data_dict

    async def _create_table(self) -> None:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def create_db(self) -> None:
        await self._create_table()

    async def insert_data(self, session: AsyncSession, data: dict) -> None:
        bank_map: dict = {}
        user_map: dict = {}
        cash_account_map: dict = {}
        employee_map: dict = {}


        #bank
        reader = csv.DictReader(data['bank'], delimiter=';')
        for row in reader:
            bank = Bank(
                name=row['name'],
                phone=row['phone'],
                email=row['email'],
                address=row['address'],
            )
            session.add(bank)
            await session.flush()
            bank_map[row['id']] = bank.id

        # user
        reader = csv.DictReader(data['_user'], delimiter=';')
        for row in reader:
            user = User(
                name=row['name'],
                phone=row['phone'],
                email=row['email'],
                password=row['password'],
                address=row['address'],
            )
            session.add(user)
            await session.flush()
            user_map[row['id']] = user.id

        #employee
        reader = csv.DictReader(data['employee'], delimiter=';')
        for row in reader:
            employee = Employee(
                name=row['name'],
                phone=row['phone'],
                email=row['email'],
                address=row['address'],
                date_of_hire=datetime.strptime(row['date_of_hire'], '%Y-%m-%d %H:%M:%S'),
            )
            session.add(employee)
            await session.flush()
            employee_map[row['id']] = employee.id

        #cash_account
        reader = csv.DictReader(data['cash_account'], delimiter=';')
        for row in reader:
            cash_account = CashAccount(
                number_account=row['number_account'],
                balance=float(row['balance']),
                CVV=int(row['__CVV']), #
                opening_date=datetime.strptime(row['opening_date'], '%Y-%m-%d %H:%M:%S'),
                user_id=int(user_map[row['user_id']]),
                bank_id=int(bank_map[row['bank_id']]),
            )
            session.add(cash_account)
            await session.flush()
            cash_account_map[row['id']] = cash_account.id

        #cashier
        reader = csv.DictReader(data['cashier'], delimiter=';')
        for row in reader:
            cashier = Cashier(
                employee_id=int(employee_map[row['employee_id']]),
                cashier_key=row['cashier_key'],
            )
            session.add(cashier)
        await session.flush()

        #deposit_contract
        reader = csv.DictReader(data['deposit_contract'], delimiter=';')
        for row in reader:
            deposit_contract = DepositContract(
                interest=float(row['interest']),
                cash_account_id=int(cash_account_map[row['cash_account_id']]),
                amount_of_money=float(cash_account_map[row['amount_of_money']]),
                opening_date=datetime.strptime(row['opening_date'], '%Y-%m-%d %H:%M:%S'),
                closing_date=datetime.strptime(row['closing_date'], '%Y-%m-%d %H:%M:%S'),
            )
            session.add(deposit_contract)
        await session.flush()

        #credit_contract
        reader = csv.DictReader(data['credit_contract'], delimiter=';')
        for row in reader:
            credit_contract = CreditContract(
                interest=float(row['interest']),
                cash_account_id=int(cash_account_map[row['cash_account_id']]),
                amount_of_money=float(row['amount_of_money']),
                opening_date=datetime.strptime(row['opening_date'], '%Y-%m-%d %H:%M:%S'),
                closing_date=datetime.strptime(row['closing_date'], '%Y-%m-%d %H:%M:%S'),
            )
            session.add(credit_contract)
        await session.flush()

        #manager
        reader = csv.DictReader(data['manager'], delimiter=';')
        for row in reader:
            manager = Manager(
                employee_id=int(employee_map[row['employee_id']]),
                manager_key=row['manager_key'],
            )
            session.add(manager)
        await session.flush()
