# Ausência do motorista

## Visão geral

O evento "Driver Absence" (Ausência do motorista) foi projetado para monitorar e garantir a presença do motorista no assento do veículo. Esse recurso é particularmente importante para evitar que o veículo seja deixado sem vigilância em situações em que isso possa representar um risco de segurança ou violar as políticas da empresa.

### Como funciona

Esse recurso geralmente se baseia em sistemas de vídeo no veículo equipados com IA e sensores para monitorar continuamente o assento do motorista. Esses sistemas usam uma combinação de reconhecimento visual (por meio de câmeras) e dados de sensores para detectar a presença ou ausência de um motorista. Se o sistema detectar que o assento do motorista está desocupado quando o veículo está em operação ou quando deveria ser atendido, ele aciona um evento de "Ausência de motorista".

Esse evento é então comunicado à plataforma telemática da Navixy, que pode gerar alertas, registrar o evento e notificar o pessoal apropriado. Um alerta pode ser acionado, por exemplo, se o veículo estiver em movimento e o sistema detectar que não há motorista no assento, ou se o motorista sair do assento sem prender o veículo adequadamente.

### Aplicativos

- **Segurança da frota:** Garantir que os veículos não sejam operados sem motorista, evitando acidentes e uso não autorizado.
- **Segurança:** Alertar os gerentes de frota se um veículo for deixado sem vigilância em uma área potencialmente perigosa ou de alto risco.
- **Conformidade:** Ajudar as frotas a cumprir as normas de segurança que exigem a presença de um motorista durante a operação do veículo.
- **Seguro:** Fornecer evidências em caso de incidentes em que a ausência do motorista possa ser um fator, o que pode ser necessário para reivindicações de seguro ou para fins legais.

O evento "Ausência do motorista" é um componente essencial para aumentar a segurança da frota, fornecendo aos gerentes de frota as ferramentas necessárias para monitorar e responder a situações em que a presença do motorista é necessária.

## Configurações de regras

Não são necessárias configurações específicas para essa regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Ausência de motorista" tem um cronômetro de reinicialização de 10 segundos, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada 10 segundos. Se ocorrer um evento enquanto a regra estiver no período de reinicialização, a plataforma suprimirá o alerta, mantendo as notificações e os relatórios claros e gerenciáveis.

- **Vários dispositivos:** Essa regra pode ser aplicada a vários rastreadores, desde que eles suportem eventos de "Ausência do motorista" e tenham esse recurso integrado à plataforma. Isso permite que os usuários monitorem esses eventos em vários veículos ou dispositivos de forma conveniente.

- **Processamento de eventos independente de GPS:** A plataforma processa e exibe eventos de ausência do motorista mesmo que o pacote de dados não tenha coordenadas GPS válidas. Esses eventos são registrados independentemente de ocorrerem dentro ou fora de uma geofence designada. As configurações de geocerca interna/externa são ignoradas nesse caso, garantindo que nenhum evento crítico seja perdido.