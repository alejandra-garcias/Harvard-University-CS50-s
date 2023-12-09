from validator_collection import validators

def validate():
    email = input('Email: ')

    try:
        email_address = validators.email(email)

        if email_address:
            print('Valid')
            
    except ValueError:
        print('Invalid')

validate()
