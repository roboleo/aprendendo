import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #sg.change_look_and_feel('Reddit')
        #Layout
        layout = [
            [sg.Text('Nome', size = (5,0)), sg.Input(size = (15,0), key ='nome')],
            [sg.Text('Idade', size = (5,0)), sg.Input(size = (15,0), key = 'idade')],
            [sg.Text('Quais provedores de e-mails são aceitos?')],
            [sg.Checkbox('Gmail', key ='gmail'), sg.Checkbox('Outlook', key ='outlook'), sg.Checkbox('Yahoo', key ='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes', key = 'aceitaCartao'), sg.Radio('Não', 'cartoes', key = 'nao')],
            [sg.Slider(range=(0,100),default_value=0,orientation='h', size=(15,20), key='sliderVelocidade')],
            [sg.Button('Enviar dados')],
            [sg.Output(size = (30,20))]
        ]
        #Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        #Extrair os dados da tela
        #self.buton, self.values = self.janela.Read()

    def Iniciar(self):
        while True:
            self.buton, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['nao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Outlook: {aceita_outlook}')
            print(f'Aceita Yahoo: {aceita_yahoo}')
            print(f'Aceita Cartão: {aceita_cartao}')
            print(f'Não aceita cartão: {nao_aceita_cartao}')
            print(f'Velocidade: {velocidade_script}')
            print(f'')
tela = TelaPython()
tela.Iniciar()
