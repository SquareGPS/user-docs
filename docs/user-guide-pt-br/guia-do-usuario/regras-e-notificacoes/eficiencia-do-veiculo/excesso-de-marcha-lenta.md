# Excesso de marcha lenta

## Visão geral

A marcha lenta excessiva é um evento importante a ser monitorado no gerenciamento de frotas, pois afeta diretamente o consumo de combustível, o desgaste do veículo e a eficiência operacional geral. A Navixy oferece dois métodos para detectar a marcha lenta excessiva: relacionado ao hardware e relacionado à plataforma. Cada método tem suas próprias vantagens e é adequado a diferentes tipos de necessidades da frota.

**A regra relacionada à plataforma** é gerenciado pela plataforma e usa parâmetros definidos pelo usuário, como duração da marcha lenta e detecção de estacionamento. Essa regra é ideal para quem precisa de uma solução flexível e personalizável que funcione com qualquer rastreador que informe dados básicos, como estado da ignição e localização por GPS.

**A regra relacionada ao hardware,** por outro lado, conta com o recurso integrado do rastreador GPS para detectar eventos de inatividade. O hardware gera e transmite o evento de marcha lenta diretamente para a plataforma. Esse método é vantajoso para rastreadores que têm recursos avançados de detecção de marcha lenta, oferecendo uma precisão potencialmente maior e funcionalidade adicional.

## Configurações de regras

### Relacionado à plataforma

- **Duração da marcha lenta:** Defina a duração após a qual a marcha lenta será considerada excessiva. A regra monitorará quando um veículo estiver estacionado (conforme determinado pelas configurações de Detecção de estacionamento) e a ignição estiver LIGADA. Se o veículo permanecer nesse estado além da duração especificada, uma notificação será acionada.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

### Relacionado a hardware

- **Configurações específicas do dispositivo:** Essa regra depende da configuração do hardware para detectar a marcha lenta. Você deve consultar a documentação do dispositivo para configurar a detecção de marcha lenta no rastreador. A plataforma receberá e exibirá eventos de marcha lenta com base na saída do dispositivo.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Detecção de ociosidade relacionada à plataforma:** A plataforma monitora continuamente o estado da ignição do veículo e o status do estacionamento. Quando o veículo está estacionado com a ignição LIGADA, a plataforma começa a contar a duração da marcha lenta. Se a marcha lenta exceder o limite definido pelo usuário, o sistema enviará um alerta. Esse método funciona com uma ampla gama de rastreadores e oferece flexibilidade na definição de limites de marcha lenta personalizados.
- **Detecção de ociosidade relacionada ao hardware:** O próprio rastreador monitora a marcha lenta e envia um evento para a plataforma quando a marcha lenta excede o limite predefinido definido no dispositivo. A plataforma simplesmente encaminha esse evento para o usuário. Esse método pode oferecer maior precisão e recursos avançados, dependendo dos recursos do rastreador.
- **Notificações:** Independentemente do método de detecção, você receberá notificações por meio da interface do usuário, e-mail ou SMS. Essas notificações ajudam os gerentes de frota a tomar medidas imediatas para reduzir a ociosidade desnecessária, economizando combustível e reduzindo o desgaste dos veículos.
- **Relatórios:** Você pode gerar relatórios sobre a marcha lenta excessiva para analisar padrões e tomar decisões baseadas em dados para melhorar a eficiência da frota. Esses relatórios podem ser particularmente úteis para identificar a marcha lenta habitual ou avaliar o impacto da marcha lenta nos custos de combustível e na manutenção do veículo.