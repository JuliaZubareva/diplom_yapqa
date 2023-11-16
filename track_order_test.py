# Зубарева Юлия, 10-я когорта – Финальный проект. Инженер по тестированию Плюс
import sender_requests

# Создаем заказ и получаем по нему данные используя номер трека
def test_track_order():
    order_track_number = sender_requests.order_new()
    response = sender_requests.order_get(order_track_number.json()["track"])
    assert response.status_code == 200

