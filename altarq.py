##################flag a##############################################################################################################
arquivo = open('/local/do/arquivo/arquivo.txt', 'a', encoding='utf-8')                #abre o arquivo para alteração                 #
arquivo.write('Teste do local de gravação de dados')                                  #escreve o texto ao final do arquivo           #
arquivo.close()                                                                       #fecha o arquivo                               #
##################flag r##############################################################################################################
arq = open('/local/do/arquivo/arquivo.txt', 'r', encoding='utf-8')                    #abre o arquivo para leitura                   #
texto = arq.read()                                                                    #salva o conteudo do arquivo na variavel texto #
print(texto)                                                                          #exibe as informaçoes salvas na variavel texto #
arq.close()                                                                           #fecha o arquivo                               #
##################flag r com a flag b#################################################################################################
arq = open('/local/do/arquivo/arquivo.txt', 'rb', encoding='utf-8')                   #abre o arquivo binario para leitura           # 
dados = arq.read()                                                                    #salva o conteudo do arquivo na variavel dados #
print(dados)                                                                          #exibe as informações salvas na variavel dados #
arq.close()                                                                           #fecha o arquivo                               #
##################flag r+##########################################################################################                  #
arq = open('/local/do/arquivo/arquivo.txt', 'r+', encoding='utf-8')                   #abre o arquivo para leitura e alteração       #
arq.write('teste outra linha')                                                        #sobrescreve o inicio do arquivo com o texto   #
texto = arq.read()                                                                    #salva o conteudo do arquivo na variavel texto #
print(texto)                                                                          #exibe as informações salvas na variavel texto #
arq.close()                                                                           #fecha o arquivo                               #
######################################################################################################################################
