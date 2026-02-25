# Auto-geofencing

## Visão geral

O recurso "Auto geofencing", disponível em alguns dispositivos de rastreamento GPS, é uma solução robusta projetada para aumentar a segurança do veículo, evitando reboques ou roubos não autorizados.

Esse recurso estabelece automaticamente uma cerca geográfica em torno da localização atual do veículo quando a ignição é desligada. Se o veículo se mover para fora desse limite predefinido sem que a ignição seja acionada, o sistema imediatamente dispara um alerta, fornecendo uma camada adicional de proteção. A utilização do recurso de delimitação geográfica automática requer um rastreador GPS compatível com essa funcionalidade.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração de hardware do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro**: O alerta "Auto Geofencing" tem um cronômetro de reinicialização de 1 minuto, o que significa que ele não será acionado mais do que uma vez a cada minuto. Se ocorrer um evento durante o período de reinicialização, ele será omitido dos relatórios.
- **Vários dispositivos**: Você pode selecionar vários rastreadores para essa regra, desde que eles suportem eventos de Auto Geofencing e que o recurso esteja integrado à plataforma. Essa flexibilidade permite que você monitore vários veículos ou ativos simultaneamente.
- **Alerta de evento independente de GPS**: Se a plataforma receber um evento de Auto Geofencing de um rastreador sem coordenadas GPS válidas, o evento ainda será contado como válido e exibido. Isso garante que eventos críticos não sejam perdidos, independentemente de sua ocorrência dentro ou fora das cercas geográficas definidas.