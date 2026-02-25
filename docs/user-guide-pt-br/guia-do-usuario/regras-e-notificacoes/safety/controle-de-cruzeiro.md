# Controle de cruzeiro

## Visão geral

O recebimento de notificações quando o Cruise Control é ativado ou desativado em um veículo fornece informações valiosas para monitorar e gerenciar o desempenho do veículo. Aqui estão alguns dos principais benefícios:

- **Monitoramento da eficiência do combustível:** O Cruise Control ajuda a manter uma velocidade consistente, o que pode melhorar a eficiência do combustível. As notificações permitem que os usuários acompanhem o uso do Cruise Control e avaliem seu impacto no consumo de combustível.
- **Gerenciamento de bateria:** Para veículos elétricos ou híbridos, o uso do Cruise Control pode afetar a vida útil e a autonomia da bateria. As notificações ajudam os usuários a monitorar seu impacto no uso da bateria, permitindo um melhor gerenciamento da energia elétrica do veículo.
- **Análise do comportamento ao dirigir:** O rastreamento de quando e onde o Cruise Control é usado oferece informações sobre o comportamento do motorista. Esses dados podem ser usados para analisar os hábitos de direção e identificar oportunidades de melhoria, como a redução do uso excessivo ou o aumento do uso subutilizado do Cruise Control.
- **Avaliação de desempenho:** O monitoramento do uso do Cruise Control pode ajudar a avaliar o desempenho do veículo. Os usuários podem comparar o Cruise Control com outros modos de direção para avaliar a eficiência em diferentes rotas e condições de direção.
- **Segurança e conforto:** O Cruise Control aumenta o conforto e a segurança durante viagens longas. As notificações garantem que os usuários saibam se o Cruise Control está ativo, permitindo que eles ajustem seu estilo de direção conforme necessário.

Esses benefícios podem variar de acordo com a marca, o modelo e os recursos adicionais do veículo.

## Configurações de regras

Essa regra não exige nenhuma configuração específica.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Cruise Control Switched ON/OFF" (Controle de cruzeiro ligado/desligado) tem um Temporizador de reinicialização de 10 minutosimpedindo que o alerta seja acionado mais de uma vez a cada 10 minutos. Se outro evento ocorrer dentro desse período de reinicialização, ele será omitido da plataforma e dos relatórios.
- **Vários dispositivos:** Os usuários podem selecionar vários rastreadores para receber notificações. Os rastreadores selecionados devem ser compatíveis com os eventos Cruise Control Switched ON/OFF e ter esse recurso integrado à plataforma. Isso permite o monitoramento de eventos do Cruise Control em vários veículos.
- **Alerta de evento independente de GPS:** A plataforma registra e exibe eventos do Cruise Control mesmo que o pacote de dados não tenha coordenadas de GPS válidas. As configurações de geocerca interna/externa são ignoradas para essa regra, garantindo que eventos críticos não sejam perdidos.