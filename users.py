import requests

# Definindo a classe users
class Users:
   
    # URL do serviço REST
    base_url = "http://127.0.0.1:8000/users/"

    def list(self):
        url = self.base_url
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("ID inválido")


    def delete(self, user_name):
        url = self.base_url+str(user_name)
        response = requests.delete(url)

        if response.status_code == 204:
            return True
        else:
            raise ValueError("ID inválido")

    def create(self,user_name):
        url = self.base_url

        response = requests.post(url, json=user_name)

        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError("Problema na execução")

    def update(self, user_name):
        url = self.base_url+str(user_name)

        response = requests.patch(url, json=user_name)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("Problema na execução")