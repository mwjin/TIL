---
layout: default
title: Basic
parent: Class
grand_parent: Typescript
nav_order: 1
---

# Basic

## Syntax

Typescript에서 클래스는 다음과 같이 정의한다.

```typescript
class Player {
  constructor(
    private firstName: string,
    private lastName: string,
    public nickname: string
  ) {}
  getFullName() {
    return `${this.firstName} ${this.lastName}`;
  }
}
```

이는 Javascript에서 다음 문법과 동일하다.

```javascript
class Player {
  constructor(firstName, lastName, nickname) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.nickname = nickname;
  }
  getFullName() {
    return `${this.firstName} ${this.lastName}`;
  }
}
```

차이점은 다음과 같다.

- Typescript에서는 constructor 내부를 정의할 필요가 없다.
- `public`, `protected`, `private`과 같은 접근 제어자(_Access Modifier_)가 존재한다.

다음 `fullName`과 같이 constructor의 인자로 넘겨받지 않고 constructor 밖에서 선언한 뒤 constructor 구현부 내에서 정의하는 방법도 있다.

```typescript
class Player {
  public fullName: string;
  constructor(
    private firstName: string,
    private lastName: string,
    public nickname: string
  ) {
    this.fullName = `${firstName} ${lastName}`;
  }
}
```

constructor 외부에서 선언하는 경우 반드시 initialize를 해주어야 한다.

## Access Modifier

외부에서 특정 클래스의 맴버 변수 또는 메소드에 접근하는 것을 제어하기 위한 키워드들이며 `public`, `protected`, `private`가 있다.

```typescript
class Player {
  constructor(
    private firstName: string,
    private lastName: string,
    public nickname: string
  ) {}

  // 메소드는 다음과 같이 제어한다.
  private getFullName() {
    return `${this.firstName} ${this.lastName}`;
  }
}
```

각 접근 제어자에 대한 설명은 다음과 같다.

- `public`: 접근에 제한이 없다. 아무런 명시도 되어 있지 않을 때 해당 제어자로 설정된다.
- `protected`: 소속되어 있는 클래스 내부 또는 자식 클래스들의 내부에서 접근 가능하다.
- `private`: 오직 소속되어 있는 클래스 내에서만 접근 가능하다.

## Class as a Type

클래스는 다음 `Word`와 같이 type을 명시하기 위한 용도로 사용될 수 있다.

```typescript
class Word {
  constructor(public term: string, public def: string) {}
}

class Dict {
  private words: Words;
  constructor() {
    this.words = {};
  }
  // class can be used as a type
  add(word: Word) {
    if (this.words[word.term] === undefined) {
      this.words[word.term] = word.def;
    }
  }
}
```
