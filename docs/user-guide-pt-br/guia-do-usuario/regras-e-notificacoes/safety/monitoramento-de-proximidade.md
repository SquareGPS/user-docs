# Monitoramento de proximidade

## Visão geral

A regra "Proximity monitoring" (Monitoramento de proximidade) aproveita a funcionalidade Bluetooth para fornecer alertas em tempo real quando ocorrem eventos de proximidade. Essa regra foi projetada para detectar distâncias precisas entre objetos equipados com dispositivos GPS que tenham recursos BLE (Bluetooth Low Energy), bem como entre dispositivos GPS e tags BLE. É uma ferramenta versátil que oferece inúmeras aplicações em vários setores.

Essa regra é particularmente benéfica em ambientes em que é fundamental manter distâncias específicas. Os exemplos incluem:

- **Uso de equipamentos perigosos:** Rastreie a proximidade dos operadores com equipamentos perigosos, evitando acidentes e garantindo a conformidade com as normas de segurança.

- **Distanciamento social em ambientes epidêmicos:** Manter e aplicar medidas de distanciamento social em locais de trabalho ou áreas públicas durante epidemias, ajudando a reduzir a disseminação de doenças contagiosas.

Ao empregar essa regra, as organizações podem aumentar a segurança, garantir a conformidade com os regulamentos e otimizar o gerenciamento das atividades relacionadas à proximidade.

## Configurações de regras

A funcionalidade dessa regra depende dos recursos e da configuração do dispositivo, portanto, não são necessárias configurações de regras específicas.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## As especificações da plataforma:

- **Reiniciar o cronômetro:** O alerta "Proximity monitoring" (Monitoramento de proximidade) tem um cronômetro de redefinição de 10 segundos, o que significa que o evento de alerta não ocorrerá com mais frequência do que uma vez a cada 10 segundos. Se esse tipo de evento ocorrer durante o tempo em que a regra estiver aguardando a redefinição, esse evento será omitido pela plataforma, incluindo os relatórios.
- **Vários dispositivos:** Essa regra permite que os usuários selecionem vários dispositivos dos quais desejam receber notificações. Os rastreadores selecionados devem ser compatíveis com o evento "Close proximity", e esse recurso deve estar integrado à plataforma desses rastreadores. Isso permite que os usuários monitorem eventos em vários dispositivos de forma conveniente.
- **Alerta de evento independente de GPS:** Sempre que a plataforma identifica um evento de hardware desse tipo a partir de um pacote de dados do rastreador sem coordenadas válidas, a plataforma conta o evento como válido e o exibe independentemente de o evento ter ocorrido dentro ou fora das cercas geográficas delimitadas para garantir notificações críticas.