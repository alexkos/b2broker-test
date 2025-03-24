1. Deploy project locally:

1.1 Set settings into .env file - copy variables from env.example

1.2 Build project
`docker-compose -f docker-compose.yml up --build`

1.3 Apply migrations
`docker-compose -f docker-compose.yml run --rm web python manage.py migrate`

1.4 Initiate data
`docker-compose -f docker-compose.yml run --rm web python manage.py initiate_data`

3. Make tests
`docker-compose -f docker-compose.yml run --rm web pytest`


API:

1. create wallet

'POST http://localhost:8000/wallets/create'
params:
- label


2. create credit transaction

'POST http://localhost:8000/transactions/credit/new'

params:

- amount
- wallet

3. create debit transaction

'POST http://localhost:8000/transactions/debit/new'

params:

- amount
- wallet


4. get wallets

'GET http://localhost:8000/wallets/'
filter params:

- min_balance
- max_balance
- label

order params:

- ordering (label, balance)

pagination params:

- page

5. get transactions

'GET http://localhost:8000/wallets/'
filter params:

- min_amount
- max_amount
- wallet

order params:

- ordering (amount, wallet)

pagination params:

- page