# SQL
___________________________________________________
### Задача 1
Есть данные по сумме оплат (sum) каждого клиента (email) по дням (date) в рамках каждой подписки (sub_id) 
Нужно вывести только вторые оплаты клиентов по каждой подписке
Суммы оплат в таблице ниже представлены не накопительным итогом, а оплатой за день  

**Решение:**
```sql
WITH sub_id_count
AS (
    SELECT email, date, sub_id, ROW_NUMBER() OVER(PARTITION by sub_id order by date) as paid_num
    FROM users
)
SELECT email, date, sub_id, 
FROM sub_id_count
WHERE paid_num = 2
```

### Задача 2
К данным в п.1 добавить столбец `week_begin`, который будет являться датой начала недели, в которую произошла оплата

**Решение:**
```SQL
with sub_id_count
AS (
	select 
	    email, 
	    date, 
	    sub_id, 
	    ROW_NUMBER() OVER(PARTITION by sub_id order by date) as paid_num
	from users
)
SELECT email, date, sub_id, DATE(date, "weekday 1") AS week_start
FROM sub_id_count
WHERE paid_num = 2
```

### Задача 3
**Описание данных:**  
таблица `ACTIVE_CLIENTS` содержит ежемесячный срез клиентов банка, которые совершали какие-либо транзакции в данном месяце.
Атрибуты: отчетный месяц (`report_month`) и идентификатор клиента (`client_id`). Считаем, что клиент «оттек» из банка в месяце **N**, если в месяце **N** он активен (присутствует в таблице `ACTIVE_CLIENTS`) 
и не активен в месяцы **N+1**, **N+2**, **N+3** (т.е. в течение 3-х месяцев).  
**Вывести:**
- количество активных клиентов на каждый месяц; 
- долю клиентов, которые «оттекли» в каждом месяце.

**Решение:**
```sql
SELECT 
    report_month,
    COUNT(DISTINCT client_id) AS active_clients_count,
    CAST(
        (COUNT(DISTINCT client_id) - LEAD(COUNT(DISTINCT client_id), 3, 0) OVER (ORDER BY report_month)) AS FLOAT
    ) / COUNT(DISTINCT client_id) AS not_active_clients_rate
FROM active_clients
GROUP BY report_month;
```

___________________________________________________
### Задача 4
**Как ускорить выполнение скрипта SQL?**
1) Стараться не использовать `*` при SELECT запросах, позволяет ускорить запросы при объединении ряда таблиц
2) Стараться не использовать оператор `IN` при больших выборках может приводить к полному сканированию последовательности и сложности вплоть до `n^2`
3) Использовать индексы для полей по которым может идти фильтрация, к примеру если мы храним исторические данные с датами и часто делаем выборки из них, это кажется неплохой идеей. Индексы отлично подходят для уникальных полей
4) Использование временных таблиц
5) Оптимизация запросов
6) Нормализация данных

### Задача 5
**Как восстановить удаленные объекты в БД?**
Если откровенно я этого ни разу не делал, но теоретически есть несколько вариантов.
1) Воспользоваться бэкапом БД за определённую дату с поиском удалённых элементов. Потребуется сценарий поиска.
2) Использовать журнал транзакций или его резервные копии


### Задача 6
**Почему не выполнится этот запрос?** 
```sql
SELECT user_name, YEAR(user_birth_date) AS year_of_birth 
FROM users 
WHERE year_of_birth = 2000
```
Потому что мы используем в операторе `WHERE` алиас `year_of_birth` а должны использовать исходное выражение `YEAR(user_birth_date)`.
Это связанно с порядком выполнения операторов, `WHERE` выполняется раньше, `SELECT` соответственно столбца `year_of_birth` ещё не существует.

### Задача 7
В чем отличие между запросам? Какой может вернуть больше строк? 
SELECT a.name, b.name FROM a LEFT JOIN b ON a.code=b.code WHERE b.name IS NOT NULL
```sql
SELECT a.name, b.name 
FROM a LEFT JOIN b ON a.code=b.code 
WHERE b.name IS NOT NULL
```
```sql
SELECT a.name, b.name 
FROM a LEFT JOIN b ON a.code=b.code AND b.name IS NOT NULL
```
**Ответ:**
В первом случае мы исключаем строки из результата - ```WHERE b.name IS NOT NULL```
Во втором случае мы применяем условие при объединении ```LEFT JOIN b ON a.code=b.code AND b.name IS NOT NULL```
Но так как мы используем оператор `LEFT JOIN` то во втором случае в результат будут добавлены все строки из таблицы `a`, так что 
при втором запросе мы получим больше записей.
Для примера возьмём 2 таблицу:  

<table>
<tr><th>Table a</th><th>Table b</th></tr>
<tr>
  <td>

| name   | code |  
|--------|------|  
| *NULL* | 1    |
| second | 2    |
| third  | 3    |
| four   | 4    |

  </td>
  <td> 

| name   | code |  
|--------|------|  
| *NULL* | 1    |
| second | 2    |
| third  | 3    |
| four   | 4    |

  </td>
</tr>
</table>

**В первом случае** 
мы используем оператор `LEFT JOIN` для объединения таблиц под подходящим параметрам и затем исключения всех строк ```WHERE b.name IS NOT NULL```
При выполнении первого запроса мы сначала объединим таблицы.
Это приведёт нас к следующему результату в первой колонке, после чего сработает WHERE и у нас останется всего пара записей.
<table>
<tr><th>1. Step - LEFT JOIN</th><th>2. Step - WHERE</th></tr>
<tr>
  <td>

| a.name  | b.name |  
|---------|--------|  
| *NULL*  | first  |
| second  | *NULL* |
| third   | third  |
| four    | *NULL* |

  </td>
  <td>

| a.name  | b.name |  
|---------|--------|  
| *NULL*  | first  |
| third   | third  |

  </td>
</tr>
</table>

**Во втором случае**
В результате будут включены все записи из таблицы **a** поэтому количество записей будет больше.

| a.name | b.name |  
|--------|--------|  
| *NULL* | first  |
| second | *NULL* |
| third  | third  |
| four   | *NULL* |


### Задача 8
Схема существующей таблицы приведена ниже:  

![table_schema](imgs/tables.jpg)

1. **Выбрать все кадастровые номера по дате добавления. Новые вначале**
> ```sql
> SELECT id, cadastral_number, add_date
> FROM cadastral_numbers
> ORDER BY add_date DESC
> ```

2. **Выбрать список домов с кадастровыми номерами**
> ```sql
> SELECT house, cadastral_number
> FROM 
>    houses INNER JOIN cadastral_numbers 
>    ON cadastral_numbers.id = houses.cadastral_number_id
> ```

3. **Сколько квартир в каждом доме, какой номер максимальной и минимальной**
> ```sql
> SELECT house, flats_amount, max_flat_number, min_flat_number
> FROM houses INNER JOIN(
>    SELECT 
>        house_id, 
>        COUNT(flat_number) AS flats_amount,
>        MAX(CAST(REPLACE(flat_number, "№", "") AS INTEGER)) AS max_flat_number,
>        MIN(CAST(REPLACE(flat_number, "№", "") AS INTEGER)) AS min_flat_number
>    FROM flats
>    GROUP BY house_id
>    ) ON houses.id = house_id
> ```
