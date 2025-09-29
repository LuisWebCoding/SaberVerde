while True:
    funcao = input("Bem vindo á SaberVerde. Você deseja saber sobre Cultivo ou Plantio? ").lower()


    if funcao == "cultivo":
        while True:
            print("Listas de plantas e flores disponíveis: Orquídea e Cacto")
            cultivo = input("Qual planta/flor você deseja cultivar? ").lower()
            if cultivo == "orquídea":
                print("De forma geral reunimos algumas informações sobre seu cuidado, mas existem varias especies de orquídeas. \nOrquídeas precisam de luz, mas não de sol direto, que pode queimar suas folhas. A frequência de rega varia conforme a espécie, o tipo de vaso e o clima, mas a regra geral é regar quando o substrato estiver seco ao toque, evite encharcar o substrato. \nAs orquideas em sua maioria vivem com altas umidades. ")
                break
            elif cultivo == "cacto":
                print("Os cactos como grande acumuladoras de água, sua rega não pode ser constante e quantidade sempre proporcional ao tamanho do vaso. \ncaEm periodos de calor regar 1 vez por semana é suficiente, em dia de frios 1 ou 2 vezes ao mês. \nEla precisa receber luz solar diariamente, normalmente em horarios das 10hrs até as 15hrs, de preferência não em locais abafados.")
                break
            else:
                print("Opção de planta inválida.")


    elif funcao == "plantio":
        while True:
            print("Listas de plantas e flores disponíveis: Orquídea e Cacto")
            plantio = input("Qual planta/flor você deseja plantar? ").lower()
            if plantio == "orquídea":
                print("Escolha um vaso fundo e não muito largo, de preferência que o material seja de ceramica ou barro, você precisá de um material que a deixe reta quando ela estiver crescendo, como bambús com arames. \nOpte por um substrato com bon nutrientes e com uma boa variação de material como carvão, musgo seco, fibra de coco, e até mesmo isopor. E adubo com potássio, fósforo e cálcio.")
                break
            elif plantio == "cacto":
                print("Para o plantio do cacto é necessário a um vaso de cerâmica ou barro, é interessante que tenha furos no fundo ou seja um vaso mais raso. \cnO seu substrato deve ser feito de areia e pedriscos. E o seu adubo deve conter fósforo e nitrogênio. Em prática, coloque a barreira de drenagem, o substrato vai junto do adubo, um pouco mais poroso para ajudar na drenagem, centralize o cacto no meio e finalie com areia e pedriscos. \nPronto!")
                break
            else:
                print("Opção de planta inválida.")
