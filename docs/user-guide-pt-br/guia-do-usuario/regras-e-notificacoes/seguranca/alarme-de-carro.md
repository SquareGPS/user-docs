# Alarme de carro

## Visão geral

A regra "Car alarm triggered" (Alarme de carro acionado) foi criada para aumentar a segurança de sua frota, fornecendo notificações em tempo real quando o sistema de alarme de um veículo é ativado. Essa regra ajuda a proteger seus ativos, alertando prontamente a sua equipe sobre possíveis incidentes de roubo, acesso não autorizado ou adulteração.

Essa regra funciona monitorando o sistema de alarme do veículo por meio de um dispositivo de rastreamento GPS conectado. Normalmente, o sinal de saída do sistema de alarme é conectado à entrada do dispositivo de GPS. Quando o alarme é acionado, o dispositivo GPS detecta esse sinal e envia um alerta para a plataforma.

## Configurações de regras

Não são necessárias configurações de regras específicas. Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Car Alarm Triggered" (Alarme de carro acionado) tem um cronômetro de reinicialização de 5 minutos, o que significa que o alerta não será acionado mais de uma vez a cada 5 minutos. Se ocorrer um evento durante o período de reinicialização, a plataforma suprimirá o alerta, mantendo as notificações e os relatórios claros e concisos.

- **Vários dispositivos:** Essa regra pode ser aplicada a vários rastreadores, desde que eles sejam compatíveis com eventos "Car Alarm Triggered" e tenham esse recurso integrado à plataforma. Isso permite que você monitore esses alertas em vários veículos ou dispositivos com eficiência.

- **Alerta de evento independente de GPS:** A plataforma processa e exibe eventos de alarme de carro mesmo que o pacote de dados não tenha coordenadas de GPS válidas. Esses eventos são registrados independentemente de ocorrerem dentro ou fora de uma delimitação geográfica designada. As configurações de geocerca interna/externa são ignoradas nesse caso, garantindo que nenhum evento crítico seja perdido.