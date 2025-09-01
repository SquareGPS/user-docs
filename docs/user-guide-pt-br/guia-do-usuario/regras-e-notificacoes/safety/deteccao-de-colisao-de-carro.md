# Detecção de colisão de carro

## Visão geral

A regra "Car Crash Detection" monitora e alerta sobre eventos significativos de direção, detectando especificamente colisões de veículos. Essa regra ajuda a manter a consciência do comportamento do motorista e permite que a sua equipe de despacho responda rapidamente a qualquer acidente.

Essa regra depende do hardware e é acionada pelos dados do acelerômetro do dispositivo GPS. O evento é gerado no lado do dispositivo GPS e a plataforma exibe o alerta com base nos dados recebidos.

A detecção precisa de colisão requer a instalação adequada do rastreador, incluindo a fiação e o alinhamento corretos ao longo dos eixos x, y e z. Instruções detalhadas de instalação são normalmente fornecidas no manual do usuário do rastreador.

## Configurações de regras

Como essa regra é processada no dispositivo GPS e não na nuvem, não são necessárias configurações adicionais.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Car Crash Detection" tem um cronômetro de reinicialização de 1 minuto, o que significa que o alerta não será acionado com mais frequência do que uma vez por minuto. Se outro evento de colisão for detectado dentro desse período de reinicialização, ele será omitido da plataforma e dos relatórios.
- **Vários dispositivos:** Essa regra permite que você selecione vários rastreadores para notificações. O único requisito é que os rastreadores sejam compatíveis com eventos de detecção de colisão de carro e tenham esse recurso integrado à plataforma. Isso permite o monitoramento de eventos de colisão em vários veículos.
- **Alerta de evento independente de GPS:** A plataforma registrará e exibirá um evento de detecção de colisão de carro mesmo que o pacote de dados não tenha coordenadas de GPS válidas. O sistema prioriza a exibição de eventos críticos, independentemente de terem ocorrido dentro ou fora das cercas geográficas designadas. As configurações de geocerca interna/externa são ignoradas para essa regra a fim de garantir que nenhum evento crucial seja perdido.