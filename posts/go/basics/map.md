---
layout: default
title: Map
parent: Basics
grand_parent: Go
nav_order: 14
---

# Map

## Basic

- *Key*와 *value*의 형태로 데이터를 저장하는 자료구조
- 다른 언어의 _hash map_, _hash table_ 등에 해당
- 키 값을 이용해 이에 대응하는 값을 가져올 수 있다.

## Syntax

### 생성

```go
make(map[key]value)
```

_e.g._

```go
m := make(map[int]string)
m[1] = "abc"
m[3] = "def"
m[5] = "ghi"
fmt.Println(m) // map[1:abc 3:def 5:ghi]
```

또는 다음과 같이 정의도 가능하다.

```go
m := map[int]string {
    1: "abc",
    3: "def",
    5: "ghi",
}
```

### Loop

```go
for k, v := range m {
    fmt.Println(k, v)
}
```

### Delete

```go
delete(m, key)
```

존재하지 않는 key 값으로 delete를 시도하는 경우 아무 일도 발생하지 않는다.

### Key 존재 여부 확인

```go
v, ok := m[key]
```

- 위의 `ok`는 boolean 값으로, 키에 대응하는 값이 존재하는 경우 `true`이다.
- 위 문법을 활용하여 특정 key가 존재할 때만 동작하는 조건문을 작성할 수 있다.

_e.g._

```go
if _, ok := m[key]; ok {
    ...
}
```
