exemplo_primeiro_octeto = '1-255'
exemplo_demais_octetos = '0-255'
exemplo_rede = '8-30'
ip_user = rede_user = 0
limite_octetos_final = 4
rede_tamanho_minimo = 8
rede_tamanho_maximo = 32
lista_octetos_validos_nao_validos = []
sair = 'Q'
continuar = 'ENTER'
decisao_user = None

# VERIFICA QUANTOS OCTETO FORAM DIGITADOS
def verificar_octetos(ip_user):
  ponto = definir_primeiro_octeto = 0
  quantidade_octetos_digitados = 4
  definir_segundo_octeto = 1
  definir_terceiro_octeto = 2
  limite_octetos = 4
  lista_primeiro_octeto = []
  lista_segundo_octeto = []
  lista_terceiro_octeto = []
  lista_quarto_octeto = []
  separar_octetos = '.'
  primeiro_octeto_digitado = segundo_octeto_digitado = terceiro_octeto_digitado = quarto_octeto_digitado = False

  # SEPARA CADA OCTETO POR PONTOS, ADICIONANDO CADA DIGITO EM UMA LISTA
  for ip in ip_user:
    if(ip == separar_octetos):
      ponto += 1
    else:
      if(ponto == definir_primeiro_octeto):
        lista_primeiro_octeto.append(ip)
      elif(ponto == definir_segundo_octeto):
        lista_segundo_octeto.append(ip)
      elif(ponto == definir_terceiro_octeto):
        lista_terceiro_octeto.append(ip)
      else:
        lista_quarto_octeto.append(ip)

  # DEFINE QUANTOS E QUAIS OCTETOS FORAM DIGITADOS
  if(len(lista_primeiro_octeto) == 0):
    quantidade_octetos_digitados -= 1
    if(len(lista_segundo_octeto) == 0):
      quantidade_octetos_digitados -= 1
      if(len(lista_terceiro_octeto) == 0):
        quantidade_octetos_digitados -= 1
        if(len(lista_quarto_octeto) == 0):
          # NENHUM OCTETO FOI DIGITADO
          quantidade_octetos_digitados -= 1
        else:
          # 1º, 2º E 3º OCTETOS NÃO FORAM DIGITADOS
          quarto_octeto_digitado = True
      elif(len(lista_quarto_octeto) == 0):
        # 1º, 2º E 4º OCTETOS NÃO FORAM DIGITADOS
        quantidade_octetos_digitados -= 1
        terceiro_octeto_digitado = True
      else:
        # 1º E 2º OCTETOS NÃO FORAM DIGITADOS
        terceiro_octeto_digitado = quarto_octeto_digitado = True
    elif(len(lista_terceiro_octeto) == 0):
      quantidade_octetos_digitados -= 1
      if(len(lista_quarto_octeto) == 0):
        # 1º, 3º E 4º OCTETOS NÃO FORAM DIGITADOS
        quantidade_octetos_digitados -= 1
        segundo_octeto_digitado = True
      else:
        # 1º E 3º OCTETOS NÃO FORAM DIGITADOS
        segundo_octeto_digitado = quarto_octeto_digitado = True
    elif(len(lista_quarto_octeto) == 0):
      # 1º E 4º OCTETOS NÃO FORAM DIGITADOS
      quantidade_octetos_digitados -= 1
      segundo_octeto_digitado = terceiro_octeto_digitado = True
    else:
      # 1º OCTETO NÃO FOI DIGITADO
      segundo_octeto_digitado = terceiro_octeto_digitado = quarto_octeto_digitado = True
  elif(len(lista_segundo_octeto) == 0):
    quantidade_octetos_digitados -= 1
    if(len(lista_terceiro_octeto) == 0):
      quantidade_octetos_digitados -= 1
      if(len(lista_quarto_octeto) == 0):
        # 2º, 3º E 4º OCTETOS NÃO FORAM DIGITADOS
        quantidade_octetos_digitados -= 1
        primeiro_octeto_digitado = True
      else:
        # 2º E 3º OCTETOS NÃO FORAM DIGITADOS
        primeiro_octeto_digitado = quarto_octeto_digitado = True
    elif(len(lista_quarto_octeto) == 0):
      # 2º E 4º OCTETOS NÃO FORAM DIGITADOS
      quantidade_octetos_digitados -= 1
      primeiro_octeto_digitado = terceiro_octeto_digitado = True
    else:
      # 2º OCTETO NÃO FOI DIGITADO
      primeiro_octeto_digitado = terceiro_octeto_digitado = quarto_octeto_digitado = True
  elif(len(lista_terceiro_octeto) == 0):
    quantidade_octetos_digitados -= 1
    if(len(lista_quarto_octeto) == 0):
      # 3º E 4º OCTETOS NÃO FORAM DIGITADOS
      quantidade_octetos_digitados -= 1
      primeiro_octeto_digitado = segundo_octeto_digitado = True
    else:
      # 3º OCTETO NÃO FOI DIGITADO
      primeiro_octeto_digitado = segundo_octeto_digitado = quarto_octeto_digitado = True
  elif(len(lista_quarto_octeto) == 0):
    # 4º OCTETO NÃO FOI DIGITADO
    quantidade_octetos_digitados -= 1
    primeiro_octeto_digitado = segundo_octeto_digitado = terceiro_octeto_digitado = True
  elif(ponto >= limite_octetos):
    # FORAM DIGITADOS MAIS DE 4 OCTETOS
    quantidade_octetos_digitados = ponto + 1
  else:
    primeiro_octeto_digitado = segundo_octeto_digitado = terceiro_octeto_digitado = quarto_octeto_digitado = True

  lista_status_octetos = [primeiro_octeto_digitado, segundo_octeto_digitado, terceiro_octeto_digitado, quarto_octeto_digitado]

  return lista_status_octetos, lista_primeiro_octeto, lista_segundo_octeto, lista_terceiro_octeto, lista_quarto_octeto, quantidade_octetos_digitados

