# Autenticación de dos factores

Navixy ofrece autenticación de dos factores (2FA) para reforzar la seguridad en las aplicaciones web y móviles. Con la creciente cantidad de datos telemáticos sensibles que se gestionan, 2FA proporciona una capa adicional vital de seguridad al requerir tanto una contraseña como un código de acceso de un solo uso (OTP) enviado por correo electrónico. Su proveedor de servicios GPS/Telemática determina si 2FA está activado y configura los ajustes correspondientes.

**¿Cómo funciona?**

La contraseña OTP se enviará a tu correo electrónico y deberás introducirla para completar el proceso de inicio de sesión. Este paso adicional garantiza que, aunque tu contraseña se vea comprometida, los usuarios no autorizados no puedan acceder a tu cuenta sin tener acceso a tu correo electrónico.

1. **Inicie sesión con su contraseña**: introduzca su nombre de usuario y contraseña para iniciar el proceso de acceso.
2. **Recibir un código único**Después de verificar su contraseña, se le enviará una contraseña de un solo uso a la dirección de correo electrónico que haya registrado en su cuenta Navixy.
3. **Introduzca el código**A continuación, introduzca la OTP para completar el inicio de sesión.
4. **Acceder a su cuenta**: si la OTP es correcta, se concede el acceso; en caso contrario, se deniega el inicio de sesión.

Abre la imagen a pantalla completaAbrir

![Two-factor authentication at Navixy](https://docs.navixy.com/__attachments/2868412417/2fa-20240930-131646.png?inst-v=e181aefb-b1e7-494a-b929-55c13c4569a3)

Cada código de acceso es válido durante 5 minutos, lo que limita las posibilidades de uso indebido. Además, puedes solicitar un nuevo código si es necesario, pero solo una vez por minuto para evitar abusos.