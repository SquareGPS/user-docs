# Sensores de nível de combustível BLE (Teltonika)

Muitos [Dispositivos GPS Teltonika](https://www.navixy.com/devices/teltonika/) suportam sensores de combustível sem fio que se conectam via Bluetooth. As vantagens de usar esses sensores de combustível Bluetooth são significativas:

- **Sem fios**: O sensor e o rastreador não precisam de uma conexão física, o que simplifica a instalação.
- **Independência de fontes de energia externas**: Esses sensores vêm com uma bateria integrada que pode durar vários anos sem a necessidade de recarga.
- **Dados adicionais**: Além dos níveis de combustível, o sensor também transmite dados sobre a temperatura, a umidade e o nível de carga da bateria.

## Preparação do dispositivo GPS

Para preparar seu dispositivo GPS Teltonika para a integração do sensor de combustível Bluetooth, siga estas etapas.

[![Bluetooth fuel sensors](https://www.navixy.com/wp-content/uploads/2019/09/teltonika.configurator_2019-09-28_13-56-33-600x365.png)

](https://www.navixy.com/wp-content/uploads/2019/09/teltonika.configurator_2019-09-28_13-56-33.png)

1. **Faça o download do configurador Teltonika**: Obtenha o aplicativo no site oficial da Teltonika.
2. **Atualizar o firmware**: Certifique-se de que o dispositivo esteja executando a versão mais recente do firmware.
3. **Executar o configurador**:
  - Ir para o **Sistema** guia.
  - Altere o protocolo de transferência de dados para **Codec 8 Extended**.
4. **Conecte o sensor de combustível**:
  - Navegue até a seção **Bluetooth** no configurador.
  - Conecte o sensor de combustível ao rastreador.
5. **Habilite os parâmetros necessários**:
  - Ir para o **E/S** guia.
  - Certifique-se de que o parâmetro correspondente ao sensor de combustível esteja ativado.

> [!INFO]
> **Codec 8 Extended** é um protocolo de comunicação proprietário da Teltonika que suporta até 65.535 parâmetros de dados (IDs AVL), permitindo uma transmissão de dados mais detalhada em comparação com o Codec 8 padrão, que suporta apenas 255.

## Configuração do sensor na plataforma Navixy

Quando o rastreador estiver conectado e transmitindo dados de combustível, siga estas etapas para configurar os sensores correspondentes na plataforma Navixy.

[![Bluetooth fuel sensors](https://www.navixy.com/wp-content/uploads/2019/09/chrome_2019-09-28_13-59-40-600x296.png)

](https://www.navixy.com/wp-content/uploads/2019/09/chrome_2019-09-28_13-59-40.png)

1. **Criar um novo sensor de medição**:
  - Navegue até Dispositivos e configurações → Sensores e botões.
  - Clique em Criar um novo [sensor de medição](../../measurement-sensors.md).
2. **Configurar o sensor**:
  - Selecione a entrada rotulada como "BLE: LLS level" (Nível LLS).
  - Defina o tipo de sensor e as unidades. Se necessário, preencha a tabela de calibração e ajuste outras configurações.
3. **Repetir para sensores adicionais**:
  - Se você tiver vários sensores de combustível, repita o processo de configuração para cada sensor, selecionando a entrada apropriada para cada um.
4. **Monitorar e relatar**:
  - Depois de configurado, você pode monitorar o nível de combustível no widget designado na plataforma.
  - Você também pode gerar relatórios detalhados sobre o consumo de combustível.

Essa configuração permite que você utilize totalmente os recursos dos sensores de combustível Teltonika Bluetooth, fornecendo dados precisos e em tempo real sobre níveis de combustível, temperatura e muito mais.