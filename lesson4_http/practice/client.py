import requests


# TODO: 1) поменять реализацию обработчика get-запроса внутри http_server, так, чтобы поддерживался json (есть тест)
#       2) реализовать метод do_POST так, чтобы получился echo-сервер(отвечает тем же, что в него поступает)
#       3) написать тесты на echo-сервер
#


def json_reader(resp: requests.Response):
    pass


def bytes_reader(resp: requests.Response):
    return {'status': resp.status_code, 'content': resp.content}


if __name__ == "__main__":
    url = "http://localhost:8080"
    response = requests.get(url)

    print(json_reader(response))
    print(bytes_reader(response))
