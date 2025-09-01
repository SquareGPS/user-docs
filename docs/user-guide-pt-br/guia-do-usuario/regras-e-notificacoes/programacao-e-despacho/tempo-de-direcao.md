# Tempo de direção

## Visão geral

A regra de tempo de direção foi projetada para monitorar e aplicar práticas de direção segura, rastreando os períodos de trabalho e descanso dos motoristas. Essa regra garante que os motoristas cumpram as normas de tempo de direção, ajudando a evitar incidentes relacionados à fadiga e a promover a segurança geral nas estradas.

Quando um motorista excede o tempo de direção contínua permitido, o sistema gera uma notificação para alertar o usuário. A regra é redefinida automaticamente quando o motorista descansa por um período especificado, que pode ser configurado de acordo com suas necessidades.

## Configurações de regras

#### **Tempo de direção permitido**

Essa configuração define a duração máxima que um motorista pode dirigir continuamente antes que uma notificação seja acionada. Quando esse limite for atingido, o sistema o alertará para que tome as medidas necessárias.

#### Tempo mínimo de estacionamento para reinicialização

Essa configuração especifica a duração mínima de estacionamento necessária para redefinir a regra de tempo de direção. O temporizador de redefinição começa somente quando o dispositivo detecta que o veículo entrou em um estado de estacionamento.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- A regra de tempo de direção funciona rastreando o tempo total que o motorista passa dirigindo continuamente. Quando o tempo máximo permitido de direção é excedido, o sistema gera um alerta.
- A regra é redefinida após o veículo ter sido estacionado pelo período mínimo especificado nas configurações, permitindo que o motorista inicie um novo período de condução.
- Essa regra é processada na nuvem, o que permite que ela seja aplicada em vários rastreadores simultaneamente. Essa flexibilidade permite que você monitore vários drivers em uma única configuração de regra.
- O sistema ajuda a garantir a conformidade com as normas de direção, reduz a fadiga do motorista e promove práticas de direção mais seguras, contribuindo para a segurança e a eficiência geral da frota.