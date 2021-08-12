---
layout: default
title: Coding Test Practice
parent: MySQL
nav_order: 1
---

# Coding Test Practice

- Programmars SQL 고득점 Kit를 풀면서 알게 된 쿼리 작성 요령을 정리하였다.
- Ref: [프로그래머스 SQL 고득점 Kit][(](https://programmers.co.kr/learn/challenges))

## Basics

- Column 기준 정렬 `order by`

  ```sql
  -- Asceding order
  select column1, column2, ... from table order by your_column;

  -- Descending order
  select column1, column2, ... from table order by your_column desc;
  ```

- 특정 조건에 맞는 row 찾기 `where`
  ```sql
  select column1, column2, ... from table where condition;
  ```
  - Comparison operator: `=, !=, >, < ...`
  - `column between a and b`: column의 값이 [a, b]
  - 여러 값과의 비교: `IN 이용`
    ```sql
    -- Example
    select col from t where col in ('a', 'b', 'c');
    ```
- 상위 N개 record 만 출력 `limit`

  ```sql
  select column from table order by column limit N;
  ```

- Group function
  ```sql
  select func(column) from table;
  ```
  - 자주 쓰는 function의 종류: `max`, `count`, `min`, `sum` 등
  - 만약 group 별로 group function을 적용하고 싶다면 `group by`
  ```sql
  select func(column) from table group by column;
  ```

## Intermediate

- 중복 제거하기 `distinct`
  ```sql
  select distinct column from table;
  ```
  만약 unique 한 값의 개수를 세고 싶다면
  ```sql
  select count(distinct column) from table;
  ```
- Group function 의 결과를 조건문에서 이용하고 싶다면 where 대신 `having`
  ```sql
  -- example
  select column, count(column) cnt from table group by column having cnt > 1;
  ```
  위 상황에선 group by 바로 뒤에 having이 와야 한다.
- Group function과 having, order by 의 조합
  ```
  select column, count(column) cnt from table group by column having condition order by column;
  ```
  위의 순서여야 한다.

## Advanced

- 1부터 N까지의 순차적인 sequence 출력하기는 `with recursive` 이용
  ```sql
  with recursive table (n) as (
  select 1
  union all
  select n + 1 from table where n < N - 1
  )
  select n from table;
  ```
- Join
  크게 4가지의 Join이 있다.
  - `inner join`: 두 테이블이 공통으로 가지고 있는 key에 대한 record 만을 출력
    ```sql
    -- example
    select a.id
    from table1 a inner join table2 b
    on a.id = b.id;
    ```
  - `left join`
    - 왼쪽 table이 가지고 있는 key 값들을 기준으로 join.
    - 왼쪽 table이 가지고 있지만 오른쪽 table이 가지고 있지 않는 key가 있다면 그 key에 대한 record 중 오른쪽 table만 가지고 있던 column의 값은 NULL이 된다.
    - 사용법은 위의 예시에서 inner 대신 left
  - `right join`
    - left join의 설명에서 왼쪽과 오른쪽이 바뀌면 된다.
    - 사용법은 위의 예시에서 inner 대신 right
  - full outer join
    - Left join과 Right join의 `UNION ALL`
    ```sql
    select * from t1
    left join t2 on t1.id = t2.id
    union all
    select * from t1
    right join t2 on t1.id = t2.id;
    ```
- NULL 처리 함수

  - JOIN을 하다 보면 null 값이 발생.
  - NULL 대신 다른 값을 출력하기 위해 다음 함수들을 이용할 수 있다.
    - `ifnull(col, alt_value)`: 어떤 row에서 col의 값이 NULL이면 alt_value를 대신 출력
    - `coalesce(col1, col2, ...)`: col1, col2, ... 중 가장 먼저 NULL이 아닌 값 출력
  - NULL 과 관련된 조건문
    - `ISNULL(column)`
    - `NOT ISNULL(column)`

- String 관련 함수
  - 일반적인 string 비교는 `=`와 같은 연산 이용
  - starts with: `LIKE` 이용
    ```sql
    select column from table where column like 'prefix%'
    ```
  - 특정 글자를 포함하는 지 여부

    ```sql
    -- 1. 'al'를 포함하는지 여부
    -- LIKE
    select col from t where col like '%al%';
    -- REGEXP
    select col from t where col regexp 'al';

    -- 2. 'al', 'el' 둘 중 하나 포함
    select col from t where col regexp 'al|el';
    ```

  - 특정 date format으로 변환: `date_format(col, format)`
    ```sql
    select date_format(col, '%Y-%m-%d') from table;
    ```
- `CASE ... WHEN ...`: select의 column 자리에 넣을 수 있는 조건문으로, 조건에 따라 출력되는 값을 정하고 싶을 때 유용
  ```sql
  select col1,
  case
  when cond1 then val1
  when cond2 then val2
  else val3
  end as col2 from table;
  ```
