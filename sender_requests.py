import requests
import configuration
import data

# функция запроса на получения заказа
def order_get(track_number):
    return requests.get(configuration.API_URL + configuration.ORDER_GET_PATH,
                        params={"t": track_number}
    )

# функция запроса на создание заказа
def order_new():
    return requests.post(configuration.API_URL + configuration.ORDER_CREATE_PATH,
                         json=data.order_data,
                         headers=data.headers
    )


