# Widget de estado da conexão

As configurações de estado de conexão permitem definir o intervalo de tempo após o qual um dispositivo GPS é considerado desconectado se parar de transmitir dados.

Talvez seja necessário ajustar essas configurações para dispositivos que informam dados com menos frequência. Isso evita que eles sejam marcados como off-line, garantindo que seu status seja mostrado com precisão, especialmente para dispositivos em modos de economia de energia.

> [!INFO]
> Você pode monitorar o [Estado da conexão](../rastreamento-por-gps/lista-de-objetos/estado-da-conexao.md) de seus dispositivos GPS, por exemplo, no [Lista de objetos](/wiki/pages/createpage.action?spaceKey=USERDOCSOLD&title=Object%20list)\-no aplicativo Tracking (Rastreamento) da interface da Web e no aplicativo móvel X-GPS Monitor. O estado da conexão é exibido como um indicador circular codificado por cores no widget de cada dispositivo, oferecendo uma referência visual rápida para avaliar se o dispositivo está conectado no momento, se não está conectado ou se perdeu a conexão.

O widget de estado da conexão em **Dispositivos e configurações** apenas uma configuração:

- **Intervalo de tempo**: Defina a duração após a qual um dispositivo será considerado desconectado se parar de transmitir dados. Você pode escolher entre minutos, horas ou dias.

![image-20240815-034950.png](attachments/image-20240815-034950.png)

O **Redefinir para os padrões** reverte as configurações para o tempo limite padrão, caso tenham sido feitas alterações. Normalmente, esse tempo é de 10 minutos, mas pode variar dependendo do modelo do dispositivo.

## Veja também

- [**Estado da conexão**](../rastreamento-por-gps/lista-de-objetos/estado-da-conexao.md) - explica os status de conexão dos dispositivos GPS na plataforma, incluindo seus significados, indicadores codificados por cores e como eles ajudam os usuários a monitorar a conectividade em tempo real e a transmissão de dados de seus dispositivos.