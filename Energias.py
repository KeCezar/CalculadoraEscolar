# Programa completo para cálculos de energias com loop principal

def calcular_energia():
    print("\n======== CALCULADORA DE ENERGIA =======")
    print("Fórmulas disponíveis:")
    print("1. Ec - Energia Cinética (Ec = (m*v²)/2)")
    print("2. Epg - Energia Potencial Gravitacional (Epg = m*g*h)")
    print("3. Epe - Energia Potencial Elástica (Epe = (k*x²)/2)")
    print("4. Eel - Energia Elétrica (Eel = P*t ou Eel = U*i*t)")
    print("5. Epelet - Energia Potencial Elétrica (Epelet = k*|Q*q|/d)")
    print("6. Sair do programa")

    while True:
        # Usuário escolhe a fórmula
        formula = input("\nDigite a fórmula que deseja calcular (Ec/Epg/Epe/Eel/Epelet) ou 'sair': ").lower()
        
        if formula == 'sair' or formula == '6':
            print("\nObrigado por usar a Calculadora de Energia! Até mais!")
            break

        # --------------------------------------------------
        # Energia Cinética: Ec = (m * v²) / 2
        # --------------------------------------------------
        elif formula == "ec" or formula == "1":
            print("\n[Energia Cinética: Ec = (m*v²)/2]")
            print("Variáveis disponíveis:")
            print("Ec - Energia Cinética (Joules)")
            print("m - Massa (kg)")
            print("v - Velocidade (m/s)")
            
            variavel = input("Qual variável deseja calcular (Ec/m/v)? ").lower()
            
            if variavel == "ec":
                try:
                    m = float(input("Massa (m) em kg: "))
                    v = float(input("Velocidade (v) em m/s: "))
                    Ec = (m * (v ** 2)) / 2
                    print(f"\nEnergia Cinética (Ec) = {Ec:.4f} J")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            elif variavel == "m":
                try:
                    Ec = float(input("Energia Cinética (Ec) em J: "))
                    v = float(input("Velocidade (v) em m/s: "))
                    m = (2 * Ec) / (v ** 2)
                    print(f"\nMassa (m) = {m:.4f} kg")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            elif variavel == "v":
                try:
                    Ec = float(input("Energia Cinética (Ec) em J: "))
                    m = float(input("Massa (m) em kg: "))
                    v = ((2 * Ec) / m) ** 0.5
                    print(f"\nVelocidade (v) = {v:.4f} m/s")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            else:
                print("Variável inválida!")

        # --------------------------------------------------
        # Energia Potencial Gravitacional: Epg = m * g * h
        # --------------------------------------------------
        elif formula == "epg" or formula == "2":
            print("\n[Energia Potencial Gravitacional: Epg = m*g*h]")
            print("Variáveis disponíveis:")
            print("Epg - Energia Potencial Gravitacional (Joules)")
            print("m - Massa (kg)")
            print("g - Aceleração gravitacional (m/s²)")
            print("h - Altura (m)")
            
            variavel = input("Qual variável deseja calcular (Epg/m/g/h)? ").lower()
            
            if variavel == "epg":
                try:
                    m = float(input("Massa (m) em kg: "))
                    g = float(input("Aceleração gravitacional (g) em m/s²: "))
                    h = float(input("Altura (h) em metros: "))
                    Epg = m * g * h
                    print(f"\nEnergia Potencial Gravitacional (Epg) = {Epg:.4f} J")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            elif variavel == "m":
                try:
                    Epg = float(input("Energia Potencial (Epg) em J: "))
                    g = float(input("Aceleração gravitacional (g) em m/s²: "))
                    h = float(input("Altura (h) em metros: "))
                    m = Epg / (g * h)
                    print(f"\nMassa (m) = {m:.4f} kg")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            elif variavel == "g":
                try:
                    Epg = float(input("Energia Potencial (Epg) em J: "))
                    m = float(input("Massa (m) em kg: "))
                    h = float(input("Altura (h) em metros: "))
                    g = Epg / (m * h)
                    print(f"\nAceleração gravitacional (g) = {g:.4f} m/s²")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            elif variavel == "h":
                try:
                    Epg = float(input("Energia Potencial (Epg) em J: "))
                    m = float(input("Massa (m) em kg: "))
                    g = float(input("Aceleração gravitacional (g) em m/s²: "))
                    h = Epg / (m * g)
                    print(f"\nAltura (h) = {h:.4f} m")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            else:
                print("Variável inválida!")

        # --------------------------------------------------
        # Energia Potencial Elástica: Epe = (k * x²) / 2
        # --------------------------------------------------
        elif formula == "epe" or formula == "3":
            print("\n[Energia Potencial Elástica: Epe = (k*x²)/2]")
            print("Variáveis disponíveis:")
            print("Epe - Energia Potencial Elástica (Joules)")
            print("k - Constante elástica (N/m)")
            print("x - Deformação (m)")
            
            variavel = input("Qual variável deseja calcular (Epe/k/x)? ").lower()
            
            if variavel == "epe":
                try:
                    k = float(input("Constante elástica (k) em N/m: "))
                    x = float(input("Deformação (x) em metros: "))
                    Epe = (k * (x ** 2)) / 2
                    print(f"\nEnergia Potencial Elástica (Epe) = {Epe:.4f} J")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            elif variavel == "k":
                try:
                    Epe = float(input("Energia Potencial Elástica (Epe) em J: "))
                    x = float(input("Deformação (x) em metros: "))
                    k = (2 * Epe) / (x ** 2)
                    print(f"\nConstante elástica (k) = {k:.4f} N/m")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            elif variavel == "x":
                try:
                    Epe = float(input("Energia Potencial Elástica (Epe) em J: "))
                    k = float(input("Constante elástica (k) em N/m: "))
                    x = ((2 * Epe) / k) ** 0.5
                    print(f"\nDeformação (x) = {x:.4f} m")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            else:
                print("Variável inválida!")

        # --------------------------------------------------
        # Energia Elétrica: Eel = P * t OU Eel = U * i * t
        # --------------------------------------------------
        elif formula == "eel" or formula == "4":
            print("\n[Energia Elétrica]")
            print("1. Eel = P * t [Potência × tempo]")
            print("2. Eel = U * i * t [Tensão × corrente × tempo]")
            try:
                modo = input("Escolha a fórmula (1/2): ")
                
                if modo == "1":
                    print("\n[Eel = P * t]")
                    print("Variáveis disponíveis:")
                    print("Eel - Energia Elétrica (Joules)")
                    print("P - Potência (Watts)")
                    print("t - Tempo (segundos)")
                    
                    variavel = input("Qual variável deseja calcular (Eel/P/t)? ").lower()
                    
                    if variavel == "eel":
                        try:
                            P = float(input("Potência (P) em Watts: "))
                            t = float(input("Tempo (t) em segundos: "))
                            Eel = P * t
                            print(f"\nEnergia Elétrica (Eel) = {Eel:.4f} J")
                        except ValueError:
                            print("Erro: Insira valores numéricos válidos!")
                        
                    elif variavel == "p":
                        try:
                            Eel = float(input("Energia Elétrica (Eel) em J: "))
                            t = float(input("Tempo (t) em segundos: "))
                            P = Eel / t
                            print(f"\nPotência (P) = {P:.4f} W")
                        except ValueError:
                            print("Erro: Insira valores numéricos válidos!")
                        
                    elif variavel == "t":
                        try:
                            Eel = float(input("Energia Elétrica (Eel) em J: "))
                            P = float(input("Potência (P) em Watts: "))
                            t = Eel / P
                            print(f"\nTempo (t) = {t:.4f} s")
                        except ValueError:
                            print("Erro: Insira valores numéricos válidos!")
                        
                    else:
                        print("Variável inválida!")
                
                elif modo == "2":
                    print("\n[Eel = U * i * t]")
                    print("Variáveis disponíveis:")
                    print("Eel - Energia Elétrica (Joules)")
                    print("U - Tensão (Volts)")
                    print("i - Corrente (Ampères)")
                    print("t - Tempo (segundos)")
                    
                    variavel = input("Qual variável deseja calcular (Eel/U/i/t)? ").lower()
                    
                    if variavel == "eel":
                        try:
                            U = float(input("Tensão (U) em Volts: "))
                            i = float(input("Corrente (i) em Ampères: "))
                            t = float(input("Tempo (t) em segundos: "))
                            Eel = U * i * t
                            print(f"\nEnergia Elétrica (Eel) = {Eel:.4f} J")
                        except ValueError:
                            print("Erro: Insira valores numéricos válidos!")
                        
                    elif variavel == "u":
                        try:
                            Eel = float(input("Energia Elétrica (Eel) em J: "))
                            i = float(input("Corrente (i) em Ampères: "))
                            t = float(input("Tempo (t) em segundos: "))
                            U = Eel / (i * t)
                            print(f"\nTensão (U) = {U:.4f} V")
                        except ValueError:
                            print("Erro: Insira valores numéricos válidos!")
                        
                    elif variavel == "i":
                        try:
                            Eel = float(input("Energia Elétrica (Eel) em J: "))
                            U = float(input("Tensão (U) em Volts: "))
                            t = float(input("Tempo (t) em segundos: "))
                            i = Eel / (U * t)
                            print(f"\nCorrente (i) = {i:.4f} A")
                        except ValueError:
                            print("Erro: Insira valores numéricos válidos!")
                        
                    elif variavel == "t":
                        try:
                            Eel = float(input("Energia Elétrica (Eel) em J: "))
                            U = float(input("Tensão (U) em Volts: "))
                            i = float(input("Corrente (i) em Ampères: "))
                            t = Eel / (U * i)
                            print(f"\nTempo (t) = {t:.4f} s")
                        except ValueError:
                            print("Erro: Insira valores numéricos válidos!")
                        
                    else:
                        print("Variável inválida!")
                
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Erro: Insira uma opção válida!")

        # --------------------------------------------------
        # Energia Potencial Elétrica: Epelet = k * |Q*q| / d
        # --------------------------------------------------
        elif formula == "epelet" or formula == "5":
            print("\n[Energia Potencial Elétrica: Epelet = k*|Q*q|/d]")
            print("Onde:")
            print("k = 9×10⁹ N·m²/C² (constante eletrostática)")
            print("Q e q - Cargas elétricas (Coulombs)")
            print("d - Distância entre as cargas (metros)")
            
            print("\nVariáveis disponíveis:")
            print("Epelet - Energia Potencial Elétrica (Joules)")
            print("Q - Carga 1 (Coulombs)")
            print("q - Carga 2 (Coulombs)")
            print("d - Distância (metros)")
            
            variavel = input("Qual variável deseja calcular (Epelet/Q/q/d)? ").lower()
            k = 9e9  # Constante eletrostática
            
            if variavel == "epelet":
                try:
                    Q = float(input("Carga Q em Coulombs: "))
                    q = float(input("Carga q em Coulombs: "))
                    d = float(input("Distância d em metros: "))
                    Epelet = (k * abs(Q * q)) / d
                    print(f"\nEnergia Potencial Elétrica (Epelet) = {Epelet:.4e} J")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            elif variavel == "q":
                try:
                    Epelet = float(input("Energia Potencial Elétrica (Epelet) em J: "))
                    q = float(input("Carga q em Coulombs: "))
                    d = float(input("Distância d em metros: "))
                    Q = (Epelet * d) / (k * abs(q))
                    print(f"\nCarga Q = {Q:.4e} C")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            elif variavel == "q":
                try:
                    Epelet = float(input("Energia Potencial Elétrica (Epelet) em J: "))
                    Q = float(input("Carga Q em Coulombs: "))
                    d = float(input("Distância d em metros: "))
                    q = (Epelet * d) / (k * abs(Q))
                    print(f"\nCarga q = {q:.4e} C")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            elif variavel == "d":
                try:
                    Epelet = float(input("Energia Potencial Elétrica (Epelet) em J: "))
                    Q = float(input("Carga Q em Coulombs: "))
                    q = float(input("Carga q em Coulombs: "))
                    d = (k * abs(Q * q)) / Epelet
                    print(f"\nDistância d = {d:.4e} m")
                except ValueError:
                    print("Erro: Insira valores numéricos válidos!")
                
            else:
                print("Variável inválida!")

        # --------------------------------------------------
        # Caso o usuário digite uma fórmula inválida
        # --------------------------------------------------
        else:
            print("Fórmula inválida! Por favor, digite uma das opções válidas.")

# Inicia o programa
if __name__ == "__main__":
    calcular_energia()