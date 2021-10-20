---
layout: default
title: Type Conversion and Coercion
parent: Fundamentals
grand_parent: Javascript
nav_order: 2
---

# Type Conversion and Coercion

## Type Conversion

- 특정 type의 값을 또 다른 type의 값으로 *명시적*으로 전환하는 것.
- `Number()`, `String()`, `Boolean()` 과 같은 함수를 이용한다.
- Number, String, Boolean으로의 전환만 가능하다.
- 예시
  ```javascript
  const num = Number("1"); // 1
  const str = String(123); // '123'
  const bool = Boolean(1); // true
  const bool2 = Boolean(undefined); // false
  ```

## Type Coercion

- 필요 시 javascript가 특정 type의 값을 다른 type의 값으로 *암묵적*으로 전환하는 것.
- 대표적으로 type coercion이 발생하는 경우는 다음과 같다.
  - 서로 다른 type의 값끼리 연산하는 경우
  - 서로 다른 type의 값끼리 비교하는 경우
  - if - else statement의 condition으로 값이 사용되는 경우

### 서로 다른 type의 값끼리 연산하는 경우

- 이에 해당하는 경우들 중 가장 빈번한 경우는 integer 또는 decimal이 string type으로 명시되어 있고 이를 그대로 사칙연산에 사용하는 경우이다.
- 이 때 **+ 연산은 모든 operand를 string으로, 그 외에는 전부 Number로 type coercion 된다고 생각하면 된다.**
- 예시

  ```javascript
  let result = "1" + "2"; // '12' (String concatenation)
  result = 1 + "2"; // '12' (String concatenation)

  result = "1" - "2"; // -1
  result = 1 - "2"; // -1

  result = "3" * "4"; // 12
  result = "3" * 4; // 12
  ```

### 서로 다른 type의 값끼리 비교하는 경우

- 가장 빈번한 경우는 string으로 명시된 number와 일반 number type의 값을 비교하는 것이다.
- 이 때 일반적으로 string은 number로 type coercion이 된다.
- 특이한 것은 equality, inequality 연산을 수행할 때이다.
- Type coercion의 유무에 따라 equality 연산은 두 개의 연산자가 존재한다.

  - `==`: _Loose_ equality operator -> _Type coercion 수행_
  - `===`: _Strict_ equality operator -> _Type coercion을 수행하지 않음_

- Inequality 연산도 위와 같은 방식으로 두 개의 연산자가 존재한다.

  - `!=`: _Loose_ equality operator
  - `!==`: _Strict_ equality operator

- 예시

  ```javascript
  console.log(23 == "23"); // true
  console.log(23 === "23"); // false
  ```

- 가급적이면 type coercion이 발생하지 않는 _strict_ operator를 사용하자.

### if - else statement의 condition으로 값이 사용되는 경우

- **Truthy value이면 true, falsy value이면 false이다.**
- Falsy value는 총 5가지가 있다.
  - `0`
  - `''` (Empty string)
  - `undefined`
  - `null`
  - `NaN` (This is a number type, Not a Number.)
