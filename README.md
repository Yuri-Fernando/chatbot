# Chatbot
TCC de Pós em Engenharia de Software FAMEESP
Descrição do Repositório

Este repositório contém três versões de um chatbot, cada uma com diferentes níveis de complexidade e capacidade de resposta, com o objetivo de demonstrar a construção e implementação de chatbots utilizando abordagens simples, aprendizado de máquina local e integração com APIs externas.

As versões incluem:

    Chatbot 1 (Respostas Predefinidas): Esta versão é a mais simples e não exige treinamento ou uso de modelos de inteligência artificial complexos. O chatbot utiliza um conjunto fixo de respostas predefinidas armazenadas em um dicionário. Quando o usuário envia uma pergunta, o servidor Flask consulta este dicionário e retorna a resposta correspondente. Ideal para aplicações com perguntas limitadas e bem definidas.

    Chatbot 2 (Aprendizado Local): Esta versão incorpora aprendizado de máquina para gerar respostas com base em dados previamente treinados. Utiliza um modelo simples de aprendizado de máquina treinado localmente, permitindo ao chatbot aprender e se adaptar a novas perguntas. Essa abordagem oferece maior flexibilidade e autonomia em relação a dados externos, mas exige mais recursos computacionais para o treinamento do modelo.

    Chatbot 3 (Integração com APIs Externas): A versão mais avançada do chatbot, que utiliza APIs externas, como o OpenAI GPT e o Google Dialogflow, para fornecer respostas. A principal vantagem dessa versão é que ela se beneficia de poderosos modelos de IA, sem a necessidade de treinamento local. O chatbot apenas envia as perguntas para a API e recebe as respostas geradas pelo modelo de IA. Ideal para obter respostas mais inteligentes e naturais.

Estrutura de Arquivos

    chat1/: Contém os arquivos necessários para a versão 1 do chatbot, que utiliza respostas predefinidas.
        chat1.py: Código do chatbot com respostas fixas.
        templates/index1.html: Página HTML para interagir com o chatbot.

    chat2/: Contém os arquivos necessários para a versão 2 do chatbot, com aprendizado local.
        chat2.py: Código do chatbot com aprendizado de máquina local.
        templates/index2.html: Página HTML para interagir com o chatbot.

    chat3/: Contém os arquivos necessários para a versão 3 do chatbot, com integração com APIs externas.
        chat3.py: Código do chatbot com integração com APIs externas.
        templates/index3.html: Página HTML para interagir com o chatbot.

Personalização

    Versão 1: Edite o dicionário de perguntas e respostas no código para personalizar as respostas do chatbot.
    Versão 2: Atualize o conjunto de dados de treinamento e ajuste o modelo de aprendizado de máquina de acordo com as necessidades do seu projeto.
    Versão 3: Configure as chaves de API para a integração com os serviços externos (como OpenAI GPT ou Dialogflow) e ajuste o modelo de conversa conforme necessário.

Contribuições

Se você tiver sugestões de melhorias ou encontrar algum erro, sinta-se à vontade para abrir um "issue" ou criar um "pull request". Contribuições são sempre bem-vindas!