# VERIFICA QUAIS OCTETOS TEM SOMENTE NÚMEROS
def converter_ip(primeiro_octeto, segundo_octeto, terceiro_octeto, quarto_octeto):
  primeiro_octeto_so_numeros = segundo_octeto_so_numeros = terceiro_octeto_so_numeros = quarto_octeto_so_numeros = None
  range_ord_min = 48
  range_ord_max = 57
  quantidade_octetos_so_numeros = 4
  lista_octetos_validos_nao_validos = []

  # FAZ A VERIFICAÇÃO COM BASE NA TABELA ASCII, USANDO DECIMAL
  for digito_primeiro_octeto in primeiro_octeto:
    if(ord(digito_primeiro_octeto) in range(range_ord_min, range_ord_max + 1)):
      primeiro_octeto_so_numeros = True
    else:
      primeiro_octeto_so_numeros = False
      quantidade_octetos_so_numeros -= 1
      break

  # FAZ A VERIFICAÇÃO COM BASE NA TABELA ASCII, USANDO DECIMAL
  for digito_segundo_octeto in segundo_octeto:
    if(ord(digito_segundo_octeto) in range(range_ord_min, range_ord_max + 1)):
      segundo_octeto_so_numeros = True
    else:
      segundo_octeto_so_numeros = False
      quantidade_octetos_so_numeros -= 1
      break

  # FAZ A VERIFICAÇÃO COM BASE NA TABELA ASCII, USANDO DECIMAL
  for digito_terceiro_octeto in terceiro_octeto:
    if(ord(digito_terceiro_octeto) in range(range_ord_min, range_ord_max + 1)):
      terceiro_octeto_so_numeros = True
    else:
      terceiro_octeto_so_numeros = False
      quantidade_octetos_so_numeros -= 1
      break

  # FAZ A VERIFICAÇÃO COM BASE NA TABELA ASCII, USANDO DECIMAL
  for digito_quarto_octeto in quarto_octeto:
    if(ord(digito_quarto_octeto) in range(range_ord_min, range_ord_max + 1)):
      quarto_octeto_so_numeros = True
    else:
      quarto_octeto_so_numeros = False
      quantidade_octetos_so_numeros -= 1
      break

  lista_octetos_validos_nao_validos = [primeiro_octeto_so_numeros, segundo_octeto_so_numeros, terceiro_octeto_so_numeros, quarto_octeto_so_numeros]

  return lista_octetos_validos_nao_validos, quantidade_octetos_so_numeros

