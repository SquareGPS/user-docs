# Cadeado de bloqueio/desbloqueio

## Cadeado de bloqueio/desbloqueioVisão geral

A regra "Locking/Unlocking Padlock" (Bloqueio/Desbloqueio de cadeado) é essencial para as organizações que usam cadeados inteligentes habilitados para GPS para proteger ativos valiosos e áreas críticas. Essa regra monitora o status desses cadeados, garantindo que os usuários sejam notificados instantaneamente sempre que um cadeado for ativado ou desativado.

Especificamente projetada para travas de GPS, essa regra fornece alertas em tempo real para todas as interações de travas, seja protegendo uma área ou trancando a carga em um contêiner.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração de hardware do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Locking/Unlocking Padlock" tem um cronômetro de reinicialização de 1 minuto, o que significa que não será acionado com mais frequência do que uma vez a cada minuto. Os eventos que ocorrerem durante esse período de reinicialização serão omitidos das notificações e dos relatórios.
- **Vários rastreadores:** Essa regra é compatível com vários rastreadores, desde que eles possam detectar eventos de bloqueio/desbloqueio (Padlock) e tenham o recurso integrado à plataforma. Os usuários podem monitorar esses eventos em vários dispositivos de forma eficiente.
- **Processamento independente de GPS:** A plataforma processa e exibe eventos de bloqueio/desbloqueio mesmo que o pacote de dados não tenha coordenadas de GPS válidas. Esses eventos são registrados independentemente de ocorrerem dentro ou fora de uma geocerca, garantindo que nenhum evento crítico seja perdido.