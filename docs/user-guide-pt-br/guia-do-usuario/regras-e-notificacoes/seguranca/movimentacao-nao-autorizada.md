# Movimentação não autorizada

## Visão geral

A regra "Movimento não autorizado" foi criada para aumentar a segurança do veículo, alertando os usuários quando um veículo parado começa a se mover sem autorização. Essa regra é particularmente valiosa em situações em que se espera que o veículo permaneça parado, como quando é desligado, mas inesperadamente começa a se mover. Ela ajuda a identificar rapidamente possíveis roubos ou uso não autorizado, permitindo que os usuários tomem medidas rápidas.

**Aplicações típicas:**

- **Prevenção de roubos:** Alertas imediatos se um veículo for movido sem autorização.
- **Segurança do estacionamento:** Monitoramento de veículos em áreas de estacionamento designadas quanto a movimentos não autorizados.
- **Proteção de ativos:** Garantir que os veículos ou equipamentos estacionários permaneçam seguros fora do horário de expediente.

A regra funciona utilizando o acelerômetro integrado do dispositivo GPS e outras definições de configuração para detectar qualquer movimento não autorizado. A precisão dessa regra depende da instalação e da configuração adequadas do dispositivo, que variam de acordo com o modelo do dispositivo. Quando a plataforma recebe o pacote de dados indicando movimento não autorizado, ela processa e exibe o evento, fornecendo aos usuários alertas em tempo real.

## Configurações de regras

Essa regra depende totalmente dos recursos do dispositivo e da configuração do hardware. Normalmente, o dispositivo deve ser capaz de detectar quando o veículo não está em uso, por exemplo, monitorando o estado da ignição.

Não há configurações específicas a serem definidas na própria regra. Para obter configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Movimento não autorizado" tem um cronômetro de reinicialização de 5 minutos, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada 5 minutos. Se ocorrer um evento enquanto a regra estiver no período de reinicialização, a plataforma suprimirá o alerta, garantindo que as notificações e os relatórios permaneçam claros e gerenciáveis.
- **Vários dispositivos:** Essa regra pode ser aplicada a vários rastreadores, desde que eles suportem eventos de "Movimento não autorizado" e tenham esse recurso integrado à plataforma. Isso permite que os usuários monitorem o movimento não autorizado em vários veículos, garantindo uma cobertura de segurança abrangente.
- **Processamento de eventos independente de GPS:** A plataforma processa e exibe eventos de movimentação não autorizados, mesmo que o pacote de dados não tenha coordenadas de GPS válidas. Esses eventos são registrados independentemente de ocorrerem dentro ou fora de uma geofence designada. As configurações de geocerca interna/externa são ignoradas nesse caso, garantindo que nenhum evento crítico seja perdido.