# VERIFICA QUAL OCTETO ESTÁ NA FAIXA IDEAL
def verificar_faixa_ip(primeiro_octeto, segundo_octeto, terceiro_octeto, quarto_octeto):
  primeiro_octeto_na_faixa = segundo_octeto_na_faixa = terceiro_octeto_na_faixa = quarto_octeto_na_faixa = False
  limite_numero_maximo = 255
  limite_numero_minimo = 1
  quantidade_octetos_faixa_ideal = 4
  lista_octetos_faixa = []

  # PRIMEIRO OCTETO É O ÚNICO QUE NÃO PODE SER 0
  if((primeiro_octeto < limite_numero_minimo) or (primeiro_octeto > limite_numero_maximo)):
    quantidade_octetos_faixa_ideal -= 1
    if(segundo_octeto > limite_numero_maximo):
      quantidade_octetos_faixa_ideal -= 1
      if(terceiro_octeto > limite_numero_maximo):
        quantidade_octetos_faixa_ideal -= 1
        if(quarto_octeto > limite_numero_maximo):
          # NENHUM OCTETO NA FAIXA IDEAL
          quantidade_octetos_faixa_ideal -= 1
        else:
          # 1º, 2º E 3º OCTETOS NÃO ESTÃO NA FAIXA IDEAL
          quarto_octeto_na_faixa = True
      elif(quarto_octeto > limite_numero_maximo):
        # 1º, 2º E 4º OCTETOS NÃO ESTÃO NA FAIXA IDEAL
        quantidade_octetos_faixa_ideal -= 1
        terceiro_octeto_na_faixa = True
      else:
        # 1º E 2º OCTETOS NÃO ESTÃO NA FAIXA IDEAL
        terceiro_octeto_na_faixa = quarto_octeto_na_faixa = True
    elif(terceiro_octeto > limite_numero_maximo):
      quantidade_octetos_faixa_ideal -= 1
      if(quarto_octeto > limite_numero_maximo):
        # 1º, 3º E 4º OCTETOS NÃO ESTÃO NA FAIXA IDEAL
        quantidade_octetos_faixa_ideal -= 1
        segundo_octeto_na_faixa = True
      else:
        # 1º E 3º OCTETOS NÃO ESTÃO NA FAIXA IDEAL
        segundo_octeto_na_faixa = quarto_octeto_na_faixa = True
    elif(quarto_octeto > limite_numero_maximo):
      # 1º E 4º OCTETOS NÃO ESTÃO NA FAIXA IDEAL
      quantidade_octetos_faixa_ideal -= 1
      segundo_octeto_na_faixa = terceiro_octeto_na_faixa = True
    else:
      # 1º OCTETO NÃO ESTÁ NA FAIXA IDEAL
      segundo_octeto_na_faixa = terceiro_octeto_na_faixa = quarto_octeto_na_faixa = True
  elif(segundo_octeto > limite_numero_maximo):
    quantidade_octetos_faixa_ideal -= 1
    if(terceiro_octeto > limite_numero_maximo):
      quantidade_octetos_faixa_ideal -= 1
      if(quarto_octeto > limite_numero_maximo):
        # 2º, 3º E 4º OCTETOS NÃO ESTÃO NA FAIXA IDEAL
        quantidade_octetos_faixa_ideal -= 1
        primeiro_octeto_na_faixa = True
      else:
        # 2º E 3º OCTETOS NÃO ESTÃO NA FAIXA IDEAL
        primeiro_octeto_na_faixa = quarto_octeto_na_faixa = True
    elif(quarto_octeto > limite_numero_maximo):
      # 2º E 4º OCTETOS NÃO ESTÃO NA FAIXA IDEAL
      quantidade_octetos_faixa_ideal -= 1
      primeiro_octeto_na_faixa = terceiro_octeto_na_faixa = True
    else:
      # 2º OCTETO NÃO ESTÃO NA FAIXA IDEAL
      primeiro_octeto_na_faixa = terceiro_octeto_na_faixa = quarto_octeto_na_faixa = True
  elif(terceiro_octeto > limite_numero_maximo):
    quantidade_octetos_faixa_ideal -= 1
    if(quarto_octeto > limite_numero_maximo):
      # 3º E 4º OCTETOS NÃO ESTÃO NA FAIXA IDEAL
      quantidade_octetos_faixa_ideal -= 1
      primeiro_octeto_na_faixa = segundo_octeto_na_faixa = True
    else:
      # 3º OCTETO NÃO ESTÃO NA FAIXA IDEAL
      primeiro_octeto_na_faixa = segundo_octeto_na_faixa = quarto_octeto_na_faixa = True
  elif(quarto_octeto > limite_numero_maximo):
    # 4º OCTETO NÃO ESTÃO NA FAIXA IDEAL
    quantidade_octetos_faixa_ideal -= 1
    primeiro_octeto_na_faixa = segundo_octeto_na_faixa = terceiro_octeto_na_faixa = True
  else:
    primeiro_octeto_na_faixa = segundo_octeto_na_faixa = terceiro_octeto_na_faixa = quarto_octeto_na_faixa = True

  lista_octetos_faixa = [primeiro_octeto_na_faixa, segundo_octeto_na_faixa, terceiro_octeto_na_faixa, quarto_octeto_na_faixa]

  return lista_octetos_faixa, quantidade_octetos_faixa_ideal

