---
layout: default
title: Closures
parent: Function Advanced
grand_parent: Javascript
nav_order: 6
---

# Closures

## Background Knowledge

- Javascript engine에서 _Execution Context (EC)_ 는 global context와 각 function에 대해 생성된다.
- 각 EC는 해당하는 context에 대한 _Variable Environment (VE)_ 를 가지고 있다

## Explain

- **Closure는 어떤 함수를 둘러싸고 있는 EC의 VE이다.**
- Javascript 상에서 정의된 모든 함수는 해당 함수가 생성된 EC의 VE에 접근할 수 있다.
- 심지어 해당 EC가 callstack 상에서 이미 남아 있지 않더라도 접근 가능하다.
- **함수는 자신이 탄생한 장소에 있던 모든 variable을 기억한다. Closure는 이 variable들을 담아두는 가방과도 같다.**

## More Information

- Closure에 속한 variable이 scope chain보다 우선 순위가 높다.
- Closure는 유저가 직접 생성, 접근, 조작하는 것이 불가능하다. Javascript가 자동으로 알아서 다 한다.

## Example

```javascript
const secureBooking = function () {
  let passengerCount = 0;

  return function () {
    passengerCount++;
    console.log(`${passengerCount} passengers`);
  };
};

const booker = secureBooking();
booker(); // 1 passengers
booker(); // 2 passengers
booker(); // 3 passengers
```

위에서 `secureBooking` 내부에 정의된 `passengerCount`에 `booker` 함수가 접근이 가능하다.

```javascript
let f;

const g = function () {
  const a = 23;
  f = function () {
    console.log(a + 2);
  };
};

g();
f(); // 25
```

위 예시에서 `f`에 대한 정보를 출력하면 다음과 같다.

```javascript
console.dir(f);

/*
{
  arguments: null,
  caller: null,
  length: 0,
  name: "f",
  prototype: {constructor: ƒ},
  [[FunctionLocation]]: VM962:5,
  [[Prototype]]: ƒ (),
  [[Scopes]]: Scopes[3],
    0: Closure (g)
      a: 23
    1: Script
    2: Global
  ...
}
*/
```

아래 예시를 통해 closure 내의 variable이 scope chain 상의 variable 보다 더 우선 순위가 높음을 알 수 있다.

```javascript
const boardPassengers = function (n, wait) {
  const perGroup = n / 3;
  setTimeout(function () {
    console.log(`We are now boarding all ${n} passengers`);
    console.log(`There are 3 groups, each with ${perGroup} passengers`);
  }, wait * 1000);
  console.log(`Will start boarding in ${wait} seconds`);
};

const perGroup = 1000; // Lower priority
boardPassengers(180, 3);

// Will start boarding in 3 seconds
// We are now boarding all 180 passengers (After 3 seconds)
// There are 3 groups, each with 60 passengers
```

다음과 같이 nested function을 정의하더라도 최상위 함수의 VE에 접근할 수 있다.

```javascript
const nested = function () {
  const n = 100;
  return function () {
    const m = 120;
    return function () {
      console.log(m, n);
    };
  };
};

const f1 = nested();
const f2 = f1();
f2();
```

위 케이스에서 `f2`의 `[[Scope]]`는 다음과 같다.

- 0: Closure {m: 120}
- 1: Closure (nested) {n: 100}
- 2: Script {...}
- 3: Global {...}
