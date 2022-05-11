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
