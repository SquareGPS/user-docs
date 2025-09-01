# Corte de energia externa

## Visão geral

A regra "Corte de energia externa" foi projetada para rastreadores GPS de veículos com fio que dependem do sistema elétrico do veículo. Essa regra é crucial para o gerenciamento de frotas, pois monitora o fornecimento de energia ao dispositivo GPS e alerta os usuários quando a energia externa é desconectada.

Ao detectar um corte de energia, o dispositivo GPS alterna automaticamente para sua bateria interna (se disponível) para manter a funcionalidade e informar a plataforma. A plataforma registra esses eventos e notifica os usuários de acordo com as configurações da regra.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração de hardware do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro.** O alerta "Corte de energia externo" tem um cronômetro de reinicialização de 5 minutos, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada 5 minutos. Se ocorrer um evento durante o período de reinicialização, ele será omitido da plataforma e não será incluído nos relatórios.
- **Evento detectado pelo dispositivo.** Esse evento é acionado diretamente pelo dispositivo com base em sua configuração. Seu dispositivo e sua configuração devem suportar essa funcionalidade para que a regra possa ser usada.
- **Alerta de evento independente de GPS.** A plataforma registrará e exibirá o evento mesmo que ele seja recebido em uma mensagem sem coordenadas válidas, garantindo que os usuários sejam informados independentemente da localização do evento. As configurações Inside/Outside para cercas geográficas são ignoradas nesses casos, pois a plataforma prioriza a exibição de eventos potencialmente críticos.