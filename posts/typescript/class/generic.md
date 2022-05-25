---
layout: default
title: Generic
parent: Class
grand_parent: Typescript
nav_order: 4
---

# Generic

## Background

- **Polymorphism**: 한 클래스가 여러 형태로 이용될 수 있다.
- *Generic*은 polymorphism을 구현할 수 있는 방법 중 하나이다.
- 개념 자체는 function에서의 generic과 동일하다.

## Syntax

다음과 같이 작성한다.

```typescript
interface MyStorage<T> {
  [key: string]: T;
}

class LocalStorage<T> {
  private storage: MyStorage<T> = {};
  set(key: string, value: T) {
    this.storage[key] = value;
  }
  remote(key: string) {
    if (this.storage[key] !== undefined) {
      delete this.storage[key];
    }
  }
  get(key: string): T {
    return this.storage[key];
  }
  clear() {
    this.storage = {};
  }
}

const stringStorage = new LocalStorage<string>();
```

- `<T>`: type에 대한 placeholder
- Placeholder로 넘겨 받은 type은 내부에서 사용하고 있는 또 다른 generic으로 넘겨줄 수 있다.
  - _e.g._ `LocalStorage` -> `MyStorage`

## Usage

다음과 같이 한 클래스를 여러 형태로 사용할 수 있다.

```typescript
const stringStorage = new LocalStorage<string>();

stringStorage.get("key");
stringStorage.set("hello", "world");

const booleanStorage = new LocalStorage<boolean>();

booleanStorage.get("key");
booleanStorage.set("tired", true);
```

명시해 준 타입에 맞게 function call signature는 자동으로 설정된다.
_e.g._ `stringStorage.get("key");` -> `LocalStorage<string>.get(key: string): string`
