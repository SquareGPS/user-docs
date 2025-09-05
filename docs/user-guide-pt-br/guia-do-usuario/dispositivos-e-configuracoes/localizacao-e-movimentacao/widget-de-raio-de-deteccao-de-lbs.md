# Widget de raio de detecção de LBS

O **Raio de detecção de LBS (serviço baseado em localização)** determina a distância que o sistema procurará por sinais de estações de base de celular ou pontos de Wi-Fi para identificar a localização de um dispositivo. Essa configuração é fundamental para garantir o rastreamento preciso da localização com base no ambiente em que o dispositivo opera.

- **Áreas rurais**: Em locais rurais com menos estações rádio-base, é recomendável aumentar o raio do LBS. Isso permite que o sistema utilize estações rádio-base mais distantes, aumentando as chances de localizar o dispositivo.
- **Áreas urbanas**: Em cidades com alta densidade de estações rádio-base, o raio do LBS deve ser menor. A proximidade de várias estações rádio-base fornece sinais suficientes para o rastreamento preciso da localização, portanto, um raio menor ajudará a manter uma precisão maior.

Ajuste o raio de detecção de LBS com base no ambiente operacional do dispositivo para equilibrar a precisão e a cobertura do sinal.

![image-20240815-180931.png](attachments/image-20240815-180931.png)

Na Navixy, os locais de LBS são exibidos no mapa como círculos. O centro indica a localização estimada, enquanto o raio mostra a possível imprecisão. Um círculo menor sugere maior precisão, normalmente vista em áreas urbanas, enquanto um círculo maior indica maior imprecisão, comum em áreas rurais.