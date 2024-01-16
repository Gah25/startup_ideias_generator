 # Startup Ideias Generator

Este é um projeto Django que utiliza a API da OpenAI para gerar ideias inovadoras de startups com base em entradas do usuário.

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/startup-ideias-generator.git

1. Crie um ambiente virtual:
    ```bash
    python -m venv venv

2. Ative o ambiente virtual:
    No Windows:
    ```bash
    .\venv\Scripts\Activate

Ative o ambiente virtual:
    No Linux/Mac:
    ```bash
    source venv/bin/activate

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt

4.Configure a Chave da API OpenAI:
    Obtenha uma chave da API da OpenAI em https://platform.openai.com.
    Abra o arquivo ideas_generator/views.py no seu editor de código.
    Procure pela seguinte linha de código:

    openai.api_key = "Sua_Chave_OpenAI_Aqui"
        

Substitua "Sua_Chave_OpenAI_Aqui" pela chave da API que você obteve.
Salve o arquivo.
    
Executando o Projeto:
    python manage.py runserver
    
    Acesse http://127.0.0.1:8000/ideas_generator/ no seu navegador.

Uso
Abra o navegador e vá para http://127.0.0.1:8000/ideas_generator/.
Digite sua ideia no campo de entrada.
Clique no botão "Gerar Ideia" para obter sugestões de startups inovadoras.