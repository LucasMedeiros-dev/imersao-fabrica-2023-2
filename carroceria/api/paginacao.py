from rest_framework.pagination import PageNumberPagination

# Cria a classe que define a paginacao


class PaginacaoPadrao(PageNumberPagination):
    '''Classe padrão de paginação.\n
    `page_size`: Quantidade máxima de items por página\n
    `page_size_query_param`: Parâmetro recebido da página\n
    `max_page_size`: Maior página possível
    '''
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000
