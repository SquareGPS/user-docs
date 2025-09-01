# Recurso confiável

# Recurso Confiable-GPS tracking/data forwarding para empresas

Recurso Confiable é um software de segurança e logística que monitora, dá visibilidade e gera previsibilidade nas operações de transporte. A Navixy criou o protocolo de encaminhamento de dados do Recurso Confiable para ser usado por outras empresas que também trabalham com o Recurso Confiable em vários setores no México, na Colômbia, nos Estados Unidos e na América Central.

*Categoria de protocolo: Protocolo empresarial*

### Tabela de conteúdo

1. [O que é Recurso Confiável?](#what-is-rc)
2. [Informações técnicas sobre o Recurso Confiable](#tech-info-rc)
3. [Configuração do Recurso Confiável](#rc-config)
  1. [Configuração](#setting-up)
  2. [Gerenciamento](#managing)
  3. [Solução de problemas](#troubleshooting)

## O que é Recurso Confiável?

Com o protocolo Recurso Confiable, os parceiros corporativos podem transferir dados de rastreamento por GPS de forma segura e confiável para um único local, a fim de otimizar os processos de gerenciamento de frotas. Isso permite ao cliente uma maneira de trabalhar e se comunicar com outros parceiros do Recurso Confiable.

Ao desenvolver esse protocolo, a Navixy levou em conta as necessidades de grandes empresas de logística e varejo. As empresas podem otimizar dados e recursos importantes da plataforma de gerenciamento de frotas e rastreamento GPS, como sistemas de controle, planejamento de viagens, rastreamento em tempo real, relatórios de modelagem preditiva, implementação e edição de geofences, otimização de rotas e muito mais. As empresas que antes estavam desconectadas umas das outras na rede do Recurso Confiable agora podem se comunicar com eficiência e rapidez.

## Informações técnicas gerais do Recurso Confiable

O protocolo do Recurso Confiable utiliza SOAP para enviar dados XML a cada 5 minutos por HTTP para o Recurso Confiable.

Dados enviados ao Recurso Confiável:

- Código do evento AVL
- Placa de identificação
- ID da remessa
- Data
- Direção
- Latitude
- Longitude
- Altitude
- Velocidade
- Curso
- Ignição
- Odômetro
- ID do cliente
- Nome do cliente
- ID do dispositivo

## Configuração do Recurso Confiável

### Configuração

Parâmetros necessários

- Login e senha do Recurso Confiável
- ID externa
- Endereço do servidor de destino
  - [http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc](http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc)
- Porta do servidor de destino
  - 80

Para configurar o encaminhamento de dados no protocolo Recurso Confiável, abra as configurações do dispositivo no menu principal pressionando o ícone "Gear" (Engrenagem) na parte inferior esquerda da tela

Em seguida, clique no widget "Data forwarding" (Encaminhamento de dados).

Clique em "Protocols" (Protocolos).

Isso abrirá uma janela pop-up na qual você inserirá os parâmetros necessários pressionando o botão +.

Para o protocolo Recurso Confiável, insira as seguintes informações:

| Parâmetro | Explicação | | | --- | --- | Nome | Digite um nome para tornar esse retradutor facilmente identificável | | Protocolo e login | Selecione o protocolo do Recurso Confiável na lista suspensa;<br><br>Use o login e a senha do Recurso Confiável | | Endereço e porta do servidor de destino | Endereço: [http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc](http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc) | Porta: 80

A tela de gerenciamento da Retradução deve ser semelhante à seguinte, com o login e a senha do Recurso Confiable. Certifique-se de que o botão "Enabled" (Ativado) esteja marcado e clique no botão "Save" (Salvar) para concluir o processo.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-1-1-600x120.png)

Em seguida, o retradutor precisará ser vinculado ao dispositivo no lado do Recurso Confiável. Para isso, selecione a opção "Link" ![link image](https://www.navixy.com/wp-content/uploads/2022/08/image-3.png)

no widget de encaminhamento de dados. Selecione o retranslator a ser conectado e clique em "Link" abaixo.

Em seguida, adicione as informações necessárias para identificar o dispositivo no Recurso Confiable no campo External ID (ID externo), clicando no ícone de lápis ou no próprio campo de ID externo. Esse valor deve incluir o seguinte no lado do Recurso Confiável, onde apenas a placa de identificação é obrigatória:

Placa de identificação

ID da rota

ID da empresa

Nome da empresa

O formato do campo External ID será separado por um pipe. Por exemplo:

ABC123|1|123|John

Se apenas a placa de identificação estiver disponível, a ID externa poderá ser inserida sozinha:

ABC123

Ou, se alguma outra informação estiver faltando, não se esqueça de incluir os tubos, por exemplo:

ABC123||123|

Selecione "Save" (Salvar) depois de concluído.

### Gerenciamento

Para editar ou interromper o encaminhamento de dados, consulte as etapas a seguir:

Selecione o ícone "Pencil" (Lápis) ou clique na caixa associada para editar a ID externa usada para apontar para o dispositivo no sistema de terceiros.

Para interromper o encaminhamento de dados, clique no botão "Lixeira".

Em seguida, confirme a alteração na janela pop-up.

Para alterar as configurações do retradutor, como nome, informações de login ou ativação, clique em "Retranslators management" (Gerenciamento de retradutores).

Isso abrirá a janela de gerenciamento do retranslator. Selecione a linha a ser editada e clique no lápis no canto superior esquerdo ou clique duas vezes na linha em questão para permitir a edição. Salve as alterações.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-3-600x107.png)

### Solução de problemas

Se os dados não forem exibidos no sistema do Recurso Confiável de terceiros, verifique:

- O nome de usuário e a senha do Recurso Confiável foram inseridos corretamente
- O URL foi inserido corretamente
- O Retranslator está ativado
- O ID externo corresponde às informações relacionadas ao Recurso Confiável