---
layout: default
title: Passing Arguments
parent: Function Advanced
grand_parent: Javascript
nav_order: 2
---

# Passing Arguments

## Pass a value as an argument

```javascript
const appendMr = function (name) {
  name = "Mr." + name;
};

const myName = "Minwoo Jeong";
appendMr(myName);
console.log(myName); // Minwoo Jeong
```

- `const name = myName` 하는 것과 같다.
- `myName`의 값을 `name`으로 복사한다.

## Pass a reference as an argument

```javascript
const updatePassengerName = function (passenger) {
  passenger.name = "Mr." + passenger.name;
};

const me = { name: "Minwoo Jeong" };
updatePassengerName(me);
console.log(me.name); // Mr. Minwoo Jeong
```

- `const passenger = me` 하는 것과 같다.
- `me`의 값을 `myName`으로 복사한다.
- `me`는 heap 메모리 상의 object를 가리키는 메모리 주소이다.
- **위 연산은 이 메모리 주소라는 값을 argument로 전달한 것이다.**
- _Pass by reference_ 와는 다르다는 것에 주의하라.
- Javascript는 오직 _Pass by value_ 뿐이다.
