---
layout: default
title: Types of TS
parent: Type
grand_parent: Typescript
nav_order: 3
---

# Types of TS

본 문서에서는 Typescript 특이적인 type에 대해 소개한다.

## Optional

- Optional하게 사용되는 variable을 명시할 때 사용.
- Type에 자동으로 `| undefined` 를 추가해준다.
- **Syntax:** `variable?: T`
- 주로 optional한 object attribute나 함수 파라미터를 명시할 때 사용한다.
- 예시

  - Optional property

  ```typescript
  type Player = {
    name: string;
    age?: number;
  };
  const player1: Player = { name: "Minwoo Jeong" };
  const player2: Player = { name: "Minwoo Jeong", age: 24 };
  ```

  - Optional function parameter

  ```typescript
  function func(a?: number) {
    if (a) console.log(a);
    else console.log("Undefined!");
  }
  ```

## Tuple

정해진 개수의, 정해진 순서와 타입을 가진 Array라고 생각하자.

```typescript
const t: [string, number, boolean] = ["Minwoo Jeong", 1, true];
```

## Readonly

- 오직 읽기만 가능하도록 하는 제어자.
- Composite data type의 element들에 대해 read-only 속성을 부여
- 다음의 경우에만 `readonly` 키워드가 허용되는 것으로 보인다.

  - Read-only property

    ```typescript
    type Player = {
      readonly name: Name;
      age?: Age;
    };

    const minwoo: Player = { name: "Minwoo Jeong" };
    minwoo.name = "Minho"; // Not allowed
    ```

  - Read-only array

    ```typescript
    const numbers: readonly number[] = [1, 2, 3, 4];
    numbers.push(5); // Not allowed
    ```

  - Read-only tuple

    ```typescript
    const t: readonly [string, number, boolean] = ["Minwoo Jeong", 1, true];
    t[0] = "Minho"; // Not allowed
    ```

  - Class property

    ```typescript
    class Word {
      constructor(public readonly term: string, public readonly def: string) {}
    }
    const kimchi = new Word("Kimchi", "Korean Food");
    kimchi.def = "xxx"; // not allowed
    ```

## Any

- Type checking으로부터 벗어나기 위해 사용하는 Type
- Javascript와 동일하게 동작한다.
- **Typescript를 사용하는 이점이 없어지므로 추천하지 않는다.**

```typescript
const a: any[] = [1, 2, 3, 4];
const b: any = true;
a + b; // Allowed like Javascript
```

## Unknown

- 어떤 type이 설정될 지 알 수 없을 때 사용한다.
- Type checker로부터 일종의 보호를 받게 된다.
  ```typescript
  let a: unknown;
  let b = a + 1; // Error
  ```
- **사용 전에 반드시 type check를 해줘야 한다.**

  ```typescript
  let a: unknown;

  if (typeof a === "number") {
    let b = a + 1;
  }
  if (typeof a === "string") {
    let b = a.toUpperCase();
  }
  ```

## Void

- 아무것도 return하지 않는 함수의 return type

```typescript
function hello() {
  console.log(1);
}
```

## Never

- 함수가 절대 return 하지 않을 때 사용된다.

  ```typescript
  function hello(): never {
    throw new Error("xxx");
  }
  ```

- 또는 type check를 위한 `if-else` 문에서, 실행될 리 없는 block에서 해당 변수의 type을 가리킬 때 사용된다.

  ```typescript
  function hello(name: string | number) {
    if (typeof name === "string") {
        ...
    } else if (typeof name === "number") {
        ...
    } else {
        name; // never
    }
  }
  ```
