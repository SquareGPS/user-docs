# Sensor de vibração

## Visão geral

Um sensor de vibração, também conhecido como sensor de vibração, depende do acelerômetro integrado de um dispositivo para detectar vibração ou movimento contínuo, normalmente quando um veículo está estacionado. Essa regra é projetada para acionar alertas ou notificações quando vibrações incomuns ou contínuas são detectadas, sinalizando possíveis atividades não autorizadas ou perturbações. As configurações de sensibilidade do sensor podem ser ajustadas de acordo com as necessidades do usuário, dependendo da configuração do dispositivo.

Essa regra é particularmente útil em várias aplicações, como em empresas de construção que protegem seus veículos estacionados. Vibrações contínuas podem indicar acesso não autorizado ou tentativa de roubo. Os alertas gerados por essa regra permitem que as empresas respondam prontamente, reduzindo o risco de roubo de veículos, minimizando os possíveis danos e limitando as perdas.

É importante observar que a eficácia dessa regra depende do hardware e da configuração do rastreador GPS. Todos os cenários relacionados à detecção de vibração devem ser configurados no ambiente do rastreador. Por exemplo, alguns rastreadores oferecem opções de configuração, como status de ignição ou tempo limite de movimento.

## Configurações de regras

Essa regra depende totalmente dos recursos e da configuração de hardware do dispositivo. Não há configurações específicas a serem definidas na própria regra.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Sensor de vibração" tem um cronômetro de redefinição de 1 minuto, o que significa que o alerta não será acionado mais de uma vez a cada minuto. Se ocorrer um evento enquanto a regra estiver aguardando a redefinição, a plataforma omitirá o evento, inclusive nos relatórios.
- **Vários dispositivos:** Os usuários podem selecionar vários rastreadores para receber notificações dessa regra, desde que os rastreadores suportem eventos do sensor de vibração e o recurso esteja integrado à plataforma.
- **Alerta de evento independente de GPS:** Se a plataforma receber um evento de vibração de um rastreador sem coordenadas de GPS válidas, o evento ainda será contado como válido e exibido, independentemente de ter ocorrido dentro ou fora de uma geocerca. A lógica dos botões de rádio Inside/Outside é ignorada nesse caso, pois é melhor mostrar um evento potencialmente crítico do que omiti-lo.