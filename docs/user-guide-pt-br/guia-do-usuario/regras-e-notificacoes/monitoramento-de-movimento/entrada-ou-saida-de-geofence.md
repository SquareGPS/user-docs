# Entrada ou saída de geofence

## Visão geral

Uma geofence é uma área designada em um mapa que atua como um limite virtual. Essa regra rastreia quando os rastreadores entram ou saem da área de geofence especificada. Os usuários receberão notificações sempre que seus objetos cruzarem esses limites de geofence. Por exemplo, se uma peça de maquinário de construção sair da zona designada, um funcionário da empresa poderá ser notificado por meio da interface do usuário, e-mail ou SMS, se configurado na regra.

![image-20240805-231934.png](attachments/image-20240805-231934.png)

Essa funcionalidade fornece insights valiosos e controle sobre a movimentação de objetos, garantindo a adesão a limites predefinidos. Ela aumenta a segurança ao alertar os usuários sobre qualquer movimento não autorizado ou possível roubo fora da área de geofence especificada. Além disso, possibilita o gerenciamento eficiente de ativos, permitindo que os usuários rastreiem e otimizem a utilização de seus equipamentos dentro das zonas designadas.

## Configurações de regras

#### Cercas geográficas

Especifique as cercas geográficas que acionarão as notificações quando forem ultrapassadas. Você pode listar várias cercas geográficas em uma única regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- O alerta "Geofence entrance or exit" tem um cronômetro de reinicialização de 60 segundos, o que significa que o alerta não será acionado mais do que uma vez a cada minuto. Se ocorrer um evento enquanto a regra estiver aguardando a reinicialização, a plataforma omitirá o evento, inclusive nos relatórios.
- Essa regra é processada na nuvem e não está vinculada a nenhum hardware específico, o que permite que ela seja aplicada a vários rastreadores simultaneamente. Essa flexibilidade permite que você gerencie vários rastreadores em uma única regra.
- Observe que o sistema pode gerar um alerta de entrada/saída mesmo que ocorra um desvio de GPS. Embora as coordenadas inválidas de GPS sejam filtradas, pequenos desvios de GPS ainda podem aparecer na trilha. Vários métodos para evitar eventos de desvio de GPS estão disponíveis, dependendo da funcionalidade do modelo do rastreador. Para obter detalhes sobre como evitar o desvio de GPS, consulte o manual do dispositivo.