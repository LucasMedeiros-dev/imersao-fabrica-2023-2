# DESAFIO FÁBRICA DE SOFTWARE 2023.2 

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
   * [Clonando o projeto](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2#clonando-o-projeto)
   * [Instalando as dependências](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#instalando-as-dependencias)
   * [Instalação do template do Insomnia](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#instala%C3%A7%C3%A3o-do-template-do-insomnia)
   * [Configurando o settings.py](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#configurando-o-settingspy)
   * [Executando e Testando](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#executando-e-testando)
     * [Insomnia](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/blob/master/README.md#insomnia) 
 * [Estrutura de Arquivos](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/tree/master#dos-conte%C3%BAdos)
 * [SOBRE O TOKEN]()
 * [ASCII Art](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/tree/master#feito-por)
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

Em seguida aperte OK e depois Finish.  
Você será levado a essa tela.

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/e2b6a673-b173-4e45-a99b-984dedff7f06)  

Clique no com o botão direito do mouse em cima de Banco de Dados e depois criar novo banco de dados.
Coloque um nome para esse banco de dados e anote-o(O nome usado no video foi 'fabrica_de_autos').
Depois pressione ok.

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/2c611027-967c-4f31-92fe-1c545e5dee5e)

Agora vamos clonar o projeto.

## CLONANDO O PROJETO
Crie uma pasta clique com botão direito do mouse em "Open with Git Bash here"
deverá se abrir um terminal.
Neste terminal digitaremos o comando
~~~bash
git clone https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2.git Principal
~~~
Adendo: Nesse caso Principal será apenas o nome da pasta e não a branch que estamos utilizando.

Quando for concluido o processo de clonagem você verá o seguinte.

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/26a66532-5ec1-41b8-980d-b002b7d999bf)

Agora vamos ver como criar e ativar o Ambiente Virtual.
## CRIANDO E ATIVANDO UM AMBIENTE VIRTUAL

Na mesma pasta, abra o VSCODE com cmd e digite.
lembrando que o seu python deve estar no path.
~~~cmd
python -m venv venv
~~~
em seguida do mesmo terminal ative-o usando
~~~cmd
venv\Scripts\activate
~~~
o cursor do VSCODE deverá retornar
~~~
(venv) C:\...
~~~
Sendo assim você instalou e ativou com sucesso seu ambiente virtual.

## INSTALANDO AS DEPENDENCIAS
De dentro do seu Ambiente Virtual execute:
~~~
pip install -r requirements.txt
~~~
Pronto, você instalou as dependências.

## INSTALAÇÃO DO TEMPLATE DO INSOMNIA
Para instalar o template de requests, abra o Insomnia e ao lado do nome Collections clique no "+"
![Cllecots](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/fbb0ba10-21cf-429a-977c-2a71d6aa01df)

E insira o nome API Fabrica de Autos.
Será aberto um documento vazio.
Clique na casinha roxa para retornar ao menu principal.

![MenuPinsomia](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/a9545110-a174-4139-ac16-9f0842e4db15)

Em seguida na caixa com o nome API Fabrica, clique nos 3 pontinhos no canto superior direito e em seguida "import".

![Improt](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/bf9a6b22-d07f-4713-a6bd-84ee18998235)

Depois clique em "Choose a file"

E Na pasta onde você clonou o projeto, acesse Principal\Extras\Insomnia_template
haverá um arquivo chamado "template_api_insomnia.json"
Clique nele depois no botão abrir no canto inferior direito.
Se tudo deu certo aparecerá a seguinte tela.

![TelaTemplate](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/f6cc2859-dfc0-455a-872e-e4dd130474fc)

Aperte Scan e depois import.
Se tudo deu certo ao acessar novamente a "API Fabrica de autos"
ela terá essas opções.

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/e8ccdd2c-78ee-4e78-a240-c7a8d3a5c1a5)

Parabéns, importado o template da api, mas ainda não podemos usá-lo, temos que colocar o servidor no ar,
e para isso configurar o settings.py.

## CONFIGURANDO O SETTINGS.PY
No VSCODE acesse a pasta Principal\Fabrica_de_autos
E abra o arquivo settings.py
Navegue pelo arquivo até encontrar a variável "DATABASES"

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/f03efae6-949a-40c4-9566-4ff0267012be)

Algumas variáveis estarão como "TROQUE-ME", sendo assim devemos trocá-las de acordo com o nosso banco de dados,
caso você esteja seguindo a risca esse tutorial ele deverá estar assim.

![Fabrica_settigns](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/b76768dd-4b34-438c-bd69-217faf4bf12c)

Depois é só salvar e fechar o settings.py
Agora, vamos aprender a executar o projeto!
## EXECUTANDO E TESTANDO
Antes de prosseguir verifique se a venv está ativa.
Para executá-lo fazemos
~~~
python manage.py makemigrations
~~~
E em seguida
~~~
python manage.py migrate
~~~
O resultado deverá ser o seguinte após os dois códigos:

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/4b5cec02-5631-4453-8139-9c739a697343)

Depois criamos um usuário com o comando:
~~~
python manage.py createsuperuser
~~~
Inserimos as credenciais e guardamos as mesmas.
E depois executamos o projeto com:
~~~
python manage.py runserver
~~~
O terminal deverá exbiir algo assim:  

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/0106e8ec-4afb-420d-937f-39329f06a839)  

Depois é só navegar até o link exibido e testar os endpoints!
Parabéns o seu Backend está pronto!
### INSOMNIA
O template do insomnia provém uma forma simples e rápida de acessar todos os endpoints.
Além de acessar páginas especificas dos endpoints.

Exemplos:

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/8226b150-1a12-4bde-8bee-096d8c6130f9)  

![image](https://github.com/LucasMedeiros-dev/imersao-fabrica-2023-2/assets/39228907/c3793cea-9555-468c-9839-cb24d4e8bc91)


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
# SOBRE O TOKEN:
````
Foi tarde demais quando entendi como usar o token, já havia gravado toda a documentação, não havia tempo hábil para refazê-la toda.
Porém fiz outro projeto mais simples com intuito apenas de demonstrar o uso de autenticação por token, para registrar, logar e exibir o email.
````
link: ['Django-token-demo'](https://github.com/LucasMedeiros-dev/Django-token-demo)
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
