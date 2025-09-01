# Ativar o dispositivo GPS

Ativar um dispositivo significa simplesmente adicionar um novo dispositivo à sua conta de usuário. Você pode ativar qualquer [dispositivo de rastreamento GPS compatível](https://navixy.com/devices/). Se o seu modelo ainda não for suportado, entre em contato com o seu [provedor de serviços](provedor-de-servicos.md) para integrar esse dispositivo à Navixy ou encontrar um dispositivo alternativo com funcionalidade semelhante. Sugerimos também que entre em contato com seu [provedor de serviços](provedor-de-servicos.md) antes de prosseguir, pois eles podem ter suas próprias recomendações.

Há dois métodos para ativar um dispositivo de rastreamento GPS:

1. [**Ativar o dispositivo GPS automaticamente (recomendado)**](https://squaregps.atlassian.net/wiki/spaces/UDOCPT/pages/3025240148/Ativar+o+dispositivo+GPS#Activate-GPS-device-automatically) - simplifica a instalação do dispositivo, configurando-o automaticamente sem nenhuma intervenção manual. Esse método é recomendado para a maioria dos casos, exceto [Quando a ativação manual é necessária ou preferida](https://squaregps.atlassian.net/wiki/spaces/UDOCPT/pages/edit-v2/3025240148#When-manual-activation-is-required-or-preferred).
2. [**Ativar o dispositivo GPS manualmente**](https://squaregps.atlassian.net/wiki/spaces/UDOCPT/pages/edit-v2/3025240148#Activate-GPS-device-manually) - requer que você insira fisicamente as definições de configuração no dispositivo usando o configurador ou, de forma mais direta, por SMS. Essa opção é útil se a configuração automática não for viável devido a restrições técnicas ou regionais específicas.

## Ativar o dispositivo GPS automaticamente

A Navixy oferece a vantagem exclusiva da ativação totalmente automática de dispositivos, o que, geralmente, libera os usuários da necessidade de configurar manualmente seus dispositivos. O processo inclui o envio de comandos de configuração inicial para um dispositivo que você está conectando por meio de mensagem de texto (SMS). No entanto, se a ativação automática não for adequada para o seu caso, você sempre pode [Configurar o dispositivo manualmente](https://squaregps.atlassian.net/wiki/spaces/UDOCPT/pages/edit-v2/3025240148#Activate-GPS-device-manually).

### Etapas de ativação automática

Após fazer login na sua conta de usuário, navegue até Device activation (Ativação do dispositivo) no menu à esquerda. Isso iniciará o assistente de ativação.

1. **Nome do objeto:** Escolha o nome que preferir (por exemplo, "Veículo ABC").
2. **Modelo e fabricante do dispositivo:** Pesquise e selecione em uma lista classificada em ordem alfabética e agrupada por fabricantes.
3. **Digite o número de telefone do cartão SIM:** Digite o número de telefone do cartão SIM instalado no dispositivo.
  1. A plataforma Navixy tentará determinar as configurações de APN apropriadas com base no número de telefone que você forneceu. Se as configurações de APN não forem encontradas, você precisará inseri-las manualmente.
4. **Digite a ID/IMEI de fábrica do dispositivo:**
  1. O comprimento desse valor pode mudar dependendo do modelo. Em caso de dúvidas, entre em contato com o seu [provedor de serviços](provedor-de-servicos.md).
5. **Código de ativação (opcional):**
  1. Se for exigido pelo seu provedor de serviços, ele poderá ter que fornecer um código de ativação antes que você possa registrar um dispositivo.
6. **Ativar:** Após inserir as informações necessárias, clique em "Next Step" (Próxima etapa). Em seguida, mensagens SMS contendo comandos de configuração serão enviadas para o dispositivo. Certifique-se de que o dispositivo esteja ligado e consiga receber essas mensagens.

Em cerca de 15 minutos, o dispositivo deve ficar on-line e pronto para uso, dependendo das configurações padrão de relatório do dispositivo.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Detalhes sobre a configuração automática

Com a ativação automática, a configuração do dispositivo é simples e fácil de usar, sem a necessidade de cabos USB, drivers ou utilitários de configuração. O processo é rápido, permitindo que o dispositivo esteja operacional em poucos minutos. Os parâmetros de configuração, como as configurações de APN e os detalhes do servidor, são enviados automaticamente por SMS do servidor para o dispositivo. Uma vez conectado, o dispositivo recebe atualizações automáticas, como as configurações do modo de rastreamento, principalmente pelo canal IP.

## Ativar o dispositivo GPS manualmente

Enquanto a Navixy oferece [ativação automática do dispositivo GPS](https://squaregps.atlassian.net/wiki/spaces/UDOCPT/pages/edit-v2/3025240148#Activate-GPS-device-automatically) que simplifica o processo de configuração, há casos em que a configuração manual pode ser necessária ou preferida. Esta seção aborda as etapas para a configuração manual do dispositivo e os casos de uso específicos em que esse método é preferido.

### Etapas de ativação manual

Para ativar manualmente o dispositivo, é necessário enviar os comandos de ativação por SMS manualmente ou conectar-se fisicamente ao configurador do dispositivo com o PC. As informações necessárias para qualquer uma das opções são as seguintes:

1. **Credenciais de APN** \- Você pode obter essas informações com o provedor do SIM. Os dispositivos normalmente exigem: Nome do APN e/ou usuário do APN, senha do APN, se necessário.
2. **Endereço do servidor** - Escolha o endereço do servidor com base em suas preferências de residência de dados e/ou nas recomendações do provedor de serviços:
  - Plataforma da UE: `tracker.navixy.com` (recomendado) ou `52.57.1.136`
  - Plataforma dos EUA: `tracker.us.navixy.com` (recomendado) ou `13.52.37.2`
3. **Porta do servidor** - Esse parâmetro depende da marca e do modelo de seu dispositivo e pode ser encontrado na seção [Seção Dispositivos](https://navixy.com/devices/) de nosso site. Por exemplo, para [Queclink GV65](https://www.navixy.com/devices/queclink/queclink-gv65/) a porta do servidor seria 47764.

Atualize esses campos no configurador do seu dispositivo para começar a se conectar à nossa plataforma.

Para a ativação por SMS, consulte o manual do dispositivo ou a equipe de suporte para obter os comandos de SMS usados para ativar seu dispositivo específico.

> [!INFO]
> Observação: a ativação de SMS depende muito da capacidade do seu provedor de SIM. De acordo com nossa experiência, os comandos de SMS de um telefone comum não conseguem chegar a um dispositivo. Nesse caso, você deve utilizar o portal do seu provedor de SIM para enviar as mensagens.

### Quando a ativação manual é necessária ou preferida

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Dispositivos celulares com problemas de capacidade de entrega de SMS

Embora a Navixy e seus parceiros utilizem gateways de SMS com alta capacidade de entrega e cobertura mundial, alguns países têm regulamentações locais e problemas técnicos que podem impedir a entrega de comandos M2M enviados por mensagens de texto SMS. Esses problemas incluem:

- **Regulamentos anti-spam**: Restrições locais sobre nomes de remetentes de mensagens, comprimento de texto e textos binários.
- **Problemas técnicos**: Símbolos especiais como $, # e %, usados nos comandos de configuração, podem não passar por todos os nós da rede na cadeia de entrega de SMS com êxito.

Se a configuração automática falhar devido a esses problemas, você poderá configurar manualmente os parâmetros básicos, como credenciais de APN, endereço do servidor e porta. A porta do servidor e o endereço IP de um modelo específico de dispositivo podem ser encontrados na seção Dispositivos do nosso site. Para obter instruções detalhadas de configuração, consulte o manual do dispositivo ou consulte o suporte técnico de sua empresa. [provedor de serviços](provedor-de-servicos.md).

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Dispositivos conectados via protocolo MQTT

Os dispositivos MQTT, que usam o modelo Editor/Assinante para comunicação, exigem um processo de configuração exclusivo. Esses dispositivos devem ser configurados manualmente porque não seguem o modelo cliente-servidor tradicional. Você precisa:

1. Configure o dispositivo com as definições apropriadas do broker MQTT.
2. Configure manualmente os parâmetros de conexão do dispositivo, como o endereço e a porta do corretor MQTT.
3. Certifique-se de que os tópicos e as credenciais de segurança corretos estejam configurados.

Consulte o[Activate Your MQTT Device on Navixy](https://squaregps.atlassian.net/wiki/spaces/SC/pages/2732589133/Activate+Your+MQTT+Device+on+Navixy) seção de nossa [Centro de Especialistas](https://squaregps.atlassian.net/wiki/spaces/SC) para obter mais detalhes.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Dispositivos conectados via rede LoRa

As redes LoRa (Long Range), que são comumente usadas para aplicativos de IoT devido aos seus recursos de baixa potência e longo alcance, também exigem configuração manual. Isso ocorre porque as redes LoRa operam de forma diferente das redes celulares padrão que usam gateways LoRaWAN com requisitos específicos:

- Insira manualmente as credenciais LoRaWAN do dispositivo
- Configure o endereço do servidor e os parâmetros de rede para corresponder às especificações da rede LoRa

Essa configuração é, de certa forma, exclusiva para cada integração. Portanto, consulte o suporte técnico de seu [provedor de serviços](provedor-de-servicos.md) sobre como integrar seus dispositivos LoRa e o gateway LoRaWAN com a Navixy.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Dispositivos conectados via rede de satélite

Os dispositivos que usam redes de satélite, como Iridium, Globalstar ou Starlink, precisam de configuração manual devido à natureza distinta da comunicação via satélite, que difere significativamente das redes terrestres.

Os dispositivos que usam um link de satélite e a plataforma Navixy se comunicam por meio de um gateway fornecido pela operadora de satélite. Esse gateway funciona como uma ponte entre a rede de satélite e a Internet, garantindo uma transmissão de dados perfeita.

Para configurar um dispositivo de satélite para ser monitorado na Navixy, você precisa:

1. Aponte seu dispositivo para a rede de satélites
2. No lado da rede de satélites, faça com que o sistema deles aponte os dados para a plataforma Navixy
3. Verifique se o dispositivo está registrado corretamente e é capaz de se comunicar com a rede de satélites.

Como cada integração pode ser única, consulte o suporte técnico de sua empresa. [provedor de serviços](provedor-de-servicos.md) para obter orientação sobre a integração de seus dispositivos e gateway com a Navixy.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Dispositivos conectados por meio de outros sistemas telemáticos ou gateways

Há cenários onde os dispositivos já estão conectados a outros sistemas telemáticos, como plataformas telemáticas OEM ou outros servidores GPS, e você precisa que eles sejam monitorados tanto nessa plataforma quanto na Navixy.

Para monitorar dispositivos que fazem parte de outros sistemas de telemática com a Navixy, você precisa:

- Configurar a transmissão de dados:  
Configure a outra plataforma para enviar dados para a Navixy usando um dos protocolos suportados pela Navixy.
- Adicione um dispositivo virtual:  
Crie um dispositivo virtual na plataforma Navixy que mapeie a fonte de dados usando um identificador de dispositivo exclusivo.

Para obter mais detalhes, leia como [Integrar dados de IoT de servidores e gateways](https://squaregps.atlassian.net/wiki/spaces/SC/pages/2732621933/Integrate+IoT+Data+from+Servers+and+Gateways).

## Perguntas frequentes e solução de problemas

Se você tiver algum problema ao ativar seus dispositivos, consulte nosso [F.A.Q. e Guia de solução de problemas](../faq/solucao-de-problemas-de-ativacao-do-dispositivo-gps.md) ou entre em contato com o seu [Provedor de serviços](provedor-de-servicos.md) para assistência.