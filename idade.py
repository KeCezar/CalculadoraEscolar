from datetime import date, timedelta

def calcular_idade_exata(data_nasc):
    hoje = date.today()
    anos = hoje.year - data_nasc.year
    meses = hoje.month - data_nasc.month
    dias = hoje.day - data_nasc.day

    if dias < 0:
        meses -= 1
        ultimo_dia_mes_anterior = (hoje.replace(day=1) - timedelta(days=1)).day
        dias += ultimo_dia_mes_anterior

    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses, dias

# Loop principal
while True:
    print("_______________________________________\n_______________________________________\n--------- Calculadora de Idade --------")
    print("Digite 'sair' para encerrar.")

    # Verifica se o usuário quer sair
    entrada = input("Ano de nascimento (AAAA) ou 'sair': ").strip().lower()
    if entrada == 'sair':
        print("Programa encerrado.")
        break  # Sai do loop

    try:
        # Converte para inteiro e pede o resto dos dados
        dn_ano = int(entrada)
        dn_mes = int(input("Mês de nascimento (MM): "))
        dn_dia = int(input("Dia de nascimento (DD): "))

        # Cria a data de nascimento
        data_nascimento = date(dn_ano, dn_mes, dn_dia)
        print(f"\nData de nascimento: {data_nascimento}")

        # Calcula e exibe a idade
        anos, meses, dias = calcular_idade_exata(data_nascimento)
        print(f"Idade: {anos} anos, {meses} meses e {dias} dias")

    except ValueError:
        print("Erro: Digite uma data válida (ex: 2000 12 31). Tente novamente!")