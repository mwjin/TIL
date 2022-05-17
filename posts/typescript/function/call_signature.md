---
layout: default
title: Call Signature
parent: Function
grand_parent: Typescript
nav_order: 1
---

# Call Signature

## Recap

두 가지 함수 작성 방식이 있다.

```typescript
// Function Declaration
function add(a: number, b: number): number {
  return a + b;
}

// Arrow Function
const add2 = (a: number, b: number): number => a + b;
```

혹은 다음과 같이 return 값에 대한 추론이 가능한 경우 return type을 생략해도 된다.

```typescript
// Function Declaration
function add(a: number, b: number) {
  return a + b;
}

// Arrow Function
const add2 = (a: number, b: number) => a + b;
```

인자에 type을 명시하지 않으면 `any` type이 됨에 주의.

## Call Signature

- _Type of Function_
- Call signature를 이용해 function의 type도 별도의 type aliasing을 할 수 있다.

```typescript
type Add = (a: number, b: number) => number; // Call Signature

const add: Add = (a, b) => a + b;
const add2: Add = (c, d) => c + d; // Legal
const add3: Add = (a: boolean, b) => a + b; // Illegal
const add4: Add = (a, b) => {
  a, b;
}; // Illegal
```

- `add3`는 인자의 type이 `boolean`으로 `Add` 와 incompatible하다.
- `add4`는 return type이 `void`으로 `Add` 와 incompatible하다.
