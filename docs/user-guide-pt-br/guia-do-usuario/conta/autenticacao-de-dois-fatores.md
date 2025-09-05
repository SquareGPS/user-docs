# Autenticação de dois fatores

A Navixy oferece autenticação de dois fatores (2FA) para reforçar a segurança em aplicativos da Web e móveis. Com o aumento da quantidade de dados telemáticos confidenciais sendo gerenciados, a 2FA fornece uma camada adicional vital de segurança, exigindo uma senha e uma senha de uso único (OTP) enviada por e-mail. Seu provedor de serviços de GPS/Telemática determina se a 2FA está ativada e define as respectivas configurações.

**Como isso funciona?**

A OTP será enviada para seu e-mail e deverá ser inserida para concluir o processo de login. A etapa adicional garante que, mesmo que sua senha seja comprometida, usuários não autorizados não poderão acessar sua conta sem acesso ao seu e-mail.

1. **Faça login com sua senha**Digite seu nome de usuário e senha para iniciar o processo de login.
2. **Receba um código único**Se você tiver uma senha de uso único, ela será enviada para o e-mail que você registrou na sua conta Navixy.
3. **Digite o código**Você digitará essa OTP para concluir seu login.
4. **Acesse sua conta**Se a OTP estiver correta, o acesso será concedido; caso contrário, o login será negado.

Abre a imagem em tela cheiaAbrir

![Two-factor authentication at Navixy](https://docs.navixy.com/__attachments/2868412417/2fa-20240930-131646.png?inst-v=e181aefb-b1e7-494a-b929-55c13c4569a3)

Cada código de acesso é válido por 5 minutos, limitando a oportunidade de uso indevido. Além disso, você pode solicitar um novo código, se necessário, mas apenas uma vez por minuto para evitar abusos.