# VERIFICA SE HÁ SÓ NÚMEROS INTEIROS NA REDE
def verificar_rede(rede_user):
  rede_so_numeros = True

  try:
    rede_user = int(rede_user)
  except ValueError:
    rede_so_numeros = False

  return rede_so_numeros, rede_user

# CALCULA A MÁSCARA DE REDE
def mascara_de_rede(rede_user):
  limite_bits = 8
  contador_bits_segundo_octeto = contador_bits_terceiro_octeto = contador_bits_quarto_octeto = 0
  soma_bits_segundo_octeto = soma_bits_terceiro_octeto = soma_bits_quarto_octeto = 0
  soma_bits_primeiro_octeto = 255
  base_bits_segundo_octeto = base_bits_terceiro_octeto = base_bits_quarto_octeto = 128

  for contar_bits in range(rede_user):
    if(contar_bits < limite_bits):
      continue
      # COMO A REDE OBRIGATÓRIAMENTE NÃO PODE SER MENOR QUE 8,
      # A SOMA DOS BITS DO PRIMEIRO OCTETO SEMPRE SERÁ 255
    elif(contar_bits < limite_bits * 2):
      # CADA NÚMERO ENTRE 8 E 16 CONTA COMO UM BIT
      contador_bits_segundo_octeto += 1
    elif(contar_bits < limite_bits * 3):
      # CADA NÚMERO ENTRE 16 E 24 CONTA COMO 1 BIT
      contador_bits_terceiro_octeto += 1
    else:
      # CADA NÚMERO ENTRE 24 E 32 CONTA COMO 1 BIT
      contador_bits_quarto_octeto += 1

  # O PRIMEIRO NÚMERO PARA SOMAR A CONTAGEM DO VALOR DE BITS SEMPRE SERÁ 
  # 128, E CONFORME AVANÇA DE UM BIT PARA OUTRO, FAZ A DIVISÃO DO NÚMERO
  # SOMADO ANTERIORMENTE POR 2, ATÉ CHEGAR NO PONTO EM QUE NÃO HÁ MAIS
  # BITS PARA SOMAR, OU A SOMA DÊ 255
  for bits_segundo_octeto in range(contador_bits_segundo_octeto):
    soma_bits_segundo_octeto += base_bits_segundo_octeto
    base_bits_segundo_octeto = base_bits_segundo_octeto//2

  for bits_terceiro_octeto in range(contador_bits_terceiro_octeto):
    soma_bits_terceiro_octeto += base_bits_terceiro_octeto
    base_bits_terceiro_octeto = base_bits_terceiro_octeto//2

  for bits_quarto_octeto in range(contador_bits_quarto_octeto):
    soma_bits_quarto_octeto += base_bits_quarto_octeto
    base_bits_quarto_octeto = base_bits_quarto_octeto//2

  return soma_bits_primeiro_octeto, soma_bits_segundo_octeto, soma_bits_terceiro_octeto, soma_bits_quarto_octeto

