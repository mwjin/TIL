---
layout: default
title: Overloading
parent: Function
grand_parent: Typescript
nav_order: 2
---

# Overloading

## Concept

- Multiple Call Signature를 가지고 있을 때 발생

```typescript
type Add = {
  (a: number, b: number): number;
  (a: number, b: string): number;
};

const add: Add = (a, b) => {
  if (typeof b === "string") return a;
  return a + b;
};
```

- 위 예시에서 `b`의 타입은 `number | string` 이다.
- 외부 패키지에서는 overloading 기법을 많이 사용한다.

## Examples

### Example 1

```typescript
type Config = {
  path: string;
  state: object;
};

type Push = {
  (path: string): void;
  (config: Config): void;
};

const push: Push = (config) => {
  if (typeof config === "string") {
    console.log(config);
  } else console.log(config.path);
};
```

- `typeof` 키워드를 통해 type checker는 `config`의 타입을 확실하게 알 수 있다.

### Example 2

Parameter 개수가 다른 경우

```typescript
type Add = {
  (a: number, b: number): number;
  (a: number, b: number, c: number): number;
};

// Not working!
const add: Add = (a, b, c) => {
  return a + b;
};
```

- `c`는 기본적으로 `Optional`이다.
- 다음과 같이 정의해야 한다.

```typescript
const add: Add = (a, b, c?: number) => {
  if (c) return a + b + c;
  return a + b;
};

add(1, 2);
add(1, 2, 3);
```
