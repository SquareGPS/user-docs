# Tags definidas pelo usuário (Galileosky)

Os dispositivos Galileosky, conhecidos por sua versatilidade e recursos avançados, destacam-se especialmente por seu suporte a tags definidas pelo usuário. A maioria dos dispositivos GPS transmite um conjunto predefinido de dados, incluindo informações essenciais, como coordenadas, altitude, aceleração, quilometragem e detalhes específicos do veículo, como status da ignição e temperatura do líquido de arrefecimento. No entanto, esses dados geralmente são limitados ao que o fabricante suporta, restringindo o monitoramento de parâmetros adicionais.

Com [Dispositivos Galileosky](https://www.navixy.com/devices/galileosky/)Com o Easy Logic, os usuários podem superar essas limitações definindo tags personalizadas, o que permite a transmissão de uma gama mais ampla de dados. Essa flexibilidade permite que os usuários monitorem parâmetros adicionais que normalmente não são suportados pelos dispositivos GPS padrão.

[![Data transfer in Galileosky user tags](https://www.navixy.com/wp-content/uploads/2019/09/configurator_2019-09-28_13-28-39-600x370.png)

](https://www.navixy.com/wp-content/uploads/2019/09/configurator_2019-09-28_13-28-39.png)[![Data transfer in Galileosky user tags](https://www.navixy.com/wp-content/uploads/2019/09/chrome_2019-09-28_13-40-07-600x296.png)

](https://www.navixy.com/wp-content/uploads/2019/09/chrome_2019-09-28_13-40-07.png)

## Benefícios das etiquetas definidas pelo usuário com dispositivos Galileosky

1. **Transmissão de dados personalizada**: Os usuários podem definir parâmetros específicos a serem monitorados e transmitidos, expandindo o escopo para além do conjunto de dados predefinido.
2. **Análise de dados aprimorada**: Ao usar o Easy Logic, os usuários podem realizar operações aritméticas nos dados antes de enviá-los ao servidor. Isso inclui somar, calcular a média ou converter os dados do sensor em percepções mais significativas.
3. **Relatórios de dados condicionais**: Operações lógicas podem ser aplicadas para garantir que os dados sejam transmitidos somente quando condições específicas forem atendidas, otimizando o uso e a relevância dos dados.
4. **Contagem e relatório de eventos**: Os dispositivos Galileosky podem contar eventos específicos e relatá-los em tempo real, fornecendo percepções críticas para aplicativos de gerenciamento de frota ou telemática.
5. **Ações automatizadas**: Os dispositivos podem ser programados para executar ações específicas, como alternar saídas ou acionar alertas, com base nas condições predefinidas, que são então informadas ao servidor.

### Aplicações práticas

Com os dispositivos Galileosky e o Easy Logic, você pode:

- **Operações aritméticas**: Você pode manipular os dados do sensor antes que eles sejam transmitidos ao servidor. Isso inclui somar, calcular a média ou converter as leituras do sensor em formatos que atendam melhor às suas necessidades de análise.
- **Operações lógicas**: Transmitir dados somente quando condições específicas forem atendidas, garantindo que os dados coletados sejam relevantes e usados com eficiência. Isso pode ajudar a otimizar a transmissão de dados e reduzir a carga de dados desnecessária.
- **Contagem de eventos**: Rastreie e conte facilmente eventos específicos com base em critérios predefinidos. Esse recurso é particularmente útil para monitorar processos repetitivos ou cíclicos.
- **Ações automatizadas**: Configure ações, como a comutação de saídas, com base em determinadas condições e faça com que essas ações sejam informadas ao servidor. Essa funcionalidade é ideal para automatizar respostas a entradas de dados em tempo real.

## Como configurar as tags definidas pelo usuário do Galileo com a Navixy

### Configurar dispositivos Galileosky

1. **Instalar o configurador do Galileosky**: Comece fazendo o download e instalando o software Galileosky Configurator.
2. **Configuração no Easy Logic**: Use o Easy Logic para definir as condições e operações necessárias para suas tags personalizadas. Esse processo envolve a criação de scripts no ambiente do Easy Logic para configurar os dados que você deseja monitorar e transmitir.

### Configurar sensores na Navixy

1. Navegue até a seção *Dispositivos e configurações* na plataforma Navixy.
2. Ir para *Sensores e botões* e crie um novo sensor de medição.
3. Selecione a entrada apropriada (User Tag), o tipo de sensor e as unidades.
4. Observe que, no Configurador Galileosky, as tags de usuário são numeradas de 0 a 7, enquanto no Navixy, elas são numeradas de 1 a 8. Portanto, a tag 0 no Configurador corresponde à entrada 1 no Navixy, e assim por diante.

Como em qualquer outro sensor, você pode aplicar configurações adicionais, como calibração, multiplicadores ou limites, para refinar a saída de dados.

Uma vez configuradas, essas tags definidas pelo usuário permitem recursos aprimorados de monitoramento e geração de relatórios, proporcionando aos usuários a capacidade de capturar e analisar dados que vão além das limitações do dispositivo GPS padrão.

4. **Configurar o sensor na Navixy**

- **Ação**:
- Crie um novo sensor de medição.
- Selecione a entrada apropriada (tag de usuário), o tipo de sensor e as unidades de medição.
- Observe a diferença de numeração: as tags de usuário no Galileosky Configurator são numeradas de 0 a 7, enquanto na Navixy são numeradas de 1 a 8. Portanto, a tag 0 no Galileosky corresponde à entrada 1 no Navixy, e assim por diante.
- **Finalidade**: A configuração correta garante que os dados processados pelo Easy Logic da Galileosky sejam corretamente interpretados e exibidos na plataforma Navixy.

5. **Aplicar configurações adicionais do sensor**

- **Ação**: Aprimore a funcionalidade do seu sensor configurando uma tabela de calibração, aplicando multiplicadores para ajustar os valores ou estabelecendo limites para filtrar os valores atípicos.
- **Finalidade**: Essas configurações adicionais ajudam a refinar os dados para garantir que eles sejam tão precisos e úteis quanto possível.

6. **Monitoramento e relatórios na Navixy**

- **Ação**: Use o widget de leituras do sensor no Navixy para monitorar os dados em tempo real. Além disso, você pode gerar relatórios detalhados com base nos dados do sensor, fornecendo informações abrangentes sobre suas operações.
- **Finalidade**: Essa integração permite o monitoramento contínuo e a análise aprofundada dos dados personalizados coletados pelos seus dispositivos Galileosky.