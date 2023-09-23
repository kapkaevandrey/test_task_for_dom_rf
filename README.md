# test_task_for_dom_rf
## Тестовое задание для Банка [Дом.рф](https://xn--d1aqf.xn--p1ai/)
___________________________________________________
[![linting and testing](https://github.com/kapkaevandrey/test_task_for_dom_rf/actions/workflows/ci.yaml/badge.svg)](https://github.com/kapkaevandrey/test_task_for_dom_rf/actions/workflows/ci.yaml)

## 1. SQL
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
```SQL

```

### Задача 4
Как ускорить выполнение скрипта SQL?


### Задача 5
Почему не выполнится этот запрос? 
```sql
SELECT user_name, YEAR(user_birth_date) AS year_of_birth 
FROM users 
WHERE year_of_birth = 2000
```

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