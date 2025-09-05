# Mudança de motorista

## Visão geral

A regra "Mudança de motorista" ajuda os gerentes de frota a rastrear qual motorista está operando um veículo, especialmente quando vários motoristas compartilham o mesmo veículo. Esse recurso funciona com tecnologias de identificação de motoristas, como iButton, leitores RFID ou chaves de hardware BLE.

## Configurações de regras

Para usar essa regra, comece adicionando todos os seus drivers à pasta **Gerenciamento de frotas** → **Seção de motoristas**. Atribua a cada motorista uma chave de hardware exclusiva, como um iButton ou uma etiqueta RFID. Quando uma mudança de motorista é detectada, a plataforma associa o evento ao motorista correto, garantindo relatórios e alertas precisos.

Não são necessárias outras configurações específicas do Rule. Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Detecção de mudança de motorista:** A plataforma identifica uma alteração de driver verificando se os dados mais recentes da chave de hardware recebidos do rastreador são diferentes dos dados anteriores. Se a chave tiver sido alterada, ela registrará isso como um evento de alteração de driver. Isso difere do [Identificação do motorista](identificacao-do-motorista.md) em que o alerta é acionado diretamente pelo hardware após a autenticação bem-sucedida do driver, e a plataforma simplesmente exibe o evento.
- **Substituições manuais:** As alterações manuais de driver feitas por meio da interface do usuário (ou seja, em widgets) não acionam um evento de alteração de driver. Essas alterações também não são incluídas no "Relatório de todos os eventos". No entanto, todas as mudanças manuais e automáticas de motoristas podem ser revisadas em detalhes por meio do relatório "Driver shift change" (Mudança de turno do motorista).
- **Temporizador de redefinição de alerta:** O alerta de "Troca de motorista" tem um cronômetro de reinicialização de 10 segundos, impedindo que ele seja acionado mais de uma vez a cada 10 segundos. Se ocorrer um evento de mudança de motorista durante esse período, a plataforma suprimirá o alerta, mantendo as notificações e os relatórios precisos e concisos.
- **Suporte para vários dispositivos:** Essa regra pode ser aplicada a vários rastreadores, permitindo que os gerentes de frota monitorem as mudanças de motorista em vários veículos. Os rastreadores devem ser compatíveis com o evento de mudança de motorista e ter esse recurso integrado à plataforma.
- **Processamento de eventos independente de GPS:** A plataforma processa eventos de mudança de motorista mesmo que os dados de GPS estejam ausentes ou sejam inválidos. Esses eventos ainda serão registrados e exibidos, independentemente de terem ocorrido dentro ou fora de uma delimitação geográfica. Isso garante que todos os eventos críticos de mudança de motorista sejam capturados e relatados com precisão.

## Veja também

- [**Regra de identificação do motorista**](identificacao-do-motorista.md) - a regra usada para verificar e autorizar o motorista antes ou durante a operação do veículo, fornecendo alertas imediatos e garantindo que somente motoristas autorizados possam operar o veículo.