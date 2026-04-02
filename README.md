🚀 Santander Dev Week 2023 - ETL com Python
Este projeto foi desenvolvido como parte do desafio da Santander Dev Week 2023 na plataforma DIO. O objetivo é criar um pipeline de dados (ETL) que extrai IDs de usuários, simula/busca dados em uma API e gera mensagens de marketing personalizadas.

🛠️ Tecnologias Utilizadas
Python 3.14+

Pandas (Manipulação de dados)

Requests (Interação com APIs)

Virtualenv (venv) (Isolamento do ambiente)

📋 Fluxo do Projeto (ETL)
Extract (Extração): Leitura de um arquivo SDW2023.csv contendo IDs de usuários.

Transform (Transformação): Geração de mensagens personalizadas baseadas no saldo bancário e limite do cartão de crédito de cada cliente.

Load (Carga): Simulação do envio dos dados transformados de volta para a API (Processo de Update).