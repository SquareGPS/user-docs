# Alteração do nível de combustível

## Visão geral

O monitoramento dos níveis de combustível é fundamental para gerenciar o consumo de combustível e detectar o uso não autorizado. A regra de alteração do nível de combustível foi projetada para fornecer notificações em tempo real sempre que ocorrerem alterações significativas nos níveis de combustível, como aumentos ou reduções repentinas.

Essas notificações podem ser entregues por meio da interface de usuário da Web, SMS ou e-mail, e podem ser consolidadas em relatórios. Esse monitoramento proativo ajuda os usuários a responder rapidamente às mudanças no nível de combustível, reduzindo potencialmente os custos de combustível e resolvendo disputas entre os funcionários.

> [!INFO]
> Antes de configurar essa regra, certifique-se de que o sensor de nível de combustível que você pretende monitorar esteja configurado corretamente. Para obter instruções detalhadas sobre a instalação e a configuração de sensores de nível de combustível, consulte a seção [Seção do sensor de nível de combustível](../../dispositivos-e-configuracoes/sensores-de-veiculos/measurement-sensors/fuel-level-sensor.md).

## Configurações de regras

#### Sensor

Especifique o sensor de nível de combustível que será usado como fonte para notificações e análises. O número de alterações de combustível indicadas é regulado pelo parâmetro Precisão do sensor de nível de combustível, que é explicado na seção [Seção do sensor de nível de combustível](../../dispositivos-e-configuracoes/sensores-de-veiculos/measurement-sensors/fuel-level-sensor.md).

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- A plataforma suaviza os dados do sensor e compara a alteração total em uma janela de 10 minutos com a configuração de precisão do sensor de combustível para determinar se uma notificação deve ser acionada. Por exemplo, com uma configuração de Precisão de 5%, uma alteração no nível de combustível de 5 litros ou mais em um tanque de 100 litros em um período de 10 minutos acionará um alerta. Se a alteração cumulativa atingir ou exceder esse limite, a plataforma enviará uma notificação.
- A estimativa de volume de mudança de combustível não está incluída atualmente nas notificações, mas estará disponível em breve.
- O alerta "Mudança de nível de combustível" tem um cronômetro de reinicialização de 15 minutos, o que significa que o alerta não será acionado mais do que uma vez a cada 15 minutos. Se ocorrer uma alteração no nível de combustível enquanto a regra estiver em seu período de reinicialização, a plataforma omitirá o evento, inclusive nos relatórios.
- Essa regra é compatível com apenas um dispositivo por regra. Essa limitação se deve às complexidades envolvidas na referência cruzada de vários sensores de medição com diferentes rastreadores, tabelas de calibração e outros aspectos de medição e filtragem.