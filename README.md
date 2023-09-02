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
 
Vá até [baixar MySQL](https://dev.mysql.com/downloads/installer/) e selecione download.  

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/5c704811-12d5-47a3-88b0-eecb31fad0ad)

Depois selecione "No thanks, just start my download."  

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/69dd6bf4-4aa1-418e-b8b0-e53fe33db1cc)

Quando o download for concluido abra o arquivo baixado.
Certifique-se de que apenas server only está marcado e clique next.  

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/59da5445-c81f-4254-8d95-9afee18d4bad)

Depois clique execute.

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/7c79c68f-29a9-4f50-a284-ec60a45a77d2)

Ao aparecer o Tick verde ao lado, pressione next.  

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/16b95a6f-1093-4454-854b-cd76ae089ae3)

Pressione Execute novamente e em seguida next, até aparecer a tela de configuração.
Certifique-se de que config type está "Development Computer" e Anote o valor que está em "Port", por padrão é 3306.  

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/44d57f65-8d06-49c2-8430-822d691ed672)

Quando aparecer uma tela chamada Authentication method deixe marcado o padrão "Use Strong Password Encrypton" e depois next.

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/237135f0-e35a-43ab-8a53-057e232c3290)

Em seguida crie uma senha para o usuário root (No video foi usado "root123", nunca use uma senha fraca em produção) preenchendo os dois campos de senha disponíveis. E caso queira adicione mais um usuário com as permissões DB Admin.
Foi criado em seguida um usuario chamado "teste" com a senha "root123", lembre-se de anotar essas informações caso use valores diferentes.  

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/fec064a6-31b5-4fc4-aaac-a6b9e1482354)  
![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/99c98697-7b2c-4e7b-b4b8-224f979a26ad)

Na tela seguinte pressione next.  
E em Server File Permissions pressione next.
E Em seguida execute e aguarde até todos os ticks ficarem verdinhos.

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/a37db426-89f5-4bee-a827-071bbaf55012)


Em seguida pressionamos finish e concluimos a instalação do Banco de Dados, agora vamos para a preparação.

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/57c8da7b-f42f-4c33-b7ee-61c7ec1cfc42)


## PREPARANDO O BANCO DE DADOS

Baixe a ferramenta [DBeaver](https://dbeaver.io/download/) e faça a instalação.  

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/f5cc902c-f786-434c-be21-645301b4885c)

Ao abrir o DBeaver selecione a tomadinha com um + para adicionar um banco de dados.

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/a8f71202-d704-4ce7-a8f6-3c120e112063)

Selecione MySQL

![mysql](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/8e7a119e-bdd9-47f3-884e-56f00b01dc11)

E acaso ele pergunte se deseja instalar o driver, realize a instalação do mesmo.  
Em seguida é hora de carregar as credenciais.  
Se você alterou a port na instalação do sql coloque a mesma porta a qual usou anteriormente.  
Seu usuário será root.
E se caso tiver colocado sua senha igual a minha, ela será root123.


![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/ae7b3553-45f6-4a3d-a9b0-5692e4ae69de)

Antes de testar vá na aba Driver Properties e altere "allowPublicKeyRetrieval" de false para true.

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/ff63df16-6296-46ad-8487-b17bc4bbb655)
![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/61c4b4ef-c407-4f33-bf8a-c417b51823b3)

Em seguida volte para Principal e clique em Testar conexão.
Se tudo deu certo a mensagem a seguir deverá aparecer.

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/d596f331-1547-4ec7-a2ef-56e2249fc334)


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
