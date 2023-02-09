import urllib.request as urllib


def main(url):
    print('checking connectivity ')

    response = urllib.urlopen(url)
    print('COnnected to ', url, ' successfully')
    print('Response code was: ', response)


print('This is a site connectivity check program')
input_url = input('Input the url of the site you want to check : ')

main(input_url)
