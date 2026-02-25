# Bloqueio de GSM

## Visão geral

O bloqueio de GSM refere-se à interrupção dos sinais GSM (sinais móveis ou celulares) devido à interferência de fontes próximas. Essa interferência, geralmente chamada de mascaramento ou mascaramento de frequência, pode impedir que os dispositivos móveis se conectem a redes móveis, afetando serviços como dados móveis (2G, 3G, 4G, LTE), mensagens de texto e chamadas de voz. No contexto do rastreamento por GPS, o bloqueio de GSM pode levar à perda da comunicação de dados em tempo real, o que torna crucial a implementação de regras de detecção.

Por exemplo, uma empresa de logística que usa veículos equipados com GPS para transportar cargas valiosas depende de sinais GSM para rastreamento de localização em tempo real. Se houver interferência de GSM, esses sinais serão interrompidos, o que pode comprometer a segurança das remessas. Ao implementar regras para detectar interferência de GSM, a empresa pode receber alertas imediatos, permitindo uma ação rápida para proteger seus ativos.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração de hardware do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "GSM jamming" tem um cronômetro de reinicialização de 5 minutos, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada 5 minutos. Se ocorrer um evento durante o período de reinicialização, ele será omitido pela plataforma e não será incluído nos relatórios.
- **Vários dispositivos:** Os usuários podem selecionar vários rastreadores para monitorar de acordo com essa regra. O único requisito é que os rastreadores selecionados sejam compatíveis com eventos de interferência GSM e estejam integrados à plataforma. Essa flexibilidade permite que os usuários monitorem esse tipo de evento em vários veículos ou dispositivos de forma conveniente.
- **Alerta de evento independente de GPS:** A plataforma registrará e exibirá o evento mesmo que ele seja recebido em uma mensagem sem coordenadas de GPS válidas. Isso garante que os usuários sejam informados sobre o evento, independentemente dos dados de localização. As configurações do botão de rádio Inside/Outside para cercas geográficas são ignoradas nesses casos, pois a plataforma prioriza a exibição de eventos potencialmente críticos.

## Veja também

- [Bloqueio de GPS](../posicionamento-do-dispositivo/bloqueio-de-gps.md)