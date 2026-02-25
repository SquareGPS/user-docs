# Navixy WS

Протокол пересылки данных Navixy Web Service отличается гибкостью, позволяя третьим сторонам хранить данные о флоте в своих базах данных для использования в любых целях или отображать данные на веб-ресурсах.

Поскольку этот протокол пересылки данных не зависит от платформы, он станет идеальным вариантом для любого партнера, работающего с XML-файлами.

Общая техническая информация о веб-сервисе Navixy  
Протокол веб-сервиса Navixy использует SOAP для получения XML-данных с устройств слежения в рамках прикладного уровня OSI. Данные извлекаются по требованию.

Отправляемые поля данных:

- DateGPS
  - Date and time in UTC
- Ignition
  - Boolean ignition status
- Latitude
- Longitude
- SpeedGPS
  - km/h
- UnitPlate
  - License plate
- Altitude
  - Meters
- Course
  - Direction vehicle is heading, for example: N,S,E,O,NO,NE,SO,SE
- DeviceID
  - IMEI
- NumSat
  - Number of GNSS satellites the device is utilizing
- Odometer
  - Traveled distance in km

## Конфигурация Navixy WS

### Setting up

#### Navixy settings:

Необходимые параметры

- ЛОгин и Пароль
  - Это может быть все что угодно, так как это не токен

Чтобы настроить пересылку данных в протоколе ILSP, откройте настройки устройства в главном меню, нажав на иконку «Шестеренка» в левой нижней части экрана.

Затем нажмите на виджет «**Ретрансляция данных**».

Нажмите «**Протоколы ретрансляции**».

Откроется всплывающее окно, в котором нужно ввести необходимые параметры, нажав кнопку +.

Для протокола ILSP введите необходимую информацию.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-4-600x112.png)

### Внешний доступ:

Необходимые параметры

- Логин и пароль
  - Они должны соответствовать тем, что были введены выше
- идентификаторы устройств
  - Не более 100
- дата начала и дата окончания

Ниже приведен пример для 9 сентября 2022 года с 12:00 UTC до 11:59:59

UTC: 2022-09-01T00:00:00Z - 2022-09-01T11:59:59Z

Описание протокола в WSDL, относящееся к месту расположения сервера, можно найти ниже:

EU [https://soap.navixy.com/LocationDataService?wsdl](https://soap.navixy.com/LocationDataService?wsdl)

США [https://soap.us.navixy.com/LocationDataService?wsdl](https://soap.us.navixy.com/LocationDataService?wsdl)

Запрос SOAP должен быть сделан с использованием одной из вышеуказанных страниц WSDL. Сам XML-запрос выглядит следующим образом и заменяется сопутствующей информацией:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org">

   [soapenv:Header](#)

   [tem:authentication](#)

    <login>username</login>

    <password>password</password>

   </tem:authentication>

   </soapenv:Header>

   [soapenv:Body](#)

   [tem:dataRequest](#)

      <!--1 to 100 repetitions:-->

      <deviceIds>IMEI of device</deviceIds>

      <startDate>2022-08-30T00:00:00Z</startDate>

      <endDate>2022-08-31T00:00:00Z</endDate>

   </tem:dataRequest>

   </soapenv:Body>

</soapenv:Envelope>

An example response may look something like this:

      <result>

         <dateGps>2022-08-30T00:02:55.000Z</dateGps>

         <ignition>false</ignition>

         <latitude>75.9270866</latitude>

         <longitude>-85.5207616</longitude>

         <speedGps>0.0</speedGps>

         <unitPlate>ss3ssj</unitPlate>

         <altitude>284.0</altitude>

         <course>E</course>

         <deviceId>866258048802349</deviceId>

         <numSat>15</numSat>

         <odometer>59845</odometer>

      </result>

### Управление

Чтобы изменить или остановить пересылку данных, выполните следующие действия:

Чтобы остановить пересылку данных, нажмите кнопку «Корзина».

Затем подтвердите изменения во всплывающем окне.

Чтобы изменить настройки ретранслятора, такие как имя, данные для входа или включение, нажмите «Управление ретрансляторами».

Откроется окно управления ретрансляторами. Выберите строку для редактирования и либо нажмите на карандаш в левом верхнем углу, либо дважды щелкните по строке, чтобы разрешить редактирование. Сохраните все изменения.

![Recurso Confiable](https://www.navixy.com/wp-content/uploads/2022/10/pasted-image-0-1-2-600x106.png)

### Диагностика

Для проверки и тестирования ваших SOAP-запросов к платформе рекомендуется использовать SoapUI, который можно найти здесь: [https://www.soapui.org/downloads/soapui/.](https://www.soapui.org/downloads/soapui/.)

- Установите Soap UI
- В меню «Файл» выберите «Новый проект SOAP».
- Вставьте правильный путь в поле WSDL в соответствии с сервером и выберите «Create sample requests for all operations?».
  - США: [https://soap.us.navixy.com/LocationDataService?wsdl](https://soap.us.navixy.com/LocationDataService?wsdl)
  - ЕС: [https://soap.navixy.com/LocationDataService?wsdl](https://soap.navixy.com/LocationDataService?wsdl)