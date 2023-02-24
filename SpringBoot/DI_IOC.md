# Spring boot

- 스프링 부트
- 스프링 클라우드 
- 스프링 데이터
- 스프링 배치 
- 스프링 시큐리티(권한 관련)

-----------

## AOP
 >스프링 데이터, 트랜잭션 관리, AOP를 통해서 로깅

## 객체 
>이식 가능한 추상화, 관전 중심 프로그램, 의존 관계 주입 


## IOC/DI
### IOC==제어의 역전 
>- spring container에 만들어져서 들어가있음 -> 싱글톤 
>- 프레임워크가 객체를 관리함

2023.02.23
### DI: 외부에서 사용하고 있는 객체를 상속시켜서 주입시켜줌. 
>- 객체를 사용하기 위한 것 
>- 제어의 역전이 일어남 
>- 의존성: 코드 테스트에 용이함 
>- Mock -> 안정적으로 테스트가 가능함 
>- Mocking: 어떠한 응답이 올거라는 기대값 
>- 코드 변경할때 영향 취소화(추상화)
>- 순환참조를 막음: 객체1 객체2 서로 참조 안함. 

```JAVA
Encoder encoder = new Encoder(new Base64Encoder());
String result = encoder.encode(url);
```
-> 주입 객체 `new Base64Encoder()` 만 바꿔줌 
> - 만약 Base64Encoder() 라는 객체 대신 다른 객체를 사용하고 싶으면 new Base64Encoder()대신 사용하고 싶은 객체를 주입해주면 됨. 여기서 Base64Encoder()는 외부에서 사용하고 있던 객체임. 
> - 테스트할때 Encoder는 바꿔줄 필요가 없음. 테스트할때는 DI 부분의 객체만 넣어서 테스트를 할 수 있음 -> 테스트할때 편할 것 같음 !! 굳이 코드 안바꾸고 테스트 객체 하나 더 만들면 되니까 
> - 코드의 관리가 쉬울듯! 
>

Interface 추가 전 
```JAVA
Encoder encoder = new Encoder();
String result = encoder.encode(url);
```

Interface 추가 
```JAVA
 IEncoder encoder = new Base64Encoder();
 String result = encoder.encode(url);

 IEncoder urlEncoder = new UrlEncoder();
 String urlResult = urlEncoder.encode(url);

```
->Interface 추가해주는 이유: Interface를 추가하기 전에는 계속해서 객체를 생성해줘야 하는 문제가 있었음. 

------

2023.02.24
IOC 