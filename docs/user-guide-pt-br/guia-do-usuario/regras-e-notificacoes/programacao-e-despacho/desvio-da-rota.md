# Desvio da rota

## Visão geral

A regra de desvio de rota permite o monitoramento de desvios de uma rota predefinida. Essa regra garante que os veículos ou objetos sigam as rotas planejadas, melhorando a eficiência e aprimorando a segurança ao identificar e solucionar prontamente quaisquer desvios. Os usuários receberão notificações sempre que um veículo ou objeto se desviar da rota especificada, ajudando a manter a conformidade e a otimizar as operações.

## Configurações de regras

#### Roteamento de cercas geográficas em torno de caminhos

Para utilizar a regra de desvio de rota, você deve primeiro criar uma ou mais cercas geográficas de rota na plataforma. Siga estas etapas para configurar a regra:

1. **Criar cercas geográficas de rota**: Antes de configurar a regra, verifique se você criou cercas geográficas de rota categorizadas como "rota".
2. **Selecionar cercas geográficas**: Escolha as cercas geográficas de rota que deseja monitorar quanto a desvios. Somente as cercas geográficas categorizadas como "rota" podem ser usadas para essa finalidade.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- O alerta "Desvio da rota" tem um cronômetro de redefinição de 10 segundos, o que significa que o evento de alerta não ocorrerá com mais frequência do que uma vez a cada 10 segundos. Se um evento ocorrer enquanto a regra estiver aguardando a redefinição, a plataforma omitirá o evento, inclusive nos relatórios.
- Essa regra é processada na nuvem e não está vinculada a nenhum hardware específico, o que permite que ela seja aplicada a vários rastreadores simultaneamente. Essa flexibilidade permite que você selecione vários rastreadores em uma única regra.