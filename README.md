# ECO TECH BOT ♻️
#####   SOBRE
O Eco Tech Bot é um chatbot desenvolvido utilizando um modelo LLM com o intuito de ajudar as pessoas 
descartarem corretamente o lixo eletrônico, evitando assim problemas ambientais graves.

> [!NOTE]
>  - A presente documentação aborda detalhes tecnicos do ECO TECH BOT - um chatbot feito com base em IA generativa.

### ARQUITETURA 📝
> [!TIP]
> A Arquitetura da api do ECHO TECH BOT  foi baseada em MVC, model-view-controller, onde há dois controladores principais: `agentcontroller`  e `sessioncontroller` (controlador do Agente e controlador de sessão). Há apenas um serviço, o `botservices`, responsavel por fazer uma especie de ponte entre a API e a API do LLM. 

### ENDPOINTS 🚆
- POST /message 
> Modelo de requisição
```json
    {
        "user_message": "Olá! Eu me chamo (pessoa) e gostaria de saber pontos para descarte de lixo eletrônico em Araguaína."
    }

```
> Modelo de resposta para a requisição
```json
    {
        "bot_response": "Olá (pessoa), seja bem-vindo ao Waste Bot Agent 1.0! 👋\n\nEntendo que você procura por locais para descartar seu lixo eletrônico em Araguaína. ♻️\n\nEm Araguaína, você pode encontrar pontos de coleta de lixo eletrônico nos seguintes locais:\n\n**Supermercado Atacadão:**\n- Av. Amazílio Correa Camargo Neto, nº 140, no Residencial Camargo.\n\n**Metalsul:**\n- Rua Aquarela Musical, nº 153, no Parque dos Sonhos Dourados.\n\n**Loja Vivo:**\n- Rua 19 de Novembro, nº 29, no Centro.\n\nLembre-se de verificar os horários de funcionamento e os tipos de materiais que eles aceitam antes de levar seus eletrônicos.\n\nEspero ter ajudado! 😄\n"
    }
```
-----
 - GET /about 
```json
    {
        "about_bot": "Eletronic Waste Agent v1.0"
    }          
```
> [!TIP]
> Rota responsavel por exibir as informações sobre o bot [versão, nome, etc].
-----
- GET /session

```json
    {  

        "session_id": "e9e1512db809db6f6c5cc4542c9de274"

    }
```
> [!TIP]
> O endpoint acima é responsável por buscar o id da sessão, garantindo que cada sessão seja única para cada um dos usuários.
-----
### Exemplo de uso
https://github.com/user-attachments/assets/5f42a245-dd74-464a-aa7f-0830c7805e4f

