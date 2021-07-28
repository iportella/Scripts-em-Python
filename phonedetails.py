###########################################################################################################################################################################
# Script para descobrir se o numero de celular é valido, se existe e exibir a geolocalização em que ele está registrado,                                                  #
# qual fuso horário do local em que ele está registrado e qual empresa de telefonia tem seu direito.                                                                      #
# Deve ser feita a instalação do módulo phonenumbers: pip install phonenumbers.                                                                                           #
# Executar o script por meio do comando: python3 nomedoscript.py                                                                                                          #
# Para números de alguns países ainda não é possível exibir qual empresa de telefonia detém os direitos do número. Ex: Brasil.                                            #
###########################################################################################################################################################################

# -*- coding: utf-8 -*- #codificação para ser feito a leitura de caracteres acentuados e especiais

import phonenumbers #importando o modulo phonenumbers                                                                                                                     #
from phonenumbers import carrier, geocoder, timezone #no modulo phone number, importando a empresa de telefonia, geolocalização e fuso horario                            #
celular = input('Digite o numero do telefone com o codigo do País: ') #solicitando ao usuário o numero de telefone com o codigo do país                                   #
celular = phonenumbers.parse(celular) #analisa o numero digitado com o módulo phonenumbers                                                                                #
print('Fuso horario do numero: ', timezone.time_zones_for_number(celular)) #exibe o fuso horário em que o número de telefone está registrado                              #
print('Empresa de telefonia do numero do telefone: ', carrier.name_for_number(celular, 'en')) #exibe a empresa em que o número de telefone está registrado                #
print('Localização em que o numero está registrado: ', geocoder.description_for_number(celular, 'en')) #exibe a geolocalização em que o número de telefone foi resigtrado #
print('Numero de telefone valido: ', phonenumbers.is_valid_number(celular)) #exibe se o numero de celular digitado é válido                                               #
print('Checando a possibilidade do numero: ', phonenumbers.is_possible_number(celular)) #exibe se o numero de celular digitado é registrado                               #