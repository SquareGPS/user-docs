# Integração Streamax para telemetria de vídeo

A Streamax é um fabricante líder de MDVR, bem estabelecido no mercado global. Com seus dispositivos, você pode habilitar gravação de vídeo 24/7 de seus veículos, coletar dados de telemetria, acessar remotamente filmagens de vídeo e monitorar a segurança na condução usando tecnologias ADAS (Sistemas Avançados de Assistência ao Motorista) e DSM (Monitoramento do Status do Motorista).

Ao integrar a Streamax com a Navixy, você obtém monitoramento abrangente de vídeo combinado com gerenciamento avançado de frota em uma única interface. Vamos examinar mais de perto como implementar essa combinação poderosa e incorporar o painel da Streamax na interface da Navixy.

## 1\. Estabelecendo a integração

Para estabelecer a integração, você precisará obter credenciais de API de sua conta Streamax e solicitar a configuração da integração de nossa equipe de suporte.

### Obter credenciais de API da Streamax

1. **Obter Chave de API e Segredo**: Siga o processo de autenticação conforme descrito na [documentação de Autenticação de Assinatura da Streamax](https://ftcloud.streamax.com:20002/DOC/Sign%20Authentication) para obter sua chave de API e segredo.
2. **Entre em contato com a Navixy**: Assim que tiver suas credenciais de API, entre em contato com seu Gerente de Sucesso do Cliente ou use [este formulário](https://www.navixy.com/contact/). Envie uma solicitação para integrar a Streamax com sua conta Navixy, contendo as seguintes informações:
  - Sua chave de API
  - Seu segredo de API
  - Detalhes de sua conta Navixy
  - Solicitação para ativação da integração Streamax
3. **Aguarde a confirmação**: Nossos especialistas configurarão a integração em 1-3 dias do nosso lado e confirmarão quando estiver pronta para uso.

> [!TIP]
> Após receber a confirmação de nosso suporte, sua conta Streamax está pronta para a integração!

## 2\. Adicionando um dispositivo Streamax à Navixy

Após receber a confirmação de nossa equipe de suporte de que a integração está pronta, você pode adicionar seu dispositivo Streamax à plataforma. Para fazer isso, siga o procedimento usual de ativação de dispositivo:

1. Vá para **Ativação de dispositivo**.
2. Selecione seu dispositivo Streamax da lista.
3. Selecione a opção **Cartão SIM comprado separadamente** e vá para o próximo passo.
4. Digite um **ID do Dispositivo** correto (IMEI do dispositivo)
5. Complete a configuração do dispositivo

Para instruções detalhadas sobre como ativar um dispositivo na Navixy, consulte [Ativar dispositivo GPS](https://squaregps.atlassian.net/wiki/spaces/UDOCPT/pages/3025240148/Ativar+o+dispositivo+GPS?atlOrigin=eyJpIjoiMTkxMjVjOWI0MzgxNGUzMGI3YzQxMjUzMzg4YWQ3N2MiLCJwIjoiYyJ9).

> [!TIP]
> Seu dispositivo e conta Navixy estão prontos para a integração!

## 3\. Incorporando a Streamax na interface da Navixy

Nesta etapa, realizamos a integração real incorporando o painel da Streamax em sua interface Navixy.  
A Navixy oferece funcionalidade de [Aplicações do usuário](https://squaregps.atlassian.net/wiki/spaces/UDOCPT/pages/3025240815/Aplicativos+de+usu+rio?atlOrigin=eyJpIjoiOGNkNzc4YWMxMzM2NDEyYmFmZDkwMDUwNjQ1OTk2MTciLCJwIjoiYyJ9) que permite incorporar aplicativos de terceiros diretamente na interface da plataforma. Usaremos isso para incorporar a Mettax.

> [!NOTE]
> **Navegação**
> A seção **Aplicações do usuário** é acessível aos **Proprietários** da conta na seção **Configurações da Conta**. Para encontrá-la:
> 1. Clique no ícone do perfil no canto superior esquerdo da tela para abrir as configurações de sua conta
> 2. Na barra lateral de configurações, selecione **Aplicações do usuário**

1. Criar nova aplicação  
Comece clicando no botão ![image-20250725-120122.png](attachments/image-20250725-120122.png)
 na lista de **Aplicações do usuário**.
2. Configurar a nova aplicação
  1. Coloque o link para sua conta Streamax no campo **URL do App**, por exemplo: `https://{sua_instância}.ifleetvision.com/ftv/ft/dashboard#`.
  2. Digite um **Rótulo** para a aplicação (por exemplo, Painel Streamax).
  3. Selecione **Incorporado** no campo **Mostrar como** para exibir a funcionalidade da Streamax dentro da Navixy.
3. Clique em **Salvar** para completar a configuração.

> [!TIP]
> Sua nova aplicação aparece automaticamente na barra lateral esquerda da Navixy. Abra-a e faça login com suas credenciais Streamax para acessar seu painel abrangente de telemetria de vídeo com monitoramento 360°, detecção de eventos alimentada por IA e feeds de vídeo multicanal - tudo integrado com suas ferramentas existentes de gerenciamento de frota da Navixy.
> ![7bf15f575f8b4a44b772b7930da817a8.png](attachments/7bf15f575f8b4a44b772b7930da817a8.png)