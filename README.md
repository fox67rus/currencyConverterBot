# currencyConverterBot
Telegram-бот возвращает цену на определённое количество валюты (евро, доллар или рубль)

Человек должен отправить сообщение боту в виде 

**<имя валюты, цену которой он хочет узнать>** 
**<имя валюты, в которой надо узнать цену первой валюты>** **<количество первой валюты>**

<b>Пример работы бота</b><br>
Ваше сообщение:<br>
<pre>
доллар рубль 100
</pre>
Ответ бота:
<pre>
7355 RUB
</pre>
<br>


<b>Список команд </b><br>
<table>
  <tr>
    <th>Команда</th>
    <th>Описание команды</th>
  </tr>
   <tr>
    <td><code>/start</code>или<code>/help</code></td>
    <td>Инструкции по применению бота.</td>
  </tr>
  <tr>
    <td><code>/values</code></td>
    <td>Информация о всех доступных валютах</td>
  </tr>
</table>