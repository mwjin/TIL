---
layout: default
title: Methods of Functions
parent: Function Advanced
grand_parent: Javascript
nav_order: 4
---

# Methods of Functions

다음과 같은 상황을 생각해보자.

```javascript
const lufthansa = {
  airline: "Lufthansa",
  iataCode: "LH",
  bookings: [],
  book(flightNum, name) {
    console.log(
      `${name} booked a seat on ${this.airline} flight ${this.iataCode}${flightNum}`
    );
    this.bookings.push({ flight: `${this.iataCode}${flightNum}`, name });
  },
};

const book = lufthansa.book; // now it's a function
```

- `book(23, 'Sarha')` 같은 regular function call에서는 에러가 발생한다. Regular function call에서 함수의 `this`는 `undefined`이기 때문이다.
- `this`에 value를 assign하기 위한 *세 가지 method*가 존재한다.

## Call

```javascript
const eurowings = {
  airline: "Eurowings",
  iataCode: "EW",
  bookings: [],
};

book.call(eurowings, 23, "Sarah"); // first argument: `this`
console.log(eurowings);
```

- `call` 메소드의 첫 번째 인자는 함수의 `this`로 전달된다.
- 인자들은 전부 풀어서 나열한다.

## Apply

```javascript
const swiss = {
  airline: "Swiss Air Lines",
  iataCode: "LX",
  bookings: [],
};
const flightData = [583, "George Cooper"];
book.apply(swiss, flightData);
console.log(swiss);
```

- 첫 번째 인자는 `call`과 마찬가지로 함수의 `this`로 전달된다.
- `call`과 달리 함수의 인자들을 배열 형태로 전달한다.

## Bind

### Basic

```javascript
const bookEW = book.bind(eurowings);
const bookLH = book.bind(lufthansa);
const bookLX = book.bind(swiss);
bookEW(23, "Steven Williams");
```

- 첫 번째 인자로 함수의 `this`에 바인딩 할 object를 전달한다.
- 메소드의 결과값으로 `this`가 대체된 *새로운 함수*를 내뱉는다.

### Partial Application

```javascript
const bookEW23 = book.bind(eurowings, 23); // the first arg is already set
bookEW23("Minwoo Jeong");
```

- 위와 같이 본래 함수의 일부 인자들에 특정 값이 이미 적용되어 있는 형태의 함수를 만들 수도 있다.
- `bind` 메소드의 두 번째 인자부터 사용해서, 본래 함수의 첫 번째 인자부터 차례대로 적용한다.

```javascript
const addTax = (rate, value) => value + value * rate;

// Use null if we don't need to care about 'this' keyword (standard)
const addVAT = addTax.bind(null, 0.23);
console.log(addVAT(1000));
```

- `this`를 포함하지 않고 있는 임의의 함수에 대해서도 첫 인자를 `null`로 한 `bind` 메소드를 사용하면 partial application을 할 수 있다.
- 인자 순서에 유의하자.

### With Event Listener

```javascript
lufthansa.buyPlane = function () {
  console.log(this);
  this.planes++;
  console.log(this.planes);
};

// 'this' keyword will point to the lufthansa object
lufthansa.buyPlane();

// 'this' keyword will point to the HTML element
document.querySelector(".buy").addEventListener("click", lufthansa.buyPlane);
```

위와 같이 `this`가 포함된 오브젝트 메소드를 그대로 event listener에 적용하는 경우 `this`는 DOM이 가리키는 HTML element가 된다.

위 문제를 해결하기 위해서 다음과 같이 `bind` 메소드를 사용한다.

```javascript
document
  .querySelector(".buy")
  .addEventListener("click", lufthansa.buyPlane.bind(lufthansa));
```
