# currencyConverterBot
Telegram-бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
Данные по курсам валют получаются с помощью [Cryptocompare API ](https://min-api.cryptocompare.com/documentation)

Человек должен отправить сообщение боту в виде: 

**<имя валюты, цену которой он хочет узнать>** 
**<имя валюты, в которой надо узнать цену первой валюты>** **<количество первой валюты>**

**Пример работы бота**

Ваше сообщение:
```
доллар рубль 100
```

Ответ бота:
```
Конвертируем евро в рубль: 
Цена 100 EUR  = 7842.0 RUB
```

**Список доступных команд**

<table>
  <tr>
    <th>Команда</th>
    <th>Описание команды</th>
  </tr>
   <tr>
    <td><code>/about</code></td>
    <td>Информация о боте</td>
  </tr>
   <tr>
    <td><code>/start</code>или<code>/help</code></td>
    <td>Инструкции по применению бота.</td>
  </tr>
  <tr>
    <td><code>/values</code></td>
    <td>Информация о всех доступных валютах</td>
  </tr>
  <tr>
    <td><code>/rate</code></td>
    <td>Получение курса иностранных валют по отношению к рублю</td>
  </tr>
</table>

Для написания бота использовалась библиотека **pyTelegramBotAPI==4.10.0**