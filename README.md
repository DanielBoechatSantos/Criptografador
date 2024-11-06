# Criptografador

Motivação:

Frequentemente, desenvolvo códigos em Python que utilizam senhas para testes, com o intuito de agilizar a execução. No entanto, ao compartilhar esses códigos em plataformas como o Visual Studio Code ou em outras workspaces de desenvolvimento, eles poderiam ser acessados em qualquer computador. Para assegurar a segurança, desenvolvi o código acima, que criptografa o arquivo, de forma que, mesmo que o código seja copiado, outros usuários só poderão acessá-lo ao realizar a decriptação.

Para descriptografar o arquivo, é necessário inserir a senha de criptografia, que é solicitada no momento da decriptação. Além disso, ampliei a funcionalidade do código para permitir a criptografia de qualquer tipo de arquivo, não apenas arquivos .py, abrangendo também outras extensões. Como o Windows não oferece a possibilidade de proteger pastas com senha, essa aplicação contribui para garantir a segurança dos arquivos de maneira prática e eficiente.
