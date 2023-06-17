'''O sistem de login deve permitir que novoc usuários sejam cadastrados, e que usuários existentes possam fazer o login. O sistema deve alertar caso a senha elogin não estejam corretos'''
# O sistema não deve permitir que usuários duplicados sejam cadastrados
# O sistema deve alertar caso a senha e login não estejam corretos.


# Permitir que usuários existentes possam fazer o login
resposta = input('[1] - Cadastrar novo usuário [2] - Fazer login ')
# armazenando os usuários existentes
usuarios = ['Amanda', 'Jhon', 'Fernando']
senhas = ['123456', '789def', '12131415']

if resposta == '1':
    # recebendo um usuário
    usuario_digitado = input('Digite seu usuário: ')
    # recebendo uma senha
    senha_digitada = input('Digite sua senha: ')
    # caso não exista, cadastrar aquele usuário e senha
    usuarios.append(usuario_digitado)
    senhas.append(senha_digitada)
    # Permitir que usuários existentes possam fazer o login
elif resposta == '2':
    # Permitir que usuários existentes possam fazer o login
    # Pedir usuário
    usuario_digitado = input('Digite seu usuário: ')
    # Pedir senha
    senha_digitada = input('Digite sua senha: ')
    # Verificar se usuário existe na lista.
    
    # Verificar se a senha providenciada para o usuário é a mesma senha que está na nossa lista de senhas.
    