---
layout: default
title: Constructor
parent: Basics
grand_parent: C++
nav_order: 1
---
# Constructor
## 배경
다음과 같이 정의된 클래스가 있다고 하자.
```cpp
class Date {
    int year;
    int month;
    int day;
public:
    void SetDate(int year_, int month_, int day_);
}
```
그리고 다음과 같이 Date 클래스의 객체를 생성했다고 하자.
```cpp
Date date;
```
위의 경우 date의 year, month와 같은 속성값이 어떤 값으로 정의되어 있는지 확신할 수 없다는 문제가 있다. 속성값을 명시적으로 정의하기 위해 ``SetDate``를 정의하였으나, 이와 같이 객체를 생성할 때마다 ``SetDate``를 호출하는 것은 매우 번거로운 일일 것이다.

이 번거로움을 클래스의 **생성자 (Constructor)**로 해결할 수 있다.

## 생성자 기초
* 생성자란 특정 클래스의 객체 생성 시 자동으로 호출되는 함수이다.
* 자동으로 호출되어 객체의 속성값을 초기화한다.
* 정의 시 별도의 return 값을 명시하지 않는다.
* 예시
```cpp
// 클래스 내부에서 정의 시
public:
    Date(int year_, int month_, int day_) {
        ...
    }

// 클래스 외부에서 정의 시
Date::Date(int year_, int month_, int day_) {
    ...
}
```
* 생성자가 정의되어 있다면 명시된 생성자 형태로 밖에 호출이 불가하다.
  * 즉 위와 같이 정의된 경우 ``Date date;`` 와 같이 객체 생성 불가.
* 사용 방법
```cpp
Date day1(2021, 6, 28);  // 암시적 방법
Date day2 = Date(2021, 6, 28);  // 명시적 방법
```

## 디폴트 생성자
* 인자를 받지 않는 생성자.
* 명시적 또는 암묵적인 방법으로 정의할 수 있다.
* 다음과 같이 정의 (명시적)
```cpp
// 클래스 내부에서 정의 시
public:
    Date() {
        ...
    }

// 클래스 외부에서 정의 시
Date::Date() {
    ...
}
```
* 아무런 생성자가 정의되어 있지 않다면 컴파일러가 암묵적으로 디폴트 생성자를 정의한다.
  * 때문에 위에서 ``Date date;`` 와 같은 방법으로 객체 생성이 가능.

* C++ 11을 기점으로, 다른 생성자가 이미 정의되어 있더라도 다음과 같이 명시하면 컴파일러가 정의한 디폴트 생성자를 사용할 수 있다.
```C++
public:
    Date() = default;
```
* 사용 방법
```cpp
Date day1;  // 암시적 방법
Date day2 = Date();  // 명시적 방법
Date day3();  // 이와 같은 방법으로 사용 불가 (함수를 정의한 것으로 인식)
```

## 생성자 오버로딩
* 한 클래스에 여러 형태의 생성자를 정의할 수 있다.
* 실제로 사용할 때는 사용하는 형태에 맞는 생성자를 찾아 이를 호출한다.
* 함수 오버로딩과 비슷.
