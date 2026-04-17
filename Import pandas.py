#----- Extract ----- Importando o arquivo csv usando a biblioteca pandas
#---json publico para teste
import pandas as pd
import requests
import json
import openai
base1 = 'https://jsonplaceholder.typicode.com/users'
openai.api_key ='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'
client = openai.OpenAI(api_key=openai.api_key)

#---Carrega o CSV com os IDs dos usuários (1 a 6)
df = pd.read_csv('D:/Estudos/ETL/base2.csv')
usuario_ids = df['id'].tolist()
#print(usuario_ids)

#---Função para pegar os dados da API, passando os IDs dos usuários
#--- Só retorna os dados se a resposta for bem-sucedida (status code 200)
def get_user(id):
   response=requests.get(f'{base1}/{id}')
   return response.json() if response.status_code == 200 else None

#---Usa list comprehension para criar uma lista de usuários, filtrando apenas os que foram encontrados na API
user = [user for id in usuario_ids if (user := get_user(id)) is not None]
print(json.dumps(user, indent=2))


#---- TRANSFORAMAÇÃO -----

#--- Função para gerar textos usando API do OpenAI, passando o nome do usuário para personalizar a mensagem
def generate_ai_news(user):
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "Você é um especialista em marketing bancário."},
            {"role": "user", "content": f"Crie uma mensagem para {user['name']} sobre a importancia dos investimentos (máximo de 100 caracteres)"}
        ],
        max_tokens=100
    )
    return response.choices[0].message.content.strip('\"')

#--- Percorre a lista de usuarios e adiciona a mensagem gerada
for user in user:
    news = generate_ai_news(user)
    print(f"Mensagem para {user['name']}: {news}")
    user['news'].append({
        "Mensagem": news
    })

#---- LOAD -----
#--- Função para atualizar os dados do usuário na API usando o método PUT, passando o ID do usuário e os dados atualizados
def update_user(user):
    response = requests.put(f'{base1}/{user["id"]}', json=user)
    return True if response.status_code == 200 else False

# --- Percorre a lista de usuários e atualiza os dados na API, imprimindo o resultado de cada atualização
for user in user:
    sucess = update_user(user)
    print(f"Usuario {user['name']} atualizado: {'Sucesso' if sucess else 'Falha'}")