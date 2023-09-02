# DESFAIO FÁBRICA DE SOFTWARE 2023.2 

O intuito do desafio é criar uma api que simula uma Fábrica de software.  
O usuário é responsável por administrar a api de um software de vendas.

# INDICE DA BRANCH
 * [Introdução](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/tree/master#desafio-f%C3%A1brica-de-software-20232)
 * [Indice](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/tree/master#indice-da-branch)
 * [Instalação](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#instala%C3%A7%C3%A3o)
   * [Video guia](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#video-guia)
   * [Instalando o Banco de Dados](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#instala%C3%A7%C3%A3o-do-banco-de-dados)
   * [Preparando o Banco de Dados](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#preparando-o-banco-de-dados)
   * [Criando um Ambiente Virtual](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#criando-um-ambiente-virtual)
   * [Instalando as dependências](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#instalando-as-dependencias)
   * [Instalação do template do Insomnia](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#instala%C3%A7%C3%A3o-do-template-do-insomnia)
   * [Configurando o settings.py](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#configurando-o-settingspy)
   * [Executando e Testando](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#executando-e-testando)
     * [Insomnia](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#insomnia) 
 * [Usando o projeto]()
 * [Estrutura de Arquivos](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/tree/master#dos-conte%C3%BAdos-desta-branch)  
# INSTALAÇÃO
## Video Guia


https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/b033197c-b83e-4c16-9b78-3ba88cead4f2


## INSTALAÇÃO DO BANCO DE DADOS
## PREPARANDO O BANCO DE DADOS
## CRIANDO UM AMBIENTE VIRTUAL
## INSTALANDO AS DEPENDENCIAS
## INSTALAÇÃO DO TEMPLATE DO INSOMNIA
## CONFIGURANDO O SETTINGS.PY
## EXECUTANDO E TESTANDO
### INSOMNIA

# DOS CONTEÚDOS
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
# FEITO POR:
```
      ██╗     ██╗   ██╗ ██████╗ █████╗ ███████╗    ███╗   ███╗
      ██║     ██║   ██║██╔════╝██╔══██╗██╔════╝    ████╗ ████║
      ██║     ██║   ██║██║     ███████║███████╗    ██╔████╔██║
      ██║     ██║   ██║██║     ██╔══██║╚════██║    ██║╚██╔╝██║
      ███████╗╚██████╔╝╚██████╗██║  ██║███████║    ██║ ╚═╝ ██║
      ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝
      Lucas Medeiros, Estudante de Ciências da Computação, Unipê.
 ```
