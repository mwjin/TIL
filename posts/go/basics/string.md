---
layout: default
title: String
parent: Basics
grand_parent: Go
nav_order: 11
---

# String

## Basics

- 일련의 문자 집합
- `"` 또는 `` ` ``를 이용해 표현할 수 있다.
- `` ` ``로 감싸져 있는 경우 문자열 안의 특수 문자가 일반 문자로 처리되며 여러 줄에 걸쳐서 문자열을 쓸 수 있다.
- 예시

  ```go
  str1 := "Hello,\tworld!"  // Hello, world! 출력
  str2 := `Hello,\tworld!`  // Hello,\tworld! 출력
  ```

  ```go
  // Hello,
  // world! 출력
  str := `Hello,
  world!`
  ```

- **UTF-8**을 표준 문자 코드로 사용
- `len()`을 통해 문자열 byte 크기를 할 수 있다.
- `string`과 `[]byte` 타입 간 상호 변환이 가능하다.

## `rune`

- 한 글자가 1 byte 보다 큰 문자까지 용이하게 표현하기 위해 `rune`이라는 타입을 사용한다.
  ```
  type rune int32
  ```
- `string`과 `[]rune` 타입은 상호 변환이 가능하다.
- 한글과 같이 한 글자가 1 byte보다 큰 문자들까지 고려하여 글자 수를 세야 할 때 용이하다.
  ```go
  str := "Hello 월드"  // len(str) => 12
  runes := []runes(str)  // len(runes) => 8
  ```

## 문자열 순회하기

크게 3가지 방법이 있다.

### 인덱스를 이용한 byte 단위 순회

```go
for i := 0; i < len(str); i++ {
    ...
}
```

- 한 글자가 1 byte 이상인 문자를 포함하고 있는 문자열의 경우 위와 같은 방식으로 접근 시 **글자가 깨져보일 수 있다.**

### `[]rune` 타입으로 변환 후 한 글자씩 순회

```go
str := ...
arr := []rune(str)

for i := 0; i < len(arr); i++ {
    ...
}
```

- 위와 같이 하면 1 byte 보다 큰 글자라도 깨짐없이 읽을 수 있다.
- 글자 당 4 byte를 할당하므로 **불필요한 메모리를 잡아먹는다는 것이 단점**

### `range`를 통해 한 글자씩 순회

```go
for _, v := range str {
    ...
}
```

- 위 두 순회 방식의 문제점을 모두 해결한 방법인 것처럼 보인다.
- `v`의 type은 `rune`이다.

## 문자열 연산

### Concatenation

`+` 연산을 이용한다.

```go
str1 := "Hello, "
str2 := "world!"
str3 := str1 + str2 // Hello, world!
```

### 비교 연산

- `==`, `!=` 연산
  - `==`은 두 문자열이 길이 포함 완전히 일치하는 경우 true
  - `!=`는 `==`의 반대
- `<`, `<=`, `>`, `>=` 연산
  - 글자 단위로 비교하여 대소 관계를 파악
  - 비교하는 글자들이 같은 글자인 경우 그 다음 글자의 대소 관계를 비교
  - 글자의 값은 ASCII 코드 참조

## String 내부 구조

- `reflect` 패키지 내의 `StringHeader` 구조체를 통해 내부 구조 유추

```go
type StringHeader struct {
    Data uintptr
    Len int
}
```

- string끼리 대입할 때

```go
str1 := "Hello, world!"
str2 := str1
```

- `StringHeader` 구조체 크기만큼의 메모리 공간이 추가적으로 할당
- 내부 포인터와 길이 값을 복사
- **`str1`, `str2` 모두 같은 문자열을 가리킴**

  ```go
  str1 := "Hello, world!"
  str2 := str1

  // 두 header 구조체의 내부 값이 동일
  header1 := (*reflect.StringHeader)(unsafe.Pointer(&str1))
  header2 := (*reflect.StringHeader)(unsafe.Pointer(&str2))
  ```

## Immutability

### Concept

- **문자열은 불변이다.**
  ```go
  str := "Hello, world!"
  str[2] = 'a'  // Error!
  ```
- `[]byte`로 형변환 후 값을 바꾸더라도 기존의 문자열은 바뀌지 않는다. 이는 형변환 결과물이 별도의 메모리 공간에 저장되기 때문이다.

### String concatenation

- String concatenation 수행 시에도 그 결과물은 별도의 메모리 공간에 저장된다.
- 빈번한 concatenation 시 위 문제 때문에 많은 메모리 공간을 잡아먹게 된다. 이를 방지하기 위해 `strings` 패키지의 `Builder`를 사용한다.

  ```go
  // 소문자를 대문자로 변환하는 예시
  func ToUpper(str string) string {
      var builder strings.Builder
      for _, c := range str {
          if c >= 'a' && c <= 'z' {
              builder.WriteRune('A' + c - 'a')
          } else {
              builder.WriteRune(c)
          }
      }
      return builder.String()
  }

  ```

- **빈번한 string concatenation 시 `strings.Builder`를 사용하자.**
