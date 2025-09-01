# Conectar/desconectar dispositivo OBDII

## Visão geral

A regra "OBDII Device Plug / Unplug" foi projetada para fornecer alertas imediatos sempre que um rastreador GPS OBDII for conectado ou desconectado da porta OBDII do veículo. Essa regra garante que os usuários possam tomar medidas imediatas para manter o rastreamento contínuo e a funcionalidade do dispositivo.

Por exemplo, quando o rastreador é desconectado, ele muda para sua bateria interna, que tem uma vida útil limitada. As notificações imediatas após a desconexão permitem que os usuários respondam rapidamente, garantindo o rastreamento ininterrupto e a transmissão de dados.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração de hardware do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro.** O alerta "OBDII Device Plug/Unplug" tem um cronômetro de reinicialização de 5 minutos, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada 5 minutos. Se o evento ocorrer enquanto a regra estiver no período de reinicialização, ele será omitido pela plataforma, inclusive nos relatórios.
- **Vários dispositivos.** **Vários dispositivos:** Os usuários podem selecionar vários rastreadores para monitorar sob essa regra. O único requisito é que os dispositivos selecionados sejam compatíveis com eventos de conexão/desconexão da porta OBDII. Essa flexibilidade permite que os usuários monitorem esse tipo de evento em vários veículos ou dispositivos de forma conveniente.
- **Alerta de evento independente de GPS.** O sistema processa esses eventos independentemente de os dados de GPS estarem disponíveis. O evento ainda será registrado e exibido, mesmo que ocorra fora das cercas geográficas definidas.