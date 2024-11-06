# Criptografador

Motivação:

Frequentemente, desenvolvo códigos em Python que utilizam senhas para testes, com o intuito de agilizar a execução. No entanto, ao compartilhar esses códigos em plataformas como o Visual Studio Code ou em outras workspaces de desenvolvimento, eles poderiam ser acessados em qualquer computador. Para assegurar a segurança, desenvolvi o código acima, que criptografa o arquivo, de forma que, mesmo que o código seja copiado, outros usuários só poderão acessá-lo ao realizar a decriptação.

Para descriptografar o arquivo, é necessário inserir a senha de criptografia, que é solicitada no momento da decriptação. Além disso, ampliei a funcionalidade do código para permitir a criptografia de qualquer tipo de arquivo, não apenas arquivos .py, abrangendo também outras extensões. Como o Windows não oferece a possibilidade de proteger pastas com senha, essa aplicação contribui para garantir a segurança dos arquivos de maneira prática e eficiente.

Funcionamento da aplicação:

![image](https://github.com/user-attachments/assets/bbefbe0e-db9f-4db4-b8a1-e9f9200867bd)


Ao clicar em Criptografar, aparecerá uma caixa de texto pedindo para que seja digitada a senha de criptografia. O campo senha está configurado como password, portanto, não serão exibidos os caracteres.

![image](https://github.com/user-attachments/assets/e535f43c-934f-4695-a487-6de24c15d877)


Ao clicar no Ok, o usuário precisa selecionar o arquivo que será criptografado. Na imagem abaixo, mostro o arquivo de teste com o texto legível, mostrando que o arquivo está normal, sem criptografia

![image](https://github.com/user-attachments/assets/a098f020-3fce-460f-ae8e-a045c451994f)


Abaixo, veja a confirmação de criptografia do arquivo, e como o arquivo fica ao ser aberto

![image](https://github.com/user-attachments/assets/88d54ad1-6ade-4c7d-97b1-5da3ec4cd7a7)


Para descriptar é o mesmo procedimento, clicando em descriptografar, digitando a senha (que precisa ser a mesma digitada anteriormente) e selecionando o arquivo a ser descriptado.

![image](https://github.com/user-attachments/assets/8aba8e78-1c61-4217-af7f-b6a762f64ea6)
![image](https://github.com/user-attachments/assets/193797e6-2750-41e2-96f9-d635b9d68c99)







