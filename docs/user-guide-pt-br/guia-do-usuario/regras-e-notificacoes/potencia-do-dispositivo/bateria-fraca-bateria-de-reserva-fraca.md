# Bateria fraca (bateria de reserva fraca)

## Visão geral

Um dispositivo GPS informa um alerta de bateria fraca quando o nível de carga de sua bateria interna cai abaixo de um limite predeterminado. Esse alerta é acionado para notificar os usuários de que a energia do dispositivo está acabando, indicando que a bateria precisa ser recarregada ou substituída em breve.

No caso de rastreadores portáteis, esse alerta indica que a fonte de alimentação primária está se esgotando, enquanto que, no caso de rastreadores montados em veículos, pode indicar que a bateria de reserva está acabando, o que pode comprometer a capacidade do dispositivo de continuar rastreando se a fonte de alimentação principal for perdida.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Função das baterias internas em dispositivos GPS

Uma bateria interna em um dispositivo GPS é uma fonte de energia integrada que desempenha um papel crucial na funcionalidade do dispositivo. Dependendo da finalidade do rastreador GPS, essa bateria interna pode ter diferentes funções.

- **Em rastreadores GPS portáteis,** a bateria interna é normalmente a principal fonte de energia. Essas baterias são essenciais para rastrear ativos, pessoas ou veículos em cenários em que a energia externa pode não estar disponível.
- **Para rastreadores GPS montados em veículos,** A bateria interna geralmente funciona como uma fonte de energia de reserva. Essa bateria de reserva entra em ação quando a fonte de alimentação principal do veículo é interrompida, seja por desconexão, adulteração ou falha da bateria do veículo. A bateria de reserva garante o rastreamento e a transmissão de dados contínuos, proporcionando uma camada extra de segurança e confiabilidade, especialmente em aplicações críticas de gerenciamento de frota ou antifurto.

## Duas regras de monitoramento de bateria

Na Navixy, há duas regras distintas criadas para monitorar o status da bateria dos seus dispositivos GPS: a regra "Bateria fraca" e a regra "Bateria de reserva fraca".

- **A regra da "bateria fraca** aplica-se à fonte de energia primária do dispositivo, normalmente usada em rastreadores portáteis ou dispositivos que dependem exclusivamente de baterias internas.
- **A regra "Bateria de reserva fraca** monitora especificamente o nível de carga das baterias secundárias ou de reserva, que são comumente encontradas em rastreadores montados em veículos.

Essas regras são baseadas em hardware, o que significa que o próprio dispositivo ou sua configuração determina o limite de disparo para o alerta de bateria fraca. Quando a carga da bateria cai abaixo desse limite, o dispositivo informa o fato e o sistema envia uma notificação, permitindo que os usuários tomem medidas proativas para recarregar o dispositivo e evitar o tempo de inatividade.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração de hardware do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Especificidades da plataforma

Os alertas "Bateria fraca" e "Bateria de reserva fraca" compartilham várias semelhanças operacionais, mas há uma diferença em seus temporizadores de reinicialização.

- **Reiniciar temporizadores**: O alerta "Backup battery low" (Bateria de reserva fraca) tem um cronômetro de reinicialização de 1 minuto, o que significa que o alerta não será acionado com mais frequência do que uma vez por minuto. Por outro lado, o alerta "Bateria fraca" tem um cronômetro de reinicialização mais longo, de 30 minutos, de modo que não será acionado com mais frequência do que uma vez a cada 30 minutos. Se um evento ocorrer durante o período de reinicialização de qualquer uma das regras, ele será omitido da plataforma, inclusive dos relatórios.
- **Seleção do rastreador**: Ambas as regras permitem que os usuários monitorem vários rastreadores, desde que os rastreadores suportem os respectivos eventos e o recurso esteja integrado na plataforma. Esse recurso permite o monitoramento eficiente dos níveis de bateria em vários veículos ou dispositivos.
- **Registro do evento**: Para ambas as regras, a plataforma registrará e exibirá o evento mesmo que ele seja recebido em um pacote sem coordenadas válidas. Isso garante que os usuários sejam informados sobre o evento independentemente de sua localização, mantendo uma supervisão consistente de seus ativos.