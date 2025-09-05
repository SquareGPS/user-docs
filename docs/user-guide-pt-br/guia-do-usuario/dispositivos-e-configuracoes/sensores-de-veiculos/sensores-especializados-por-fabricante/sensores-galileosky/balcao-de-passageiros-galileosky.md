# Balcão de passageiros (Galileosky)

[Dispositivos Galileosky](https://www.navixy.com/devices/galileosky/)quando integrados aos sensores de fluxo de passageiros PP-01, oferecem uma solução robusta para contar o número de passageiros que entram e saem dos veículos de transporte público. Essa integração aproveita a tecnologia Easy Logic da Galileosky, permitindo a coleta e a análise avançadas de dados, que podem ser monitoradas por meio da plataforma Navixy.

#### Exemplo de caso de uso

Imagine um operador de ônibus urbano que precisa monitorar o número de passageiros para otimizar as rotas e melhorar a eficiência do serviço. Ao integrar os dispositivos Galileosky com os sensores PP-01 e usar a plataforma Navixy, o operador pode monitorar com precisão o fluxo de passageiros, analisar tendências e tomar decisões informadas sobre ajustes de rotas e melhorias no serviço.

## Principais recursos e benefícios

- **Contagem de passageiros:** O sensor PP-01 conectado ao dispositivo Galileosky permite a contagem precisa dos passageiros que entram e saem do veículo.
- **Registro de dados baseado em eventos:** Os dados podem ser registrados com base em eventos específicos, como a abertura ou o fechamento de portas, garantindo que os dados dos passageiros sejam registrados apenas durante os períodos relevantes.
- **Registro de dados cumulativos:** O sistema também pode ser configurado para registrar dados cumulativos de passageiros, fornecendo um total de passageiros durante a viagem.

## Etapas de integração

1. **Conecte o sensor PP-01:**
  - O sensor PP-01 se conecta ao dispositivo Galileosky por meio da interface RS485. Certifique-se de que a conexão esteja correta seguindo as instruções de fiação fornecidas.
  - Configure a interface RS485 com os seguintes parâmetros:
    - Velocidade: 19200 bits/s
    - Bits de dados: 8
    - Bit de parada: 1
2. **Configure o sensor PP-01:**
  - Conecte o sensor PP-01 a um PC usando um adaptador RS485-USB.
  - Use o PP-01 Configuration Utility para configurar o sensor. Ajuste o endereço do sensor conforme necessário, escolhendo entre os intervalos de 1 a 8.
  - Use o Galileosky Configurator para carregar o script Easy Logic apropriado, dependendo do modo escolhido (registro baseado em eventos ou cumulativo).
  - Certifique-se de que o script tenha sido carregado e configurado com êxito no dispositivo Galileosky.
3. **Integração com a Navixy:**
  - Na plataforma Navixy, navegue até a seção "Devices and Settings" (Dispositivos e configurações) e vá para "Sensors and Buttons" (Sensores e botões).
  - Crie um novo sensor de medição e selecione a entrada correspondente à tag do usuário no dispositivo Galileosky.
  - Mapear os dados do sensor PP-01 para a plataforma Navixy, garantindo a correspondência correta entre os dados do sensor e a interface Navixy.

## Monitoramento e relatórios

- **Visualização em tempo real.** Uma vez integrados, os dados do passageiro podem ser monitorados em tempo real usando o widget "Sensor readings" (Leituras do sensor) no [Widgets de informações do dispositivo](/wiki/pages/createpage.action?spaceKey=USERDOCSOLD&title=Device%20information%20widgets).
- **Relatórios.** Você também pode gerar [Relatórios](../../../../relatorios/detalhes-especificos-do-relatorio/relatorio-de-sensores-de-medicao.md) que incluem dados de contagem de passageiros, permitindo uma análise abrangente e insights sobre o fluxo de passageiros.