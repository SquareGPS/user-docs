# Dispositivo ligado/desligado

## Visão geral

A regra "Device switched ON/OFF" permite que os usuários monitorem quando um dispositivo GPS é ligado ou desligado. Essa regra é particularmente útil para gerentes que precisam garantir que os funcionários estejam usando dispositivos GPS de acordo com as políticas prescritas durante o horário de trabalho. Ela fornece informações valiosas sobre os padrões de uso do dispositivo, ajudando a evitar o uso indevido e garantindo que os dispositivos estejam funcionando corretamente.

> [!WARNING]
> Essa regra se aplica somente a dispositivos que têm a capacidade de informar seu status de energia. Em outras palavras, o dispositivo GPS deve ser capaz de enviar notificações à plataforma quando estiver ligado ou desligado. Se um dispositivo não tiver essa funcionalidade, a regra não poderá ser aplicada, pois a plataforma não receberá os dados necessários para acionar as notificações, mas você ainda poderá usar o dispositivo independente "[Perda de conexão do dispositivo](../conexao-do-dispositivo/perda-de-conexao-do-dispositivo.md)".

## Configurações de regras

### Rastreador ligado

A regra "Tracker switched ON" aciona uma notificação quando um rastreador é ligado, desde que o dispositivo tenha a funcionalidade de relatório necessária.

**Pontos principais:**

- **Objetivo:** Monitora quando um rastreador é ligado, ajudando-o a acompanhar quando os dispositivos voltam a funcionar.
- **Reiniciar o cronômetro:** O alerta "Rastreador ligado" inclui um Temporizador de reinicialização de 60 segundosque impede o envio de vários alertas em um único minuto, reduzindo as notificações desnecessárias.
- **Configuração:** A regra exige uma configuração mínima e é compatível com vários rastreadores, desde que eles tenham a capacidade de relatar eventos de ativação.

### Rastreador ligado/desligado

A regra "Tracker switched OFF" (Rastreador desligado) aciona uma notificação quando um rastreador é desligado ou perde a conexão, desde que o dispositivo possa relatar esse evento e acione novamente quando for ligado.

**Pontos principais:**

- **Objetivo:** Notifica você quando um rastreador é desligado ou perde a conexão, permitindo que você responda rapidamente a possíveis problemas.
- **Reiniciar o cronômetro:** Esse alerta inclui um Temporizador de reinicialização de 10 segundosgarantindo que os alertas não sejam acionados com mais frequência do que uma vez a cada 10 segundosevitando notificações excessivas.
- **Configuração:** Semelhante à regra "Tracker switched ON" (Rastreador ligado), essa regra também requer configuração mínima e pode ser aplicada a vários rastreadores que suportam relatórios de eventos de desligamento.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- A regra "Tracker switched ON/OFF" (Rastreador ligado/desligado) opera com base nos eventos de hardware gerados pelo rastreador quando ele é ligado ou desligado. Esses eventos são transmitidos para a plataforma e processados para notificação.
- A regra é flexível e pode ser aplicada a vários rastreadores simultaneamente, desde que eles suportem o recurso de evento ON/OFF.
- Se a plataforma identificar um evento de hardware desse tipo sem coordenadas válidas, o evento ainda será contado como válido e exibido, garantindo que nenhum evento crucial seja perdido.
- O sistema permite que você rastreie esses eventos, independentemente de ocorrerem dentro ou fora das cercas geográficas definidas, pois a lógica da cerca geográfica é ignorada para esses eventos específicos a fim de garantir um monitoramento abrangente.

Essa regra é fundamental para manter a integridade operacional da sua frota, garantindo que todos os rastreadores estejam funcionando conforme o esperado e permitindo respostas rápidas a qualquer alteração inesperada no status do rastreador.