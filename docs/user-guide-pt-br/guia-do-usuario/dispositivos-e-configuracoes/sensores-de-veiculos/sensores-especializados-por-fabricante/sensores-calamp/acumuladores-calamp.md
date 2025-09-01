# Acumuladores CalAmp

[Dispositivos CalAmp](https://www.navixy.com/devices/calamp/) são equipados com acumuladores (variáveis) que armazenam vários tipos de dados, dependendo de como o dispositivo é configurado pelo usuário.

Para otimizar a integração e o uso desses acumuladores na plataforma Navixy, foi introduzido um widget dedicado. Esse widget permite que os usuários configurem e recuperem facilmente os dados dos seguintes acumuladores:

## Acumuladores suportados

- **Tensão da placa**: Monitora o nível de tensão da placa interna do dispositivo, o que é crucial para avaliar a integridade e o status de energia do dispositivo.
- **Sensores externos de temperatura (1-8)**: Captura dados de até 8 sensores de temperatura externos conectados ao dispositivo CalAmp, permitindo o monitoramento detalhado das condições ambientais.
- **Quilometragem de hardware**: Esses são os dados de quilometragem calculados diretamente pelo próprio dispositivo, fornecendo uma medida precisa da distância percorrida com base na entrada do hardware em vez de apenas nos dados do GPS.
- **Valores do sensor analógico (1-8)**: Recupera leituras de até 8 sensores analógicos conectados ao dispositivo, permitindo o monitoramento de uma ampla gama de entradas, como pressão, umidade ou outros sinais analógicos.
- **IO\_States (Estados de entrada/saída)**: Exibe o status dos canais de entrada e saída do dispositivo, essencial para entender a interação em tempo real entre o dispositivo e os periféricos conectados.
- **ID do iButton (partes baixa e alta)**: Captura o identificador exclusivo dos dispositivos iButton em duas partes (baixa e alta), que normalmente é usado para identificação do motorista ou controle de acesso em aplicativos de gerenciamento de frota.

## Configuração dos acumuladores CalAmp na Navixy

Para configurar e monitorar esses acumuladores na plataforma Navixy, siga estas etapas:

1. Acesse a seção "Devices and Settings" (Dispositivos e configurações)
2. Selecione o dispositivo CalAmp desejado
3. Abra o widget Acumuladores. Você pode selecionar os acumuladores que deseja monitorar. Dependendo de seus requisitos, é possível ativar o monitoramento da tensão da placa, dos sensores de temperatura externos, da quilometragem do hardware, dos valores do sensor analógico, dos estados de E/S e das peças de ID do iButton.
4. Salve sua configuração.

## Monitoramento dos dados do acumulador

Uma vez configurado, você pode visualizar os dados em tempo real dos acumuladores selecionados diretamente na plataforma Navixy. Esses dados podem ser usados para vários fins de monitoramento e relatórios, dependendo de suas necessidades operacionais.

## Aplicações práticas

- **Gerenciamento de frotas**: Monitore a quilometragem do hardware para rastreamento preciso de distância e programação de manutenção.
- **Monitoramento ambiental**: Use sensores de temperatura externos para rastrear as condições ambientais dentro da carga ou ao redor dos veículos.
- **Identificação do motorista**: Implemente o monitoramento do iButton ID para garantir que somente o pessoal autorizado opere seus veículos.
- **Monitoramento de entrada analógica**: Rastreie várias entradas analógicas para aplicações especializadas, como monitoramento de níveis de fluido ou pressão em tanques.