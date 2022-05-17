---
layout: default
title: Generic
parent: Function
grand_parent: Typescript
nav_order: 4
---

# Generic

## 설명

- Type에 대한 Placeholder로, 유저가 원하는 type을 typescript가 알아서 생성하도록 한다.
- Typescript의 *Type Checker*에게 type 추론을 맡긴다.
- 다음 두 요소를 통해 type을 추론한다.
  - Generic을 첫 번째로 인지하는 시점의 type
  - Generic의 순서
- _Concrete Type_ (e.g. `number`, `boolean`, etc.) 을 명확히 알지 못할 때 사용한다.
- `<T>`는 generic을 사용하겠다는 표시이다.

## 예시

- Type aliasing을 사용하고 있는 경우

  ```typescript
  type SuperPrint = {
    <T>(arr: T[]): void;
  };

  const superPrint: SuperPrint = (arr) => {
    arr.forEach((i) => console.log(i));
  };

  superPrint([1, 2, 3]);
  superPrint([true, false]);
  superPrint(["a", "b", "c"]);
  superPrint(["a", "b", true, false]);
  ```

- Return type까지 사용하고 싶을 때

  ```typescript
  type ReturnFirst = {
    <T>(arr: T[]): T;
  };

  const returnFirst: ReturnFirst = (arr) => arr[0];

  returnFirst([1, 2, 3]);
  returnFirst(["a", "b", true, false]); // Return type: string | boolean
  ```

- 두 가지의 generic을 사용

  ```typescript
  type PrintTwo = {
    <T, V>(a: T, b: V): void;
  };

  const printTwo: PrintTwo = (a, b) => {
    console.log(a, b);
  };

  printTwo(1, 2);
  printTwo("a", 1);
  printTwo("a", null);
  ```

## vs. Any

- Generic은 *type checker에게 type 지정을 위임한 것*이고 any는 아예 *type을 지정하지 않는 것*이다.
- 다음과 같은 상황에서 차이가 있다.

```typescript
const a = returnFirst(["a", "b", true, false]);
const b = a + 1; // Error if you use generic
```

- `a`는 generic을 사용하는 경우 `string | boolean`으로 인식된다.
- `string | boolean`은 `number`와 연산할 수 없다.
- `any`라면 위와 같은 연산이 가능하다.

## In Practice

- 일반적으로 라이브러리를 정의할 때 주로 generic을 사용한다.
- 라이브러리를 사용하는 입장이라면 generic을 직접 정의하기보다는 사용하는 경우가 많을 것이다.
- 다음과 같은 형태로 자주 사용된다.

### Function Declaration

```typescript
function superPrint<V>(arr: V[]) {
  arr.forEach((i) => console.log(i));
}

// Usually it is recommend to allow typescript to infer the types
superPrint([1, 2, 3]);
superPrint([true, false]);
superPrint(["a", "b", "c"]);
superPrint(["a", "b", true, false]);

superPrint<number>([1, 2, 3]); // working
superPrint<boolean>([1, 2, 3]); // not working
```

Typescript에게 type 추론을 맡기는 것을 추천한다.

### Object

```typescript
type Player<E> = {
  name: string;
  extraInfo: E;
};

type MinwooExtra = {
  favFood: string;
};

type MinwooPlayer = Player<MinwooExtra>;

const minwoo: MinwooPlayer = {
  name: "Minwoo Jeong",
  extraInfo: {
    favFood: "Kimchi",
  },
};

const other: Player<null> = {
  name: "Other",
  extraInfo: null,
};
```

### Array

```typescript
type A = Array<number>;
let a: A = [1, 2, 3, 4];
```
