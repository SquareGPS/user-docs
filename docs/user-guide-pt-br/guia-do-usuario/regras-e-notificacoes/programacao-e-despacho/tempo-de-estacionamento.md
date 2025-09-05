# Tempo de estacionamento

## Visão geral

A regra de tempo de estacionamento foi criada para notificar os usuários quando a duração do estacionamento de um veículo exceder um limite especificado. Essa regra é crucial para monitorar o tempo que os veículos permanecem parados, garantindo que os motoristas cumpram os padrões de tempo definidos para estacionamento e períodos de permanência.

Por exemplo, se o tempo de estacionamento permitido for definido como 30 minutos, o sistema alertará os usuários sempre que um veículo permanecer estacionado além desse limite. Essas notificações podem ser enviadas por meio da interface do usuário, e-mail ou SMS, e os usuários também podem gerar relatórios para analisar esses eventos historicamente.

## Configurações de regras

**Tempo de estacionamento permitido**  
O tempo de estacionamento começa a contar assim que o veículo entra em um estado estacionado. Os usuários podem configurar a duração permitida do estacionamento, com opções que variam de 5 a 60.000 minutos. O cronômetro é reiniciado quando o veículo sai do estado estacionado. Para obter informações mais detalhadas sobre a detecção de estacionamento, consulte o artigo Detecção de estacionamento.

Para monitorar o tempo de permanência em áreas específicas, vincule a regra às cercas geográficas designadas.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- O alerta "Parking Time" tem um cronômetro de redefinição de 10 segundos, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada 10 segundos. Se ocorrer um evento enquanto a regra estiver aguardando a reinicialização, a plataforma omitirá o evento, inclusive nos relatórios.
- Essa regra é processada na nuvem e não está vinculada a nenhum hardware específico, o que permite que ela seja aplicada a vários rastreadores simultaneamente. Essa flexibilidade permite que os usuários gerenciem vários rastreadores em uma única regra.