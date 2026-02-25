# Pressionar o botão SOS

## Visão geral

O recurso "Pressing SOS Button" (Pressionando o botão SOS), comumente chamado de "botão SOS", é uma função de segurança essencial projetada para dispositivos GPS equipados com um botão de emergência. Esse botão pode ser um componente externo ou integrado em um dispositivo de rastreamento pessoal. Ele serve como um salva-vidas vital em situações críticas, permitindo que funcionários e indivíduos solicitem assistência rapidamente quando for mais necessário.

## Configurações de regras

A funcionalidade dessa regra depende dos recursos e da configuração do dispositivo, portanto, não são necessárias configurações de regras específicas.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Conexão de um botão externo à entrada do dispositivo GPS do veículo

Dependendo do dispositivo, o botão SOS pode ser conectado a uma entrada dedicada, projetada especificamente para essa função, ou a uma entrada discreta geral. Se estiver conectado a uma entrada discreta, você deverá criar a entrada no menu Devices and Settings (Dispositivos e configurações) na seção Sensors and Buttons (Sensores e botões). Nesse caso, selecione o tipo de regra "Input Triggering" (Acionamento de entrada) para a configuração adequada.

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Pressionando o botão SOS" tem um cronômetro de reinicialização de 30 segundos, o que significa que o alerta não será acionado mais de uma vez a cada 30 segundos. Se ocorrer um evento enquanto a regra estiver aguardando a reinicialização, a plataforma omitirá o evento, inclusive nos relatórios.
- **Vários dispositivos:** Essa regra permite que os usuários selecionem vários rastreadores dos quais desejam receber notificações. Os rastreadores selecionados devem ser compatíveis com o evento "Pressing SOS Button" (Pressionar botão SOS), e esse recurso deve ser integrado à plataforma desses rastreadores. Isso permite que os usuários monitorem sinais de emergência em vários dispositivos de forma conveniente.
- **Alerta de evento independente de GPS:** A plataforma reconhece e conta esse tipo de evento de hardware mesmo que o pacote de dados não tenha coordenadas de GPS válidas. O evento será exibido independentemente de ter ocorrido dentro ou fora das cercas geográficas definidas. As configurações de geocerca interna/externa são ignoradas nesse caso, garantindo que nenhum evento crítico seja omitido.