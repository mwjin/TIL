---
layout: default
title: Aliasing
parent: Type
grand_parent: Typescript
nav_order: 2
---

# Aliasing

## Concept

다음과 같이 같은 type의 두 object가 있다고 하자.

```typescript
const player1: {
  name: string;
} = {
  name: "Minwoo Jeong",
};

const player2: {
  name: string;
} = {
  name: "Minho Jeong",
};
```

위와 같이 명시할 type이 길어지는 경우 매번 type을 치기 번거롭다. 이를 위해 Typescript에서는 **aliasing**을 지원한다.

```typescript
type Player = { name: string };

const player1: Player = { name: "Minwoo Jeong" };
const player2: Player = { name: "Minho Jeong" };
```

모든 type에 대해서 aliasing을 할 수 있다.

```typescript
type Age = number;
type Name = string;
```

## Index Signature

Object의 type을 aliasing 할 때 key로 들어올 값은 정해져 있지 않지만 type은 정해져 있는 경우 다음과 같이 명시할 수 있다.

```typescript
type Player = { [key: string]: string };

const player: Player = {};
player.a = "a";
player["b"] = "b";
player[1] = "c"; // Error
```
