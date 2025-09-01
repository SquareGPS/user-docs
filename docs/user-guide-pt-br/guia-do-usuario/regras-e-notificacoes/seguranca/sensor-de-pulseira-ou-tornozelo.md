# Sensor de pulseira (ou tornozelo)

A regra do "sensor de pulseira" (ou "sensor de tornozelo") foi projetada especificamente para aplicações de monitoramento legal que envolvem rastreadores GPS especializados. É uma ferramenta essencial para a segurança em contextos como prisão domiciliar ou liberdade condicional.

Essa regra foi criada para notificar imediatamente a equipe de segurança se um dispositivo GPS for removido sem autorização. Nessas situações, a regra aciona um alerta instantâneo para as autoridades relevantes, permitindo uma ação rápida para evitar qualquer movimento não autorizado ou violação das condições legais.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração de hardware do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro.** O alerta "Sensor de pulseira" tem um cronômetro de redefinição de 3 minutos, o que significa que o evento de alerta não ocorrerá com mais frequência do que uma vez a cada 3 minutos. Se esse tipo de evento ocorrer durante o tempo em que a regra estiver aguardando a redefinição, esse evento será omitido pela plataforma, incluindo os relatórios.
- **Vários dispositivos:** Com essa regra, você tem a flexibilidade de selecionar vários rastreadores para receber notificações. O único requisito é que os rastreadores selecionados sejam compatíveis com os eventos do sensor da pulseira e tenham esse recurso integrado à plataforma. Isso permite que você monitore vários rastreadores compatíveis simultaneamente, garantindo o recebimento eficiente de notificações para os eventos relevantes em vários veículos ou dispositivos.
- **Alerta de evento independente de GPS:** Quando a plataforma detecta esse tipo de evento de hardware a partir de dados do rastreador que não possuem coordenadas válidas, ela ainda registrará e exibirá o evento como válido. Isso se aplica independentemente de o evento ter ocorrido dentro ou fora das cercas geográficas designadas. Nesses casos, a plataforma desconsidera a lógica de geocerca interna/externa para garantir que o evento seja capturado e relatado.