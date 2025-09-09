# Perda e recuperação do sinal de GPS

## Visão geral

A regra "Perda/recuperação de sinal de GPS" monitora a disponibilidade do sinal de GPS dos seus dispositivos. Essa regra aciona notificações quando um dispositivo perde o sinal de GPS, geralmente por estar em um local fechado, subterrâneo ou em uma área com pouca visibilidade do satélite, e quando o sinal é recuperado posteriormente. Ao receber essas notificações, você pode se manter informado sobre o status da localização dos seus ativos, mesmo em ambientes desafiadores.

Essa regra é particularmente útil em ambientes em que a cobertura do sinal de GPS não é confiável, como canteiros de obras, armazéns ou instalações subterrâneas. Garantir que seu rastreador mantenha conexões de celular e Internet é fundamental para receber esses alertas quando o sinal de GPS for perdido e recuperado.

## Configurações de regras

Essa regra é processada na nuvem, o que significa que o software do servidor monitora quando o sinal de GPS é perdido e quando é recuperado. Você pode aplicar essa regra a vários rastreadores simultaneamente, desde que os rastreadores suportem esse tipo de evento e que ele esteja integrado à plataforma.

Para ver as configurações de regras comuns, consulte a seção [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "sinal de GPS perdido/recuperado" tem um cronômetro de reinicialização de 10 segundos, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada 10 segundos. Se ocorrer um evento durante o período de reinicialização, ele será omitido pela plataforma, inclusive nos relatórios.
- **Vários dispositivos:** Você pode selecionar vários rastreadores para monitorar sob essa regra, desde que os rastreadores suportem eventos de perda/recuperação de sinal de GPS e que o recurso esteja integrado à plataforma. Isso permite que você gerencie vários dispositivos com eficiência.
- **Alerta de evento independente de GPS:** A plataforma registrará e exibirá esse evento mesmo que ele seja recebido em uma mensagem sem coordenadas válidas, garantindo que você seja informado independentemente da localização do evento. As configurações Inside/Outside para cercas geográficas são ignoradas nesses casos, pois a plataforma prioriza a exibição de eventos potencialmente críticos.