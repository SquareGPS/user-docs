# Perda de conexão do dispositivo

## Visão geral

A regra "Device lost connection" foi criada para monitorar e notificar os usuários quando um dispositivo GPS perde a conexão com a plataforma. Essa perda de conexão pode ocorrer por vários motivos, como problemas de hardware (descarga de bateria, desconexão de energia, falha de hardware, problemas de fiação) ou problemas de comunicação (problemas de rede GSM, cobertura ruim, fundos insuficientes ou interrupções do provedor).

Essa regra ajuda os usuários a se manterem informados sobre o status operacional de seus dispositivos de rastreamento e permite respostas rápidas a possíveis problemas, como mau funcionamento do equipamento, interferência do GSM ou roubo de veículos. Ela também ajuda a coletar dados valiosos para otimizar as operações, como a identificação de áreas com cobertura ruim ou a detecção de falhas no equipamento ou no provedor de serviços.

> [!INFO]
> Para monitoramento em tempo real do status de energia do dispositivo, recomenda-se usar o [Recurso de autorrelato "Interruptor do dispositivo LIGADO/DESLIGADO"](/wiki/pages/createpage.action?spaceKey=USERDOCSOLD&title=Device%20switched%20ON%20%2F%20OFF)se suportado por seu dispositivo GPS.

## Configurações de regras

#### Tempo off-line mais de

A configuração "Offline time more than" permite que os usuários definam um cronômetro personalizado que começa a contagem regressiva depois que o rastreador entra em status vermelho (indicando perda de conexão). O período total de desconexão é calculado da seguinte forma:

- **Tempo limite padrão (10 minutos)**: Esse é o período padrão após o qual um rastreador é considerado como tendo perdido a conexão se nenhum dado for recebido do dispositivo.
- **Seu tempo limite off-line personalizado**: O tempo adicional especificado pelo usuário no campo "Offline time more than".

Por exemplo, se um dispositivo perder a conexão às 10h10, após o tempo limite padrão de 10 minutos, ele será marcado com um status vermelho às 10h20. Se o usuário definir o tempo limite off-line personalizado para 7 minutos, a notificação será acionada às 10h27.

Para configurações de regras comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- O alerta "Device lost connection" tem um cronômetro de redefinição de 10 segundos, o que significa que o alerta não será acionado mais do que uma vez a cada 10 segundos. Se ocorrer um evento enquanto a regra estiver aguardando a redefinição, ele será omitido pela plataforma, inclusive nos relatórios.
- Essa regra é processada na nuvem e não está vinculada a nenhum hardware específico, o que a torna aplicável a vários rastreadores simultaneamente. Essa flexibilidade permite que você gerencie vários rastreadores em uma única regra.
- Diferentes modelos de dispositivos têm tempos limite em nível de transporte variados. Se você incluir vários modelos de rastreadores na mesma regra, os períodos de notificação poderão ser diferentes com base nas configurações específicas de tempo limite do dispositivo. Essa variação ocorre porque a notificação é acionada por uma combinação do tempo limite padrão do rastreador e do tempo limite off-line personalizado especificado na configuração da regra.

Ao usar essa regra, os usuários podem garantir que sejam prontamente informados sobre quaisquer interrupções na conectividade do rastreador, o que lhes permite tomar medidas rápidas para resolver possíveis problemas.