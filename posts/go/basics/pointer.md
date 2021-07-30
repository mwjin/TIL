---
layout: default
title: Pointer
parent: Basics
grand_parent: Go
nav_order: 8
---

# Pointer

## Basics

- **Pointer**란 특정 type의 instance에 대한 *메모리 주소를 값으로 하는 변수*를 의미한다.
  - **Instance**: 메모리에 존재하는 데이터의 실체
- 기본적인 특징은 C의 포인터와 같다.
  - 대표적으로 _Call by Reference_

## Usage

- 다음과 같이 정의한다.
  ```go
  var p *T  // T: type
  ```
- 일반적인 경우 다음과 같이 할당한다.

  ```go
  var v T
  var p *T = &T

  // Or
  p := &v

  // Or
  p := new(T)
  ```

- Struct에 대한 포인터는 같은 경우 다음과 같이 정의할 수 있다.

  ```go
  type Data struct {
    value int
    data [200]int
  }

  var v Data
  p := &v

  // Or
  p := new(Data)

  // Or
  p := &Data{}
  ```

- `&Data{}` 와 같은 경우는 `{}`내에 초기값 설정이 가능하다.
  - e.g. `&Data{3, {1, 2}}`
