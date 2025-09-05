# Intrusão de casos

## Visão geral

A regra "Case Intrusion" foi projetada para dispositivos GPS que suportam um alerta quando o estojo do dispositivo é violado ou aberto, garantindo que você seja imediatamente notificado sobre qualquer acesso não autorizado aos seus dispositivos.

Essa regra é vital para aumentar a segurança e a proteção de cargas valiosas durante o trânsito ou o armazenamento. Ao usar rastreadores equipados com a regra "Case Intrusion", você pode adicionar uma camada extra de segurança para proteger seus ativos.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração de hardware do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Temporizador de descanso.** O alerta "Case Intrusion" tem um cronômetro de reinicialização de 1 minuto, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada minuto. Se um evento ocorrer durante o período de reinicialização, ele será omitido da plataforma, inclusive nos relatórios.
- **Vários dispositivos.** Você pode selecionar vários rastreadores GPS que acionarão notificações quando ocorrer um evento de violação. O único requisito é que os rastreadores selecionados sejam compatíveis com eventos de detecção de violação e tenham esse recurso integrado à plataforma.

- **Alerta de evento independente de GPS.** Essa regra funciona independentemente das coordenadas de GPS. Se a plataforma receber um evento de violação de um rastreador sem dados de GPS válidos, o evento ainda será contado como válido e exibido, independentemente de ter ocorrido dentro ou fora de uma delimitação geográfica. Nesses casos, as configurações do botão de rádio Inside/Outside para geofences são ignoradas para garantir que eventos potencialmente críticos não sejam perdidos.