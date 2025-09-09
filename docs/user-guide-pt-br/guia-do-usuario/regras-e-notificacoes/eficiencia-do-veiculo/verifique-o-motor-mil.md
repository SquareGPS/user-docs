# Verifique o motor (MIL)

## Visão geral

A regra "Check engine (MIL)" foi criada para monitorar o status da lâmpada indicadora de mau funcionamento (MIL), comumente conhecida como luz "Check Engine", nos veículos. Essa regra é crucial para a manutenção de veículos e o gerenciamento de frotas, pois alerta prontamente os usuários quando a MIL é ativada.

Normalmente, a MIL se acende quando o sistema de diagnóstico a bordo do veículo detecta um problema no motor, nas emissões ou em outros sistemas críticos. Ao receber notificações oportunas, os usuários podem tomar medidas imediatas para resolver possíveis problemas, evitando danos maiores e garantindo a segurança e a conformidade do veículo.

> [!INFO]
> Para monitorar códigos DTC específicos, você pode configurar um [Valor do campo de estado](../entradas-e-saidas/valor-do-campo-de-estado.md) regra.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro.** O alerta "Verificar motor (MIL)" tem um cronômetro de reinicialização de 24 horas, o que significa que ele não será acionado com mais frequência do que uma vez a cada 24 horas. Se o evento ocorrer durante o período de reinicialização, ele será omitido da plataforma e dos relatórios.
- **Vários dispositivos.** Essa regra pode ser aplicada a vários dispositivos GPS, desde que eles suportem o evento Check Engine (MIL) e tenham o recurso integrado à plataforma.
- **Alerta de evento independente de GPS.** A plataforma registrará o evento e acionará notificações, independentemente de o veículo estar dentro ou fora de uma cerca geográfica, mesmo que o pacote de dados não tenha coordenadas de GPS válidas. A plataforma prioriza a captura e a exibição desses eventos críticos para garantir que eles não sejam perdidos.