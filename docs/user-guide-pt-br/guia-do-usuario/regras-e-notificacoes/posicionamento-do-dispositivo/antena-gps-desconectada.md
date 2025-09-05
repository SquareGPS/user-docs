# Antena GPS desconectada

## Visão geral

A regra "antena GPS desconectada" foi criada para dispositivos GPS que utilizam uma antena externa, normalmente conectada por meio de um cabo e um soquete. Quando a antena é desconectada (ou cortada), ela pode interromper a recepção do sinal de satélite, levando a possíveis problemas de rastreamento. Essa regra o alerta imediatamente quando essa desconexão ocorre, permitindo que você resolva rapidamente o problema e mantenha o rastreamento contínuo dos seus ativos.

Por exemplo, se você gerencia uma frota de veículos de entrega equipados com rastreadores e antenas externas de GPS, essa regra o ajuda a monitorar a integridade das conexões de GPS. Se uma antena for desconectada devido a fatores ambientais ou adulteração, você será imediatamente notificado. Isso permite que você tome medidas corretivas, como o envio de um técnico para restaurar a conexão, evitando possíveis atrasos e mantendo a eficiência das operações.

> [!INFO]
> A maioria dos dispositivos GPS modernos vem equipada com antenas integradas de alta sensibilidade, tornando obsoletas as antenas externas.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração de hardware do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "antena GPS desconectada" tem um cronômetro de reinicialização de 5 minutos, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada 5 minutos. Se ocorrer um evento durante o período de reinicialização, ele será omitido pela plataforma e não será incluído nos relatórios.
- **Vários dispositivos:** É possível monitorar vários rastreadores com essa regra, desde que os rastreadores selecionados suportem eventos de desconexão da antena GPS e que o recurso esteja integrado à plataforma. Isso permite um monitoramento abrangente de vários veículos ou dispositivos.
- **Tratamento de eventos sem coordenadas:** A plataforma registrará e exibirá o evento mesmo que ele seja recebido em um pacote sem coordenadas de GPS válidas. Isso garante que você seja informado sobre o evento de desconexão, independentemente dos dados de localização. As configurações do botão de rádio Inside/Outside para geofences são ignoradas nesses casos, priorizando a exibição de eventos potencialmente críticos.