# CALCULA A REDE, BROADCAST, 1º E ÚLTIMO IP VÁLIDOS
def rede_broadcast_ip_valido(primeiro_octeto, segundo_octeto, terceiro_octeto, quarto_octeto, rede_user):
  maximo_numeros_ip = 256
  maximo_bits_total = 32
  quantidade_intervalos = broadcast_ip = rede_ip = 0
  lista_rede = []
  lista_broadcast = []
  lista_primeiro_ip_válido = []
  lista_ultimo_ip_valido = []

  if(rede_user < maximo_bits_total//2):
    # QUANTOS BITS ESTÃO LIGADOS NO SEGUNDO OCTETO (REDE ENTRE 8 16)
    bits_desligados = (maximo_bits_total//2) - rede_user
    quantidade_intervalos = maximo_numeros_ip//2**bits_desligados
    intervalo = maximo_numeros_ip//quantidade_intervalos

    for intervalos_segundo_octeto in range(0, maximo_numeros_ip + 1, intervalo):
      if(segundo_octeto < intervalos_segundo_octeto):
        broadcast_ip = intervalos_segundo_octeto - 1
        rede_ip = intervalos_segundo_octeto - intervalo
        break

    # COMO A REDE ESTÁ ENTRE 8 E 16, O PRIMEIRO OCTETO DO IP SEMPRE REPETIRÁ
    lista_rede.extend([primeiro_octeto, rede_ip, 0, 0])
    lista_primeiro_ip_válido.extend([primeiro_octeto, rede_ip, 0, 1])
    lista_ultimo_ip_valido.extend([primeiro_octeto, broadcast_ip, maximo_numeros_ip - 1, maximo_numeros_ip - 2])
    lista_broadcast.extend([primeiro_octeto, broadcast_ip, maximo_numeros_ip - 1, maximo_numeros_ip - 1])
  elif(rede_user < (maximo_bits_total//4)*3):
    # QUANTOS BITS ESTÃO LIGADOS NO TERCEIRO OCTETO (REDE ENTRE 16 E 24)
    bits_desligados = ((maximo_bits_total//4)*3) - rede_user
    quantidade_intervalos = maximo_numeros_ip//2**bits_desligados
    intervalo = maximo_numeros_ip//quantidade_intervalos

    for intervalos_terceiro_octeto in range(0, maximo_numeros_ip + 1, intervalo):
      if(terceiro_octeto < intervalos_terceiro_octeto):
        broadcast_ip = intervalos_terceiro_octeto - 1
        rede_ip = intervalos_terceiro_octeto - intervalo
        break

    # COMO A REDE ESTÁ ENTRE 16 E 24, O PRIMEIRO E SEGUNDO OCTETOS DO IP SEMPRE REPETIRÃO
    lista_rede.extend([primeiro_octeto, segundo_octeto, rede_ip, 0])
    lista_primeiro_ip_válido.extend([primeiro_octeto, segundo_octeto, rede_ip, 1])
    lista_ultimo_ip_valido.extend([primeiro_octeto, segundo_octeto, broadcast_ip, maximo_numeros_ip - 2])
    lista_broadcast.extend([primeiro_octeto, segundo_octeto, broadcast_ip, maximo_numeros_ip - 1])
  else:
    # QUANTOS BITS ESTÃO LIGADOS NO QUARTO OCTETO (REDE ENTRE 24 E 32)
    bits_desligados = maximo_bits_total - rede_user
    quantidade_intervalos = maximo_numeros_ip//2**bits_desligados
    intervalo = maximo_numeros_ip//quantidade_intervalos

    for intervalos_quarto_octeto in range(0, maximo_numeros_ip + 1, intervalo):
      if(quarto_octeto < intervalos_quarto_octeto):
        broadcast_ip = intervalos_quarto_octeto - 1
        rede_ip = intervalos_quarto_octeto - intervalo
        break

    # COMO A REDE ESTÁ ENTRE 24 E 32, O PRIMEIRO, SEGUNDO E TERCEIRO OCTETOS DO IP SEMPRE REPETIRÃO
    lista_rede.extend([primeiro_octeto, segundo_octeto, terceiro_octeto, rede_ip])
    lista_primeiro_ip_válido.extend([primeiro_octeto, segundo_octeto, terceiro_octeto, rede_ip + 1])
    lista_ultimo_ip_valido.extend([primeiro_octeto, segundo_octeto, terceiro_octeto, broadcast_ip - 1])
    lista_broadcast.extend([primeiro_octeto, segundo_octeto, terceiro_octeto, broadcast_ip])

  return lista_rede, lista_primeiro_ip_válido, lista_ultimo_ip_valido, lista_broadcast

# VERIFICA QUAL A CLASSE DO IP, BASEANDO-SE NO PRIMEIRO OCTETO
def classe_ip(primeiro_octeto):
  classe_a = 127
  classe_b = 191
  classe_c = 223
  classe_d = 239
  classe_e = 255
  classe = None

  if(primeiro_octeto <= classe_a):
    classe = 'A'
  elif(primeiro_octeto <= classe_b):
    classe = 'B'
  elif(primeiro_octeto <= classe_c):
    classe = 'C'
  elif(primeiro_octeto <= classe_d):
    classe = 'D'
  else:
    classe = 'E'

  return classe

# VERIFICA SE O IP É PRIVADO OU PÚBLICO
def ip_privado_publico(primeiro_octeto, segundo_octeto, terceiro_octeto, quarto_octeto, classe_ip):
  ip_classe_a = 'A'
  ip_classe_b = 'B'
  ip_classe_c = 'C'
  ip_classe_d = 'D'
  ip_classe_E = 'E'
  tipo_de_ip = None
  nao_disponivel = 'NÃO DISPONÍVEL'
  privado = 'PRIVADO'
  publico = 'PÚBLICO'

  if(classe_ip == ip_classe_a):
    if(primeiro_octeto == 10):
      tipo_de_ip = privado
    else:
      tipo_de_ip = publico
  elif(classe_ip == ip_classe_b):
    if(primeiro_octeto == 172):
      if((segundo_octeto >= 16) or (segundo_octeto <= 31)):
        tipo_de_ip = privado
      else:
        tipo_de_ip = publico
    else:
      tipo_de_ip = publico
  elif(classe_ip == ip_classe_c):
    if(primeiro_octeto == 192):
      if(segundo_octeto == 168):
        tipo_de_ip = privado
      else:
        tipo_de_ip = publico
    else:
      tipo_de_ip = publico
  else:
    tipo_de_ip = nao_disponivel

  return tipo_de_ip

if __name__ == '__main__':
  print('Bem vindo usuário!\nEste programa é uma calculadora de sub-redes IPv4!')
  print('Ao você digitar o IP e REDE, ela irá calcular:')
  print('Máscara de rede\nRede\n1º IP Válido\nÚltimo IP Válido\nBroadcast\nClasse de IP\nIP PRIVADO ou PÚBLICO')
  print('-' * 30)

  while(True):
    while(True):
      print(f'Para fazer o cálculo, por favor digite o IP desejado, no seguinte formato:')
      print(f'{exemplo_primeiro_octeto}.{exemplo_demais_octetos}.{exemplo_demais_octetos}.{exemplo_demais_octetos}:')
      ip_user = input()
      print('-' * 30)

      lista_status_octetos_final, primeiro_octeto, segundo_octeto, terceiro_octeto, quarto_octeto, quantidade_octetos_final = verificar_octetos(ip_user)
      if(quantidade_octetos_final < limite_octetos_final):
        lista_octetos_nao_validos = []
        for octetos_validos_nao_validos in range(len(lista_status_octetos_final)):
          if(lista_status_octetos_final[octetos_validos_nao_validos] == False):
            octeto_nao_valido = octetos_validos_nao_validos + 1
            lista_octetos_nao_validos.append(octeto_nao_valido)
        if(quantidade_octetos_final == limite_octetos_final - 1):
          print(f'Erro! Você não digitou o {lista_octetos_nao_validos[0]}º octeto!')
        elif(quantidade_octetos_final == limite_octetos_final - 2):
          print(f'Erro! Você não digitou o {lista_octetos_nao_validos[0]}º e {lista_octetos_nao_validos[1]}º octetos!')
        elif(quantidade_octetos_final == limite_octetos_final - 3):
          print(f'Erro! Você não digitou o {lista_octetos_nao_validos[0]}º, {lista_octetos_nao_validos[1]}º e {lista_octetos_nao_validos[2]}º octetos!')
        else:
          print('Erro! Você não digitou nenhum octeto!')
      elif(quantidade_octetos_final > limite_octetos_final):
        print(f'Erro! Você digitou {quantidade_octetos_final} octetos!')
        print(f'São somente aceitos {limite_octetos_final} octetos!')
      else:
        lista_octetos_validos_nao_validos, quantidade_octetos_so_numeros_final = converter_ip(primeiro_octeto, segundo_octeto, terceiro_octeto, quarto_octeto)
        if(quantidade_octetos_so_numeros_final < limite_octetos_final):
          lista_octetos_com_caracteres = []
          for octetos_com_sem_caracteres in range(len(lista_octetos_validos_nao_validos)):
            if(lista_octetos_validos_nao_validos[octetos_com_sem_caracteres] == False):
              octeto_com_caractere = octetos_com_sem_caracteres + 1
              lista_octetos_com_caracteres.append(octeto_com_caractere)
          if(quantidade_octetos_so_numeros_final == limite_octetos_final - 1):
            print(f'Erro! Você não digitou somente números no {lista_octetos_com_caracteres[0]}º octeto!')
          elif(quantidade_octetos_so_numeros_final == limite_octetos_final - 2):
            print(f'Erro! Você não digitou somente números no {lista_octetos_com_caracteres[0]}º e {lista_octetos_com_caracteres[1]}º octetos!')
          elif(quantidade_octetos_so_numeros_final == limite_octetos_final - 3):
            print(f'Erro! Você não digitou somente números no {lista_octetos_com_caracteres[0]}º, {lista_octetos_com_caracteres[1]}º e {lista_octetos_com_caracteres[2]}º octetos!')
          else:
            print('Erro! Você não digitou somente números em nenhum octeto!')
        else:
          primeiro_octeto = int(''.join(primeiro_octeto))
          segundo_octeto = int(''.join(segundo_octeto))
          terceiro_octeto = int(''.join(terceiro_octeto))
          quarto_octeto = int(''.join(quarto_octeto))
          lista_octetos_na_faixa_ou_nao, quantidade_octetos_na_faixa_final = verificar_faixa_ip(primeiro_octeto, segundo_octeto, terceiro_octeto, quarto_octeto)
          if(quantidade_octetos_na_faixa_final < limite_octetos_final):
            lista_octetos_nao_na_faixa = []
            for octetos_na_faixa_ou_nao in range(len(lista_octetos_na_faixa_ou_nao)):
              if(lista_octetos_na_faixa_ou_nao[octetos_na_faixa_ou_nao] == False):
                octeto_nao_na_faixa = octetos_na_faixa_ou_nao + 1
                lista_octetos_nao_na_faixa.append(octeto_nao_na_faixa)
            if(quantidade_octetos_na_faixa_final == limite_octetos_final - 1):
              print(f'Erro! Você não digitou o {lista_octetos_nao_na_faixa[0]}º octeto dentro da faixa de número ideal!')
            elif(quantidade_octetos_na_faixa_final == limite_octetos_final - 2):
              print(f'Erro! Você não digitou o {lista_octetos_nao_na_faixa[0]}º e o {lista_octetos_nao_na_faixa[1]}º octetos dentro da faixa de número ideal!')
            elif(quantidade_octetos_na_faixa_final == limite_octetos_final - 3):
              print(f'Erro! Você não digitou o {lista_octetos_nao_na_faixa[0]}º, {lista_octetos_nao_na_faixa[1]}º e {lista_octetos_nao_na_faixa[2]}º octetos dentro da faixa de número ideal!')
            else:
              print('Erro! Nenhum octeto que você digitou está dentro da faixa de número ideal!')
          else:
            break
      print('Por favor, tente novamente!')
      print('-' * 30)

    while(True):
      print(f'Agora, qual o CIDR desse IP?')
      print(f'Valores válidos: {exemplo_rede}:')
      rede_user = input()
      print('-' * 30)

      rede_so_numeros_final, rede = verificar_rede(rede_user)
      if(rede_so_numeros_final == False):
        print('Erro! Você não digitou somente números inteiros!')
      elif(rede < rede_tamanho_minimo):
        print('Erro! Você digitou a rede abaixo do valor mínimo!')
      elif(rede > rede_tamanho_maximo - 2):
        print('Erro! Você digitou a rede acima do valor máximo!')
      else:
        break
      print('Por favor, tente novamente!')
      print('-' * 30)

    mascara_primeiro_octeto, mascara_segundo_octeto, mascara_terceiro_octeto, mascara_quarto_octeto = mascara_de_rede(rede)
    rede_final, primeiro_ip_valido, ultimo_ip_valido, broadcast_final = rede_broadcast_ip_valido(primeiro_octeto, segundo_octeto, terceiro_octeto, quarto_octeto, rede)
    classe_final = classe_ip(primeiro_octeto)
    tipo_de_ip_final = ip_privado_publico(primeiro_octeto, segundo_octeto, terceiro_octeto, quarto_octeto, classe_final)

    print(f'IP e Rede: {primeiro_octeto}.{segundo_octeto}.{terceiro_octeto}.{quarto_octeto}/{rede}')
    print(f'Máscara de Rede: {mascara_primeiro_octeto}.{mascara_segundo_octeto}.{mascara_terceiro_octeto}.{mascara_quarto_octeto}')
    print(f'Rede: {rede_final[0]}.{rede_final[1]}.{rede_final[2]}.{rede_final[3]}')
    print(f'1º IP Válido: {primeiro_ip_valido[0]}.{primeiro_ip_valido[1]}.{primeiro_ip_valido[2]}.{primeiro_ip_valido[3]}')
    print(f'Último IP válido: {ultimo_ip_valido[0]}.{ultimo_ip_valido[1]}.{ultimo_ip_valido[2]}.{ultimo_ip_valido[3]}')
    print(f'Broadcast: {broadcast_final[0]}.{broadcast_final[1]}.{broadcast_final[2]}.{broadcast_final[3]}')
    print(f'IP de Classe: {classe_final}')
    print(f'Tipo de IP: {tipo_de_ip_final}')
    print('-' * 30)

    while(True):
      print(f'Para sair do programa, aperte a tecla "{sair}" e em seguida "{continuar}".' )
      print(f'Para fazer outro cálculo, apenas aperte "{continuar}".')
      
      decisao_user = input()
      print('-' * 30)

      if((decisao_user.upper() == sair) or (decisao_user.upper() == "")):
        break
      else:
        print('Erro! Você não digitou uma das opções disponíveis!')
        print('Por favor, tente novamente!')
        print('-' * 30)

    if(decisao_user.upper() == sair):
        print('Programa Finalizado!')
        print('-' * 30)
        break


"""https://www.bosontreinamentos.com.br/hardware/tabela-ascii/"""
