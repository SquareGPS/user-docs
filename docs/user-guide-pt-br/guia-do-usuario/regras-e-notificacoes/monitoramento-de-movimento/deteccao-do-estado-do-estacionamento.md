# Detecção do estado do estacionamento

## Visão geral

Essa regra permite que os usuários recebam notificações quando um dispositivo inicia ou termina o estacionamento. Por exemplo, as organizações que desejam controlar o tempo de condução de seus veículos podem usar essa regra para garantir que os veículos não sejam usados fora do expediente. Essa regra fornece notificações à interface do usuário, ao endereço de e-mail ou ao número de telefone sobre os estados de estacionamento dos objetos selecionados.

A configuração dessa regra ajuda os usuários a se manterem informados sobre o início e o fim das viagens, bem como sobre as alterações no status de estacionamento de seus veículos. Isso aumenta o controle, a segurança e a eficiência das operações de gerenciamento de frota.

## Configurações de regras

**Configurações de detecção de estacionamento**

As configurações de uma regra de detecção de estacionamento são gerenciadas exclusivamente no widget Detecção de estacionamento. Para obter informações detalhadas sobre a configuração da detecção de estacionamento, consulte o artigo sobre Detecção de estacionamento.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- O alerta "Detecção de estado de estacionamento" tem um cronômetro de reinicialização de 10 segundos, o que significa que o evento de alerta não ocorrerá com mais frequência do que uma vez a cada 10 segundos. Se um evento ocorrer enquanto a regra estiver aguardando a redefinição, a plataforma omitirá o evento, inclusive nos relatórios.
- Essa regra é detectada no lado do servidor e não está vinculada a nenhum hardware específico, o que permite que ela seja aplicada a vários rastreadores simultaneamente. Essa flexibilidade permite que você gerencie vários rastreadores em uma única regra.