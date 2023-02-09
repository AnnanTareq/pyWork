def main():
    print('Welcome to the email slicer')

    email_input = input('Input your email address')
    (user_name, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')

    print('User Name ', user_name)
    print('Domain :', domain)
    print('Extension : ', extension)


main()