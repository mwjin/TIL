---
layout: default
title: First Class
parent: Function Advanced
grand_parent: Javascript
nav_order: 3
---

# First Class

## 설명

- Javascript에서 함수는 **First-class citizens** 이다.
- **함수는 하나의 값으로 취급된다**는 의미이다.
- 함수는 자바스크립트 객체의 또 하나의 타입이다.

## 예시

- 함수를 변수 또는 Object의 property로 저장

```javascript
const add = (a, b) => a + b;

const counter = {
  value: 25,
  inc: function () {
    this.value++;
  },
};
```

- 함수를 또 다른 함수의 인자값으로 전송 (e.g. callback)

```javascript
const greet = {} => console.log('Hey Minwoo');
btnClose.addEventListener('click', greet);
```

- 함수를 또 다른 함수로부터 return

```javascript
function count() {
  let counter = 0;
  return function () {
    counter++;
  };
}
```

- 함수에 대한 method를 호출 e.g. `call`, `apply` and `bind`

## Higher-Order Functions

- 다른 함수를 인자로 받거나 리턴값으로 사용하는 함수를 **Higher-Order Function**이라고 한다.
- 위 예시에서 `addEventListener`, `count` 함수들이 해당된다.
- *First Class*는 자바스크립트의 특징, *Higher-Order Function*은 이 특징을 활용한 사례이다.

### Callback

- 다른 함수에 인자로 전달되는 함수를 일반적으로 콜백(Callback) 함수라고 한다.
- 예시: `oneWord`와 `upperFirstWord`

  ```javascript
  const oneWord = function (str) {
    return str.replace(/ /g, "").toLowerCase();
  };

  const upperFirstWord = function (str) {
    const [first, ...others] = str.split(" ");
    return [first.toUpperCase(), ...others].join(" ");
  };

  const transformer = function (str, fn) {
    console.log(`Original string: ${str}`);
    console.log(`Transformed string: ${fn(str)}`);
    console.log(`Transformed by: ${fn.name}`);
  };

  transformer("Javascript is the best!", upperFirstWord);
  transformer("Javascript is the best!", oneWord);
  ```

- 위와 같이 콜백 함수를 사용하는 이유는 추상화를 증가시키기 위함이다.
- 함수를 정의하면서 세부 동작을 감출 수 있다.
  - e.g. `transformer` 함수는 `upperFirstWord`의 내부 동작을 신경쓰지 않는다.

### Functions Returning Functions

일반적인 예시는 다음과 같다.

```javascript
const greet = function (greeting) {
  return function (name) {
    console.log(`${greeting} ${name}`);
  };
};

const greeter = greet("Hey");
greeter("Minwoo");
greeter("Jin");

greet("Hello")("Minwoo");
```

Arrow function을 활용하면 다음과 같이 작성할 수 있다.

```javascript
const greet2 = (greeting) => (name) => {
  console.log(`${greeting} ${name}`);
};

greet2("Hello")("Minwoo");
```
