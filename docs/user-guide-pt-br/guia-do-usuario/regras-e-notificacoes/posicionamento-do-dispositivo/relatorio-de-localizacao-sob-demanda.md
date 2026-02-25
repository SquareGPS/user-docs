# Relatório de localização sob demanda

## Visão geral

O **Relatório de localização sob demanda via SMS** permite que os usuários solicitem manualmente a localização atual de um dispositivo GPS enviando um comando SMS. Esse recurso é particularmente útil em situações em que o dispositivo não consegue estabelecer uma conexão celular com a plataforma por IP, como quando está em uma área de roaming com cobertura de dados limitada ou inexistente.

Quando o dispositivo não consegue transmitir seus dados de localização por meio dos canais usuais (como redes GPRS ou 3G/4G), o **Atualização de localização sob demanda via SMS** oferece uma alternativa confiável. Ao enviar um comando SMS da plataforma para o dispositivo, os usuários ainda podem recuperar a posição do dispositivo. O dispositivo responde com suas coordenadas de GPS via SMS para a plataforma, garantindo o rastreamento da localização mesmo quando as conexões de dados padrão não estão disponíveis.

Para aumentar ainda mais a conveniência, a Navixy oferece um **Atualização de localização via regra de SMS**. Essa regra notifica os usuários assim que uma atualização de localização GPS é recebida via SMS. Como as atualizações de localização baseadas em SMS podem levar de minutos a horas, dependendo da disponibilidade da rede e do status do dispositivo, essa regra garante que os usuários sejam alertados imediatamente quando a atualização ocorrer. Esse recurso de notificação simplifica o processo, permitindo que os usuários se concentrem em outras tarefas sem a necessidade de verificar manualmente a chegada da atualização.

## Configurações de regras

Não há configurações de regras específicas. Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro.** O alerta "Location report on demand" (Relatório de localização sob demanda) tem um cronômetro de redefinição de 1 minuto, o que significa que o evento de alerta não ocorrerá com mais frequência do que uma vez a cada 1 minuto. Se esse tipo de evento ocorrer durante o tempo em que a regra estiver aguardando a redefinição, esse evento será omitido pela plataforma, inclusive os relatórios.
- **Vários dispositivos.** Nesse tipo de regra, os usuários têm a flexibilidade de selecionar vários rastreadores dos quais desejam receber notificações. O único requisito é que os rastreadores selecionados sejam compatíveis com os eventos de relatório de localização sob demanda e que o recurso seja integrado à plataforma de determinados rastreadores. Isso significa que os usuários podem escolher vários rastreadores compatíveis para receber notificações, o que lhes permite monitorar eventos de direção severa em vários veículos ou dispositivos de forma conveniente.