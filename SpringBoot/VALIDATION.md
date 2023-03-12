# Validation

[BeanValidation](https://beanvalidation.org/)
> - 서비스 로직과의 분리 필요 
> - 일관된 validation으로 정리해야 함.
>> @Size, @NotNull, @NotEmpty, @NotBlank, @Past, @PastOrPresent, @Future, @FutureOrPresent, @Pattern, @Max, @Min, @AssertTrue, @AssertFalse, @Valid
> - 모든 annotation에는 message를 추가해줄 수 있음. 


- ## Custom validation
> - @AssertTrue, @ConstraintValidator



- ## Annotation 만들기 

- @NotBlank 어노테이션을 붙혀줘도 작동이 안되는 이유는 -> 무조건 @Valid 어노테이션을 붙혀줘야 검사를 하게 됨. 



- ## 예외처리하기 
> - @ControllerAdvice, @ExceptionHandler
> - RequestParam(required = false): 해당값이 입력되지 않아도 실행됨. 



