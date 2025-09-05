# Mudança de status de trabalho

## Visão geral

A regra "Work status change" foi criada para monitorar e rastrear as atividades em tempo real dos funcionários móveis que usam o aplicativo X-GPS Tracker. Essa regra alerta sobre a atualização do status atual dos funcionários, indicando, por exemplo, quando eles estão disponíveis para uma nova tarefa ou quando iniciaram uma nova atividade.

Quando a regra "Work status" estiver ativa, qualquer alteração no status de um funcionário acionará notificações imediatas por SMS, e-mail ou alertas pop-up na interface do usuário. Essa funcionalidade garante que os supervisores e despachantes permaneçam informados sobre as atividades atuais e a disponibilidade de sua equipe, permitindo uma melhor coordenação e gerenciamento de tarefas.

## Configurações de regras

#### Status de trabalho

Defina os status de trabalho específicos que acionarão as notificações quando selecionados pelos funcionários. Os usuários podem escolher quais status monitorar, garantindo que o sistema alerte apenas sobre as atualizações de status mais relevantes. Esses status são criados e atribuídos por meio do widget "Working statuses" (Status de trabalho) no menu Devices and Settings (Dispositivos e configurações).

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- Essa regra foi projetada especificamente para uso com dispositivos habilitados para o X-GPS Tracker, o que significa que somente esses dispositivos podem ser selecionados como fontes para monitorar as alterações de status do trabalho.
- A lista de status de trabalho que aciona essa regra pode variar dependendo das listas personalizadas atribuídas a diferentes rastreadores. Se você modificar a lista de dispositivos vinculados à regra e isso alterar a lista de status de trabalho associados, a regra incluirá os status antigos e os novos. Entretanto, os status recém-adicionados da lista atualizada não serão selecionados por padrão. Você pode editar a regra para incluir esses novos status.
- Ao contrário de muitas outras regras, a regra "Status de trabalho" não tem um cronômetro de reinicialização, o que permite a notificação imediata de qualquer alteração de status.

Essa configuração ajuda as organizações a manter uma comunicação clara e um gerenciamento de tarefas eficaz, mantendo a equipe atualizada sobre o status atual do trabalho de cada membro.