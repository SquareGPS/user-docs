# Botão de chamada pressionado

## Visão geral

A regra "Botão de chamada pressionado" foi projetada para dispositivos GPS equipados com uma função de chamada integrada, normalmente encontrada em dispositivos capazes de fazer chamadas de voz ou comunicação por rádio.

Essa regra aciona as notificações sempre que a função de chamada telefônica do dispositivo é ativada, proporcionando uma maneira rápida de iniciar a comunicação em tempo real. Esse recurso aumenta a segurança, a proteção e a eficiência operacional, garantindo respostas rápidas em situações críticas e contribuindo para operações mais tranquilas.

## Configurações de regras

A funcionalidade dessa regra depende dos recursos e da configuração do dispositivo, portanto, não são necessárias configurações de regras específicas.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Call Button Pressed" (Botão de chamada pressionado) tem um cronômetro de reinicialização de 1 minuto, o que significa que o alerta não será acionado mais de uma vez por minuto. Se ocorrer um evento enquanto a regra estiver aguardando a reinicialização, a plataforma omitirá o evento, inclusive nos relatórios.
- **Vários dispositivos:** Essa regra permite que os usuários selecionem vários rastreadores dos quais desejam receber notificações. Os rastreadores selecionados devem ser compatíveis com o evento "Call Button Pressed" (Botão de chamada pressionado), e esse recurso deve ser integrado à plataforma desses rastreadores. Isso permite que os usuários monitorem eventos em vários dispositivos de forma conveniente.
- **Alerta de evento independente de GPS:** A plataforma reconhece e conta esse tipo de evento de hardware mesmo que o pacote de dados não tenha coordenadas de GPS válidas. O evento será exibido independentemente de ter ocorrido dentro ou fora das cercas geográficas definidas. As configurações de geocerca interna/externa são ignoradas nesse caso, garantindo que nenhum evento crítico seja omitido.