# VPC
[youtube강의](https://www.youtube.com/watch?v=FeYagEibtPE)

## Bastion Host
- private ec2 인스턴스와 private ec2인스턴스에서 점프를(?)바로 갈 수 있게 해주는 것 

# 1. VPC란?
- 가상 네트워크 센터, 네트워크를 구성하는 센터 

|Default VPC|Custom VPC|
|---|---|
|- 계정 생성시 자동으로 셋업 되어 있음(모든 리전에)<br> - 모든 서브넷의 인터넷 접근이 가능함 <br> - EC2가 퍼블릭 IP와 Private IP 모두 가지고 있음 <br> - 삭제시 복구 불가| - 새로 만들어야 함<br> - Default VPC의 특징을 가지고 있지 않음 |
|테스트3|테스트3|
