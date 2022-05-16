---
layout: default
title: Declaration
parent: Type
grand_parent: Typescript
nav_order: 1
---

# Declaration

## Implicit vs. Explicit

```typescript
let a = "Hello"; // Implicit (a: string) -> Recommended!
let b: boolean = true; // Explicit
a = 1; // Illegal!
```

- _Implicit_: Typescript의 Type Checker가 literal을 기반으로 유추하는 것
- _Explicit_: 유저가 명시할 수 있다.
- 일반적으로 Implicit declaration을 추천한다. Type checker에게 추론을 맡기는 것이 간단하고 가독성이 좋아진다.

## Array

```typescript
let c = [1, 2, 3];
let d: number[] = [];
c.push("1"); // Illegal!
```

- 위에서 `c`, `d`모두 `number[]` type을 가진다.
- Type이 결정되고 난 뒤 type이 다른 또 다른 원소를 추가하는 것은 불가능하다.

## Object

- _Implicit_

```typescript
const player = {
  name: "Minwoo Jeong",
};

player.hello(); // Illegal
player.name = 1; // Illegal
```

위의 경우 `{ name: string }`으로 type을 추론한다.

- _Explicit_

```typescript
const player: { name: string } = {
  name: "Minwoo Jeong",
};
```
