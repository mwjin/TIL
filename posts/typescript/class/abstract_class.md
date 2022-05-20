---
layout: default
title: Abstract Class
parent: Class
grand_parent: Typescript
nav_order: 2
---

# Abstract Class

Abstract class는 상속이 가능한 대신 인스턴스화가 불가능하다는 특징을 가지며 다음과 같이 정의한다.

```typescript
abstract class User {
  constructor(
    private firstName: string,
    private lastName: string,
    protected nickname: string
  ) {}
  getFullName() {
    return `${this.firstName} ${this.lastName}`;
  }
  private getFullNameInternal() {
    return `${this.firstName} ${this.lastName}`;
  }
  // abstract method (only declared with a call signature)
  // must not be implemented
  abstract getNickName(): string;
}
```

위의 `getNickName`과 같이 _abstract class_ 내에 `abstract` 키워드와 함께 오직 *call signature*만으로 선언되는 메소드를 **abstract method**라고 한다.

Abstract class를 상속받은 클래스는 반드시 abstract method를 구현해야 한다.

```typescript
class Player extends User {
  // Must be implemented
  getNickName() {
    return this.nickname;
  }
}
```

_(p.s. `nickname`에 접근이 가능한 이유는 해당 속성이 `protected`이기 때문이다.)_

`Player`는 인스턴스를 생성할 수 있는 반면, `User`는 안된다.

```typescript
const minwoo = new Player("Minwoo", "Jeong", "minu");
const user = new User("Minwoo", "Jeong", "minu"); // Error!
```
