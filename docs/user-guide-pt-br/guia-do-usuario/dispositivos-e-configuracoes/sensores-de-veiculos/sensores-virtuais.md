# Sensores virtuais

# Sensores virtuais

Os sensores virtuais permitem que você processe os dados de telemetria com mais eficiência. Ao mapear a tensão da placa, eles podem ajudá-lo a calcular as horas do motor com base em condições e valores definidos. Além disso, eles permitem que você converta vários pontos de dados de diferentes sensores conectados a um dispositivo em indicadores mais fáceis de entender, como "quente", "frio", "aberto" e "fechado", independentemente do fabricante ou modelo do dispositivo. Isso abre novas possibilidades de monitoramento, rastreamento e previsão do desempenho de tecnologias complexas.

[![Virtual sensor interface](https://www.navixy.com/wp-content/uploads/2024/03/browser_clvf66ikbi.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_clvf66ikbi.png)

Interface de sensor virtual

## Como criar um sensor virtual

O sensor virtual pode ser criado por meio do portlet "Sensors and Buttons" (Sensores e botões) localizado na guia Devices and settings (Dispositivos e configurações):

1. Entre na seção de dispositivos e configurações.
2. Selecione um rastreador GPS.
3. Clique em "+".
4. Selecione a opção "Virtual sensor option" (Opção de sensor virtual).

Cada dispositivo pode ter até 100 sensores virtuais.

[![Virtual sensor adding in sensors and buttons portlet](https://www.navixy.com/wp-content/uploads/2024/03/browser_73sv6rayqh.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_73sv6rayqh.png)

Adição de sensor virtual no portlet de sensores e botões

As próximas etapas dependem do caso de uso que deve ser resolvido por meio do Sensor Virtual. Abaixo, você encontrará exemplos e instruções para diferentes métodos de cálculo.

## Métodos de cálculo

Os sensores virtuais têm três tipos diferentes de cálculo:

- Valor no intervalo.
- Valor de origem.
- Índice de bits.

Todos os valores dos sensores virtuais devem corresponder ao formato em que são recebidos do dispositivo. Todos os estados são suas definições para esses valores.

Aqui, descrevemos como funcionam os diferentes métodos de cálculo. Clique no nome do método de cálculo para expandir.

#### [Valor no intervalo](#1679329407451-09b70c96-6385)

Esse tipo de sensor virtual ajuda nossos clientes a manter parâmetros importantes, como ignição virtual, temperatura, umidade e nível de combustível, dentro de uma faixa especificada.

Veja como funciona:

- Se o valor do sensor estiver dentro dos limites especificados, será 1 para a plataforma. E 1 é igual ao seu valor A.
- Se o valor do sensor estiver fora desses quadros, o valor do sensor virtual será 0 para a plataforma. E 0 é igual ao seu valor B.

### Exemplo de ignição virtual

Se você não tiver uma entrada de ignição ou se o dispositivo já estiver funcionando em sua capacidade total, poderá usar uma Ferramenta de Ignição Virtual para detectar o estado da ignição. A tensão de bordo do carro aumentará significativamente quando o motor for ligado, permitindo que o limite de tensão seja usado como um indicador de que o motor está funcionando ou não. Geralmente, a tensão da placa deve exceder 13,2 V para indicar que o motor está funcionando.

Para criar esse sensor:

1. Comece dando um nome a ela.
2. Defina a entrada como Tensão da placa ou qualquer outro sensor, se necessário.
3. Habilite "Considerar como estado de ignição" nas configurações.
4. Escolha "Value in range" (Valor no intervalo) como método de cálculo.
5. Especifique um valor de intervalo mínimo, como 13,2 V. O valor máximo não é necessário, pois a tensão da placa pode variar com a ignição ligada.
6. Por fim, defina o significado dos estados 0 e 1 - geralmente são On e Off, respectivamente

[![Example configuration for virtual ignition](https://www.navixy.com/wp-content/uploads/2024/03/browser_7qx9prhhxc.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_7qx9prhhxc.png)

Exemplo de configuração para ignição virtual

Depois que você definir o intervalo de limite de tensão, se o valor de entrada a bordo estiver dentro desse intervalo, a plataforma mudará o estado da ignição para "ligado". Por outro lado, se estiver fora desse intervalo, a ignição será desligada. A ignição virtual criada por meio desse método também será levada em consideração em relatórios e notificações com base em seu status; por exemplo, você pode usá-la para gerar relatórios de horas do motor ou alertas de marcha lenta excessiva.

Além disso, essa ignição será usada para detecção de viagem e estacionamento com consideração de ignição.

### Exemplo com um sensor analógico

Esse exemplo é semelhante ao anterior, mas, em vez de monitorar a ignição do veículo, ele monitora a temperatura.

Suponha que você tenha um sensor analógico que coleta dados de temperatura - digamos que ele produza 1020 para -10°C e 1900 = 0°C. Os dados provenientes dos sensores analógicos não são calibrados e, portanto, também devem ser especificados dessa forma para o sensor virtual.

Podemos definir nosso intervalo - qualquer coisa entre 1020 e 1900 seria categorizada como "fria" (1) e qualquer coisa acima de 1900 seria considerada "quente" (0).

[![Example configuration for reading temperature from analog sensor](https://www.navixy.com/wp-content/uploads/2024/03/browser_kgzvrsdzb1.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_kgzvrsdzb1.png)

Exemplo de configuração para leitura de temperatura do sensor analógico

#### [Valor de origem](#1679329407460-fa411058-510d)

Com sensores virtuais, você pode atribuir sua definição a qualquer valor recebido. Esse método funciona com conjuntos predefinidos de valores e cadeias de caracteres, o que facilita o trabalho com valores estáticos sem a necessidade de especificar intervalos diferentes. Além disso, ele pode trabalhar com qualquer dado que você precisar. Por exemplo:

- 0/1,
- verdadeiro/falso,
- ligado/desligado,
- abrir/fechar,
- armado/desarmado,
- estado 1/estado 2/estado 3,
- tecla 1/tecla 2/tecla 3, etc.

O modo funciona da seguinte maneira:

- quando o valor 1 chega, esse é o valor A;
- quando o valor 2 chegar, esse será seu valor B;
- e quando o valor 3 chegar, esse será seu valor C e assim por diante.

Vamos ilustrar esse tipo de funcionalidade com exemplos concretos.

### Exemplo com leituras de CAN do carro

Alguns sensores CAN podem fornecer valores numéricos diferentes a uma plataforma. Por exemplo, temos um caminhão com CAN: sensor de estado da tomada de força que pode emitir apenas os seguintes valores:

- 0 - Desligado
- 1 - Manter
- 2 - Retenção remota
- 3 - Em espera
- 4 - Espera remota
- 5 - Conjunto
- 6 - Desacelerar
- 7 - Currículo
- 8 - Acelerar

Para configurar esse sensor:

1. Especifique seu nome.
2. Escolha a entrada.
3. Considere que a ignição deve estar desligada.
4. Selecione "Source Value" como método de cálculo.
5. Preencha a tabela com seus próprios valores no lado esquerdo e seus respectivos valores de sensor no lado direito. Adicione linhas clicando no sinal "+" e exclua-as usando o botão da lixeira.

[![Configuration example for source value calculation method](https://www.navixy.com/wp-content/uploads/2024/03/browser_xlxdl1ak9e.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_xlxdl1ak9e.png)

Exemplo de configuração para o método de cálculo do valor de origem

### Leituras-chave de hardware para motoristas, equipamentos e reboques

Alguns dispositivos podem ser capazes de ler os motoristas e seus iButtons, chaves RFID ou equipamentos conectados ao dispositivo por meio de sensores Bluetooth. A plataforma pode detectar o equipamento ou o motorista mais próximo do dispositivo, e o Sensor virtual é capaz de exibir esses nomes.

A maneira mais simples de identificação é por meio de tags - cada unidade conectada a um equipamento pesado tem seu próprio sensor com uma tag anexada, que é reconhecida pela plataforma como uma chave de hardware. Quando conectada à máquina, essa chave será enviada à plataforma e seu nome associado poderá ser exibido de forma compreensível - semelhante à forma como os valores da tomada de força foram nomeados.

[![Configuration example for source value calculation method for hardware key or state field sensor reading](https://www.navixy.com/wp-content/uploads/2024/03/browser_vw7hkgdl0n.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_vw7hkgdl0n.png)

Exemplo de configuração para o método de cálculo do valor de origem para a leitura da chave de hardware ou do sensor de campo de estado

#### [Índice de bits](#1679330119395-5e95e66b-c1e9)

Alguns dispositivos podem fornecer dados avançados em seus pacotes, às vezes mesclando vários parâmetros [em um único valor](https://www.navixy.com/blog/sensor-parameters-avl/). A ferramenta Virtual Sensors permite que você trabalhe com partes de valores telemáticos, decodificando assim os dados transmitidos pelo hardware do GPS.

Por exemplo, digamos que o valor 011 seja transmitido - primeiro devemos ler essas informações em little endian de acordo com o protocolo:

- 1 - Mostra o status do cinto do motorista: 0 - preso, 1 - solto. Bit 0
- 1 - Exibe o status da porta do motorista: 0 - fechada, 1 - aberta. Bit 1
- 0 - Indica a condição do exaustor: 0 - fechado, 1 - aberto. Bit 2

Cada posição no parâmetro exibe o valor de diferentes sistemas do veículo. Para configurá-los e exibi-los, é necessário criar um sensor separadamente para cada parâmetro.

Para um sensor que mostra a condição do capô do carro em nosso exemplo, você precisa

1. Defina o nome do sensor.
2. Escolha a entrada de acordo com a documentação do dispositivo.
3. Selecione "Bit Index" como método de cálculo
4. Escolha o bit 2 para esse campo.

Abaixo está um exemplo de um sensor que mostra a condição do capô do carro.

[![Configuration example for Bit index calculation sensor](https://www.navixy.com/wp-content/uploads/2024/03/browser_2qcam8zclk.png)

](https://www.navixy.com/wp-content/uploads/2024/03/browser_2qcam8zclk.png)

Exemplo de configuração para o sensor de cálculo de índice de bits

Quando um sensor virtual estiver configurado e o sensor do dispositivo associado tiver fornecido dados, eles poderão ser visualizados no widget "Sensor Readings" (Leituras do sensor) na guia Information (Informações) do dispositivo. Os sensores do dispositivo agora podem falar em seu idioma.