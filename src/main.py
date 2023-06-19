from adapter.easybroker import apiConsult

if __name__ == '__main__':
    print('Starting...')
    responses=apiConsult.get_organization_properties()
    for response in responses:
        for item in response:
            print(item['title'])