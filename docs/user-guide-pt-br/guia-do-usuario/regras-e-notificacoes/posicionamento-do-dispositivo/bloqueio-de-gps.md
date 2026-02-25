# Bloqueio de GPS

## Visão geral

O bloqueio de GPS ocorre quando as frequências de GPS ou GNSS são interrompidas por interferência de fontes próximas, um processo conhecido como mascaramento ou mascaramento de frequência. Essa interferência pode fazer com que o dispositivo perca a conexão com os satélites, levando a dados de GPS distorcidos ou completamente perdidos. O bloqueio de GPS é diferente de [Bloqueio de GSM](../conexao-do-dispositivo/bloqueio-de-gsm.md)pois eles operam em bandas de frequência separadas. Quando ocorre um bloqueio de GPS, o dispositivo pode perder a conexão com o satélite, resultando em zero satélites visíveis ou em coordenadas inválidas que a plataforma de rastreamento não consegue recuperar.

A regra de interferência de GPS aumenta a segurança de veículos e ativos, evitando roubos em cenários em que a interferência do sinal de GPS é usada para desativar os sistemas de rastreamento. Por exemplo, se um veículo for alvo de roubo ou sequestro, essa regra fornece um alerta em tempo hábil, permitindo uma ação rápida para evitar perdas ou danos. É uma ferramenta essencial para que as empresas protejam suas frotas e ativos valiosos.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração de hardware do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "GPS jamming" tem um cronômetro de reinicialização de 5 minutos, o que significa que o alerta não será acionado mais de uma vez a cada 5 minutos. Se um evento ocorrer durante o período de reinicialização, ele será omitido da plataforma, inclusive dos relatórios.
- **Vários dispositivos:** Essa regra permite que você selecione vários rastreadores para receber notificações, desde que os rastreadores selecionados suportem eventos de interferência de GPS e que o recurso esteja integrado à plataforma. Essa flexibilidade permite o monitoramento de eventos de interferência de GPS em vários veículos ou dispositivos.
- **Alerta de evento independente de GPS:** A plataforma registrará e exibirá o evento mesmo que ele seja recebido em um pacote sem coordenadas válidas. O evento será exibido independentemente de ter ocorrido dentro ou fora das cercas geográficas delimitadas, pois a plataforma prioriza a exibição de eventos potencialmente críticos em vez de omiti-los.

## Veja também

- [Bloqueio de GSM](../conexao-do-dispositivo/bloqueio-de-gsm.md)