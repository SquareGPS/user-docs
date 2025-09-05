# Desvinculação do rastreador

## Visão geral

A regra "Tracker detach from the object" alerta os usuários quando um dispositivo de rastreamento GPS é removido do veículo ou do ativo que está monitorando. A disponibilidade dessa regra depende dos recursos e da configuração do dispositivo. Dependendo do design do dispositivo, ele pode usar vários sensores, como pontos de contato ou sensores de luz, para detectar o desprendimento.

Essa regra é essencial para a segurança de ativos e a prevenção de perdas, permitindo que as empresas respondam rapidamente a possíveis roubos, adulterações ou manuseio não autorizado. Ela é especialmente valiosa em setores como logística e transporte, em que a proteção de ativos durante o trânsito ou armazenamento é fundamental.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro.** O alerta "Tracker detach from the object" tem um cronômetro de reinicialização de 1 minuto, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada minuto. Se um evento ocorrer durante o período de reinicialização, ele será omitido da plataforma, inclusive nos relatórios.
- **Vários dispositivos.** Os usuários têm a flexibilidade de selecionar vários dispositivos GPS para receber notificações quando o dispositivo é desconectado de um objeto. O único requisito é que os rastreadores selecionados sejam compatíveis com os eventos "Tracker detach from the object" e tenham esse recurso integrado à plataforma.

- **Alerta de evento independente de GPS.** Se a plataforma receber um evento de desprendimento de um rastreador sem dados de GPS válidos, o evento ainda será contado como válido e exibido, independentemente de ter ocorrido dentro ou fora de uma delimitação geográfica. Nesses casos, as configurações Dentro/Exterior das cercas geográficas são ignoradas para garantir que eventos potencialmente críticos não sejam perdidos.