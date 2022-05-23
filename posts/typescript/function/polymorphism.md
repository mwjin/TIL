---
layout: default
title: Polymorphism
parent: Function
grand_parent: Typescript
nav_order: 3
---

# Polymorphism

## Concept

- 함수에서의 polymorphism은 한 함수가 여러 형태로 호출될 수 있는 것을 의미한다.
- 예를 들어 한 함수가 여러 type의 인자와 리턴값을 가질 수 있다.
- Overloading은 polymorphism의 한 종류로 볼 수 있다.

## Example

```typescript
type SuperPrint = {
  (arr: number[]): void;
  (arr: boolean[]): void;
  (arr: string[]): void;
};

const superPrint: SuperPrint = (arr) => {
  arr.forEach((i) => console.log(i));
};

superPrint([1, 2, 3]);
superPrint([true, false]);
superPrint(["a", "b", "c"]);
superPrint(["a", "b", true, false]); // Not working!
```

- 위에서 `superPrint` 함수는 polymorphism을 가지고 있다.
- `superPrint(["a", "b", true, false])`는 동작하지 않는데, 이는 `SuperPrint` type이 `string | boolean` type을 지원해주고 있지 않기 때문이다.

## Reference

- https://www.bmc.com/blogs/polymorphism-programming/
