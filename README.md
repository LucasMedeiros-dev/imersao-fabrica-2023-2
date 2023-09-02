# Desafio Fábrica de Software 2023.2 

O intuito do desafio é criar uma api que simula uma Fábrica de software.  
O usuário é responsável por administrar a api de um software de vendas.

# Indice da branch
 * [Introdução](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/tree/master#desafio-f%C3%A1brica-de-software-20232)
 * [Indice](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/tree/master#indice-da-branch)
 * [Instalação]()
   * Video guia 
   * Instalando o Banco de Dados
   * Preparando o Banco de Dados
   * Criando um Ambiente Virtual
   * Instalando as dependências
   * Instalação do template do Insomnia
   * Executando e Testando
 * [Usando o projeto]()
 * [Estrutura de Arquivos](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/tree/master#dos-conte%C3%BAdos-desta-branch)
## Dos conteúdos desta branch.
 Estrutura de arquivos:
```
.
├── Fabrica de autos                         # Pasta do projeto gerada pelo Django.
│   └── __init__.py                          # Arquivos autogerados pelo django.
│   └── asgi.py                              # Arquivos autogerados pelo django.
│   └── settings.py                          # Arquivo de configurações do projeto.
│   └── urls.py                              # Arquivo de configuração das urls do projeto.
│   └── wsgi.py                              # Arquivos autogerados pelo django.
├── carroceria
│   ├── api                                  # Pasta que contém arquivos de configiuração do endpoint /carroceria/
│   │   └── paginacao.py                     # Define as configurações de paginação deste endpoint.
│   │   └── serializers.py                   # Define as configurações dos serializadores deste endpoint.
│   │   └── viewsets.py                      # Define as configurações dos viewsets deste endpoint.
│   ├── migrations                           # Arquivos autogerados pelo django.
│   │   └── ...                              # Arquivos autogerados de migração da DB.
│   ├── __init__.py                          # Arquivos autogerados pelo django.
│   ├── admin.py                             # Arquivos de realização do registro na interface web admin django.
│   ├── apps.py                              # Arquivos autogerados pelo django.
│   ├── models.py                            # Arquivos de modelos do Banco de Dados.
│   ├── tests.py                             # Arquivos de testes, não utilizado neste projeto.
│   ├── urls.py                              # Arquivos de configuração da url, define o endpoint.
│   └── views.py                             # Arquivo de views autogerados pelo django, não utilizado.
├── extras                                   # Arquivos incluidos que não fazem parte do projeto em sí.
│   └── Insomnia_template                    # Template para rápido acesso a todas as funções da api.
│       └── template_api_insomnia.json       # Arquivo de template.
├── motor
│   ├── api                                  # Pasta que contém arquivos de configiuração do endpoint /motor/
│   │   └── paginacao.py                     # Define as configurações de paginação deste endpoint.
│   │   └── serializers.py                   # Define as configurações dos serializadores deste endpoint.
│   │   └── viewsets.py                      # Define as configurações dos viewsets deste endpoint.
│   ├── migrations                           # Arquivos autogerados pelo django.
│   │   └── ...                              # Arquivos autogerados de migração da DB.
│   ├── __init__.py                          # Arquivos autogerados pelo django.
│   ├── admin.py                             # Arquivos de realização do registro na interface web admin django.
│   ├── apps.py                              # Arquivos autogerados pelo django.
│   ├── models.py                            # Arquivos de modelos do Banco de Dados.
│   ├── tests.py                             # Arquivos de testes, não utilizado neste projeto.
│   ├── urls.py                              # Arquivos de configuração da url, define o endpoint.
│   └── views.py                             # Arquivo de views autogerados pelo django, não utilizado.
├── opcionais
│   ├── api                                  # Pasta que contém arquivos de configiuração do endpoint /opcionais/
│   │   └── paginacao.py                     # Define as configurações de paginação deste endpoint.
│   │   └── serializers.py                   # Define as configurações dos serializadores deste endpoint.
│   │   └── viewsets.py                      # Define as configurações dos viewsets deste endpoint.
│   ├── migrations                           # Arquivos autogerados pelo django.
│   │   └── ...                              # Arquivos autogerados de migração da DB.
│   ├── __init__.py                          # Arquivos autogerados pelo django.
│   ├── admin.py                             # Arquivos de realização do registro na interface web admin django.
│   ├── apps.py                              # Arquivos autogerados pelo django.
│   ├── models.py                            # Arquivos de modelos do Banco de Dados.
│   ├── tests.py                             # Arquivos de testes, não utilizado neste projeto.
│   ├── urls.py                              # Arquivos de configuração da url, define o endpoint.
│   └── views.py                             # Arquivo de views autogerados pelo django, não utilizado.
├── .gitignore                               # Arquivo com exclusões do repositório.
├── README.md                                # Arquivo com toda documentação do projeto.
├── manage.py                                # Arquivo gerado pelo Django para sua administração.
└── requirements.txt                         # Bibliotecas necessárias para executar esse projeto.
````
