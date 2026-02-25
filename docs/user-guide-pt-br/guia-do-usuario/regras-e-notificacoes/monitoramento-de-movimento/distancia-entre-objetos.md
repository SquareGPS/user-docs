# Distância entre objetos

## Visão geral

A regra "Distância entre objetos" foi criada para ajudá-lo a gerenciar e monitorar com eficiência a distância entre vários ativos, como entre dois veículos, um veículo e sua carga ou um caminhão e seus reboques.

Essa regra permite que você defina limites de distância específicos entre os objetos rastreados. Se a distância exceder ou ficar abaixo dos limites definidos, um evento será acionado, registrado e poderá gerar uma notificação.

### Como funciona

Essa regra aproveita os dados de GPS para rastrear continuamente a distância entre um objeto primário designado, como um veículo líder, e até 100 objetos secundários, como reboques ou veículos que o seguem. Ao definir parâmetros de distância específicos, os usuários podem receber notificações em tempo real quando esses objetos se aproximam ou se afastam mais do que o permitido. O sistema calcula automaticamente as distâncias com base nas coordenadas de GPS mais recentes, garantindo alertas precisos e oportunos.

### Aplicativos

- **Rastreamento de reboques e ativos:** Mantenha o controle sobre a distância entre um veículo e seus ativos anexados ou seguintes, como reboques. Isso é essencial para evitar a desconexão acidental, gerenciar o espaçamento do comboio e garantir que os reboques permaneçam dentro de uma faixa operacional segura.
- **Aplicação da distância segura de seguimento:** Monitore e imponha distâncias seguras de acompanhamento entre os veículos da frota. Esse aplicativo é fundamental para evitar colisões e promover a adesão aos protocolos de segurança, principalmente em ambientes de tráfego intenso ou na operação de veículos pesados.
- **Coordenação da frota e gerenciamento de tráfego:** Use a regra para gerenciar o espaçamento dos veículos em um comboio ou para monitorar as posições relativas de vários ativos da frota durante as operações. Esses dados também podem ser agregados para análise de tráfego, ajudando a identificar padrões de congestionamento e a otimizar o planejamento de rotas.

## Configurações de regras

### Parâmetros de distância

- **Aproximação:** Configure o sistema para alertá-lo quando objetos secundários estiverem se aproximando do veículo principal. Essa configuração é fundamental para manter distâncias operacionais seguras e evitar colisões ou outros riscos à segurança.
- **Moving Away:** Defina alertas para quando objetos secundários estiverem aumentando sua distância do veículo principal. Isso é particularmente útil para detectar quando os veículos estão se afastando de um comboio ou quando os reboques estão se separando do veículo principal.
- **Faixa de distância:** Defina uma faixa de distância específica permitida entre os objetos primário e secundário, variando de 5 a 200.000 metros. O sistema gerará notificações sempre que a distância estiver dentro ou fora desse intervalo predefinido, permitindo o gerenciamento proativo das operações da frota.

![image-20240813-221847.png](attachments/image-20240813-221847.png)

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

### Detalhes da operação do sistema

- **Cálculo de distância baseado em GPS:** A regra calcula as distâncias com base nas últimas coordenadas de GPS disponíveis, garantindo a precisão no monitoramento da proximidade do objeto.
- **Reiniciar o cronômetro:** O alerta "Distance between objects" (Distância entre objetos) apresenta um cronômetro de reinicialização de 10 segundos, o que significa que os alertas não serão acionados com mais frequência do que uma vez a cada 10 segundos. Isso ajuda a evitar notificações redundantes e garante que os alertas sejam significativos e acionáveis.
- **Vários dispositivos:** Essa regra é independente de hardware e pode ser aplicada a vários rastreadores simultaneamente, oferecendo flexibilidade no gerenciamento de grandes frotas com diversos ativos.