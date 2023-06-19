import requests
import os


class apiConsult:

    def get_organization_properties():
        '''
        Retrieves a list of organization properties from an API endpoint.

        Returns:
            list: A list of organization properties.
        '''
        EASYBROKER_CLIENT_ID = os.environ.get('EASYBROKER_CLIENT_ID')
        BASE_URL = os.environ.get('URL')
        page = 1
        list_responses = []
        headers = {
            'accept': 'application/json',
            'X-Authorization': EASYBROKER_CLIENT_ID
        }
        exit = True
        while exit:
            url = '{}properties?page={}&limit=50'.format(BASE_URL, page)
            page += 1
            response = requests.get(url, headers=headers)
            response_dict = response.json()
            if len(response_dict['content']) != 0:
                list_responses.append(response_dict['content'])
            else:
                exit = False
        return list_responses
