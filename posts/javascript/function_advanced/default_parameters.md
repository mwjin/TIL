---
layout: default
title: Default Parameters
parent: Function Advanced
grand_parent: Javascript
nav_order: 1
---

# Default Parameters

다음과 같이 function의 default parameter를 설정할 수 있다.

```javascript
const createBooking = function (
  flightNum,
  numPassengers = 1,
  price = 199 * numPassengers
) {
  ...
};
```

## 설명

- `flightNum`은 default parameter가 없다.
- `numPassengers`의 default parameter는 `1`이다.
- `price`의 default parameter는 `199 * numPassengers`이다.

## 유의 사항

`price`의 default parameter에는 `numPassengers`가 들어가 있다. 이와 같이 다른 argument를 default parameter로 사용하기 위해선 해당 argument가 먼저 resolving이 되어야 한다. 따라서 다음과 같이 작성할 수 없다.

```javascript
const createBooking = function (
  flightNum,
  price = 199 * numPassengers // Runtime Error!
  numPassengers = 1,
) {
    ...
};

createBooking('LH123', undefined, 2);  // Cannot access 'numPassengers' before initialization
```
