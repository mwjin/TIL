---
layout: default
title: Interface
parent: Class
grand_parent: Typescript
nav_order: 3
---

# Interface

## `type` keyword

`type` keyword는 다음과 같은 용도로 사용된다.

- **Type aliasing**

  ```typescript
  type Nickname = string;
  type Health = number;
  type Friends = Array<string>;
  ```

- *Object*의 모양을 결정하기 위해 사용

  ```typescript
  type Player = {
    nickname: Nickname;
    healthBar: Health;
  };
  const minwoo: Player = {
    nickname: "Jin",
    healthBar: 10,
  };
  ``;
  ```

- 특정 type에 속할 수 있는 값을 한정짓기 위해 사용

  ```typescript
  // Specify values
  type Team = "read" | "blue" | "yellow";

  type Player = {
    nickname: string;
    team: Team;
    health: Health;
  };

  const minwoo2: Player = {
    nickname: "Jin",
    team: "yellow",
    health: 10,
  };
  ```

## `interface`

Typescript의 `interface`는 `type`와 유사하게 *object*의 모양을 특정하기 위한 용도로 사용된다. 그러나 `type`과 달리 아래와 같은 특징을 가진다.

- Inheritance

  ```typescript
  interface User {
    name: string;
  }
  interface Player extends User {}

  const minwoo3: Player = {
    name: "Minwoo Jeong",
  };
  ```

- Cumulate properties

  ```typescript
  interface User {
    name: string;
  }

  interface User {
    lastName: number;
  }

  interface User {
    health: Health;
  }

  const minwoo: User = {
    name: "Minwoo",
    lastName: "Jeong",
    health: 10,
  };
  ```

- `extends` keyword

  ```typescript
  interface PlayerB {
    name: string;
  }
  interface PlayerBB extends PlayerB {
    lastName: string;
  }
  ```

- `implements` keyword를 통해 특정 class가 interface의 property와 method들을 정의하도록 강제

  ```typescript
  interface User {
    firstName: string;
    lastName: string;
    sayHi(name: string): string;
    fullName(): string;
  }
  interface Human {
    health: number;
  }

  class Player implements User, Human {
    constructor(
      public firstName: string,
      public lastName: string,
      public health: number
    ) {}
    fullName() {
      return `${this.firstName} ${this.lastName}`;
    }
    sayHi(name: string) {
      return `Hello, ${name}! My name is ${this.fullName()}`;
    }
  }
  ```

  위와 같이 interface로부터 property 혹은 method를 승계받는 경우 접근자는 `public`이어야 한다.

## `Type` vs. `Interface`

- 다음 두 가지 방식 모두 **object의 형태를 특정하기 위한 용도**로 사용된다.

  ```typescript
  type User = {
    firstName: string;
    lastName: string;
    sayHi(name: string): string;
    fullName(): string;
  };

  interface User {
    firstName: string;
    lastName: string;
    sayHi(name: string): string;
    fullName(): string;
  }
  ```

- 두 가지 모두 경우 아래와 같이 parameter 또는 return value의 type으로 사용될 수 있다. 이 때 `new User(...)`와 같은 키워드는 사용하지 않는다.

  ```typescript
  function makeUser(user: User): User {
    return {
      firstName: "Minwoo",
      lastName: "Jeong",
      fullName: () => "xx",
      sayHi: (name) => "string",
    };
  }

  makeUser({
    firstName: "Minwoo",
    lastName: "Jeong",
    fullName: () => "xx",
    sayHi: (name) => "string",
  });
  ```

- 두 가지 경우 모두 JS로 컴파일 시 사라진다.
- `interface`가 객체 지향 프로그래밍을 하기에는 더 적합하다.
- 일반적으로 object의 형태를 한정짓기 위한 용도로는 `interface`가 더 선호되는 편이다.
