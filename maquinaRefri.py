qntd_fiveCents, qntd_tenCents, qntd_vinteCentavos, qntd_fiftyCents, qntd_umReal, qntd_doisReais,  qntd_cincoReais, qntd_dezReais, qntd_vinteReais = 50, 50, 50, 20, 20, 20, 20, 20, 20
fiveCents, tenCents, twentyCents, fiftyCents, umReal, doisReais,  cincoReais, dezReais, vinteReais = 0.05, 0.10, 0.25, 0.50, 1, 2, 5, 10, 20

preco = 5.50

comando = ''

while comando != 'SAIR':
    comando = int(input(
        'Selecione o usuário:\n[1] Consumidor\n[2] Administrador, \n ou digite [SAIR] para cancelar sua escolha: '
    ))

    if comando == 1:
        produtoSelecionado = int(input('Selecione um produto: \n [1]. Coca-Cola '))
        if produtoSelecionado == 1:
            metodoPagamento = int(input('Qual o método de pagamento? \n [1].Dinheiro \n [2].Cartão de débito/crédito '))
            if metodoPagamento == 1:
                validacaoMoeda = False
                while validacaoMoeda == False:
                    pagamento = float(input('Por favor, insira suas moedas individualmete até pagar o preço requerido. \n'))

                    if pagamento == fiveCents or pagamento == tenCents or pagamento == twentyCents or pagamento == fiftyCents or pagamento == umReal or pagamento == doisReais or pagamento == cincoReais or pagamento == dezReais or pagamento == vinteReais:
                        while pagamento < preco:
                            moedaFaltante = pagamento
                            moedaFaltante = float(input(
                                'Moedas faltantes. Por favor insira mais moedas. \nPagamento total no momento: R$' + str(pagamento) + '\n'
                            ))
                            if moedaFaltante == fiveCents or moedaFaltante == tenCents or moedaFaltante == twentyCents or moedaFaltante == fiftyCents or moedaFaltante == umReal or moedaFaltante == doisReais or moedaFaltante == cincoReais or moedaFaltante == dezReais or moedaFaltante == vinteReais:
                                pagamento += moedaFaltante
                            else:
                                print('Pagamento invalido. Tente inserir moedas brasileiras válidas.')
                    else:
                        print('Pagamento invalido. Tente inserir moedas brasileiras válidas.')

                    if pagamento == preco:
                        print('Compra finalizada. Volte sempre!')
                        validacaoMoeda = True
                    elif pagamento > preco:
                        troco = pagamento - preco
                        troco20R = 0
                        troco10R = 0
                        troco5R = 0
                        troco2R = 0
                        troco1R = 0
                        troco50C = 0
                        troco25C = 0
                        troco10C = 0
                        troco5C = 0
                        
                        while troco >= vinteReais and qntd_vinteReais > 0:
                         troco20R += 1
                         troco -= vinteReais
                         qntd_vinteReais -= 1

                        while troco >= dezReais and qntd_dezReais > 0:
                         troco10C += 1
                         troco -= dezReais
                         qntd_dezReais -= 1

                        while troco >= cincoReais and qntd_cincoReais > 0:
                         troco5R += 1
                         troco -= cincoReais
                         qntd_cincoReais -= 1

                        while troco >= doisReais and qntd_doisReais > 0:
                         troco2R += 1
                         troco -= doisReais
                         qntd_doisReais -= 1
                       
                        while troco >= umReal and qntd_umReal > 0:
                         troco1R += 1
                         troco -= umReal
                         qntd_umReal -= 1
        
                        while troco >= fiftyCents and qntd_fiftyCents > 0:
                            troco50C += 1
                            troco -= fiftyCents
                            qntd_fiftyCents -= 1
                            
                        while troco >= twentyCents and qntd_vinteCentavos > 0:
                            troco25C += 1
                            troco -= twentyCents
                            qntd_vinteCentavos -= 1
                            
                        while troco >= tenCents and qntd_tenCents > 0:
                            troco10C += 1
                            troco -= tenCents
                            qntd_tenCents -= 1
                            
                        while troco >= fiveCents and qntd_fiveCents > 0:
                            troco5C += 1
                            troco -= fiveCents
                            qntd_fiveCents -= 1


                        print('Produto sendo entrege... \n Obrigado e volte sempre!')            
                                
