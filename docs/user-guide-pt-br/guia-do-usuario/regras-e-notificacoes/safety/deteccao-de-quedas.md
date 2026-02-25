# Detecção de quedas

## Visão geral

A regra "Detecção de quedas" foi criada para garantir a segurança e o bem-estar dos indivíduos, detectando e notificando os usuários sobre possíveis quedas ou acidentes.

Essa regra usa sensores e algoritmos avançados para monitorar os padrões de movimento e a orientação dos dispositivos GPS pessoais. Se o sistema detectar uma mudança repentina e significativa na posição ou na aceleração, ele identifica o fato como uma possível queda e aciona uma notificação.

Essa funcionalidade é especialmente valiosa para monitorar idosos, trabalhadores solitários ou outras pessoas que possam estar vulneráveis a quedas. Ao fornecer alertas em tempo real, o sistema permite resposta e assistência imediatas, aumentando a segurança geral e oferecendo tranquilidade aos cuidadores e entes queridos.

## Configurações de regras

A funcionalidade dessa regra depende dos recursos e da configuração do dispositivo, portanto, não são necessárias configurações de regras específicas.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Detecção de queda" tem um cronômetro de reinicialização de 30 segundos, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada 30 segundos. Se ocorrer um evento enquanto a regra estiver no período de reinicialização, a plataforma suprimirá o alerta, garantindo que as notificações e os relatórios permaneçam claros e gerenciáveis.
- **Vários dispositivos:** Essa regra pode ser aplicada a vários rastreadores GPS pessoais, desde que eles suportem eventos de "Detecção de queda" e tenham esse recurso integrado à plataforma. Isso permite que os usuários monitorem eventos de detecção de quedas em vários dispositivos, garantindo uma cobertura abrangente.
- **Processamento de eventos independente de GPS:** A plataforma processa e exibe eventos de detecção de queda mesmo que o pacote de dados não tenha coordenadas GPS válidas. Esses eventos são registrados independentemente de ocorrerem dentro ou fora de uma geocerca designada. As configurações de geocerca interna/externa são ignoradas nesse caso, garantindo que nenhum evento crítico seja perdido.