from adapter.easybroker import apiConsult

'''
cd C:/Users/aaron/OneDrive/Escritorio/EasyBroker
.\env\Scripts\activate
set EASYBROKER_CLIENT_ID=l7u502p8v46ba3ppgvj5y2aad50lb9
set URL=https://api.stagingeb.com/v1/
cd src
'''


if __name__ == '__main__':
    print('Starting...')
    responses=apiConsult.get_organization_properties()
    for response in responses:
        for item in response:
            print(item['title'])