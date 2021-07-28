############################################################################################################################################################################################
# Script que realiza a pesquisa de um termo na Wikipedia de acordo com a escolha de idioma do usuário.                                                                                     #
# Desenvolvido por Igor Portella Pereira Lopes                                                                                                                                             #
# Data: 28/07/2021                                                                                                                                                                         #
# Deve ser feita a instalação do módulo wikipedia: pip install wikipedia.                                                                                                                  #
# Executar o script por meio do comando: python3 nomedoscript.py                                                                                                                           #
############################################################################################################################################################################################

# -*- coding: utf-8 -*- #codificação para ser feito a leitura de caracteres acentuados e especiais                                                                                         #
import wikipedia #importa o modulo wikipedia                                                                                                                                               #
idioma = input('Digite o idioma em que se quer fazer a pesquisa: \n1- para portugues \n2- para ingles \n3- para espanhol \n') #solicita ao usuário a escolha de um idioma pré definido     #
if idioma == '1':
    wikipedia.set_lang('pt') #define que o idioma da pagina a ser pesquisada é em português                                                                                                #
    termo = input('Digite o termo a ser pesquisado: ')  # solicita ao usuário o termo a ser pesquisado                                                                                     #
    wikipedia.search(termo)  # busca o termo desejado na pagina da desejada                                                                                                                #
    py = wikipedia.page(termo)  # cria um objeto da pagina desejada                                                                                                                        #
    print(py.url)  # exibe a url da pagina da wikipedia em que se encontra o termo a ser pesquisado                                                                                        #
    print(py.title)  # exibe o titulo da pesquisa                                                                                                                                          #
    print(wikipedia.summary(termo, sentences=1))
    conteudo = input('Deseja exibir o conteúdo total da pagina? \n1- sim\n 2- nao\n')
    if conteudo == '1':
        print(py.content)  # exibe o conteúdo da pagina pesquisada                                                                                                                         #
        print('Pesquisa Concluída !')
    else:
        print('Pesquisa Concluída! ')
elif idioma == '2':
    wikipedia.set_lang('en') #define que o idioma da pagina a ser pesquisada é em inglês                                                                                                   #
    termo = input('Digite o termo a ser pesquisado: ')  # solicita ao usuário o termo a ser pesquisado                                                                                     #
    wikipedia.search(termo)  # busca o termo desejado na pagina da desejada                                                                                                                #
    py = wikipedia.page(termo)  # cria um objeto da pagina desejada                                                                                                                        #
    print(py.url)  # exibe a url da pagina da wikipedia em que se encontra o termo a ser pesquisado                                                                                        #
    print(py.title) # exibe o titulo da pesquisa                                                                                                                                           #
    print(wikipedia.summary(termo, sentences=1))
    conteudo = input('Deseja exibir o conteúdo total da pagina? \n1- sim\n 2- nao\n')
    if conteudo == '1':
        print(py.content)  # exibe o conteúdo da pagina pesquisada                                                                                                                         #
        print('Pesquisa Concluída !')
    else:
        print('Pesquisa Concluída! ')
elif idioma == '3':
    wikipedia.set_lang('es') #define que o idioma da pagina a ser pesquisada é em espanhol                                                                                                 #
    termo = input('Digite o termo a ser pesquisado: ')  # solicita ao usuário o termo a ser pesquisado                                                                                     #
    wikipedia.search(termo)  #busca o termo desejado na pagina da desejada                                                                                                                 #
    py = wikipedia.page(termo)  #cria um objeto da pagina desejada                                                                                                                         #
    print(py.url)  # exibe a url da pagina da wikipedia em que se encontra o termo a ser pesquisado                                                                                        #
    print(py.title)  # exibe o titulo da pesquisa                                                                                                                                          #
    print(wikipedia.summary(termo, sentences=1))
    conteudo = input('Deseja exibir o conteúdo total da pagina? \n1- sim\n 2- nao\n')                                                                                                      #
    if conteudo == '1':
        print(py.content)  # exibe o conteúdo da pagina pesquisada                                                                                                                         #
        print('Pesquisa Concluída !')
    else:
        print('Pesquisa Concluída! ')
else:
    print('Idioma não cadastrado') #caso nao seja escolhida nenhuma das opções, o programa exibe a mensagem e interrompe                                                                   #


