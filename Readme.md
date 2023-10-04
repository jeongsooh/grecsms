## charging profile
{
  "conectorId": 1,
  "idTag": "000000001500495E",
  "chargingProfile": {
    "chargingProfileId": 1,
    "transactionId": 1,
    "stackLevel": 1,
    "chargingProfilePurpose": "TxDefaultProfile", // ChargePointMaxProfile, TxDefaultProfile, TxProfile
    "chargingProfileKind": "Absolute", // Absolute, Recurring, Relative
    "recurrencyKind": "Daily", // Daily, Weekly
    "validFrom": DateTime[0....1],
    "validTo": DateTime[0....1],
    "chargingSchedule": {
      "duration": 0,
      "startSchedule": DateTime[0...1],
      "chargingRateUnit": "W",  // "W", "A"
      "chargingSchedulePeriod: [
        {
          "startPeriod": 1,
          "limit": 1000,
          "numberPhases": 1,
        },
        {
          "startPeriod": 2,
          "limit": 2000,
          "numberPhases": 1,
        },
      ],
      "minChargingRate": decimal,
    }
  }
}

### csChargingProfiles 예시
{
  'connectorId': 1, 
  'csChargingProfiles': {
    'chargingProfileId': 1, 
    'stackLevel': 1, 
    'chargingProfilePurpose': 'TxProfile', 
    'chargingProfileKind': 'Absolute', 
    'chargingSchedule': {
      'duration': 10000, 
      'chargingRateUnit': 'W', 
      'chargingSchedulePeriod': [
        {'startPeriod': 1, 'limit': 8.1},
        {'startPeriod': 1000, 'limit': 7000}
      ]
    }
  }
}

## GetConfiguration sample
### 모든 configuration을 얻고 싶으면 Null 값 전송 {}
### 특정 값을 얻고 싶으면 아래와 같이 리스트에 넣어서 전송
{"key": ["MeterValueSampleInterval", "ClockAlignedDataInterval"]}

## ChangeConfiguration sample
{
  'key': 'MeterValueSampleInterval',
  'value': 0
}
{
  "key": "ClockAlignedDataInterval",
  "value": "1500"
}

## ClearChargingProfile: 모든 값이 option이므로 다양하게 사용 가능
{
  'id': 1,
  'connectorId': 1,
  'chargingProfilePurpose': 'TxProfile',
  'stackLevel': 1
}

### ClearChargingProfile sample
{
  'connectorId': 1, 
  'id': 1
}

## GetCompositeSchedule
{
  'connectorId': 1,     // required
  'duration': 1000      // required. time in seconds
}

### GetCompositeSchedule sample
{
  'connectorId': 1, 
  'duration': 1000
}

## 23/09/14 HeartHeat 받으면 Active 충전기 정상 및 시간 기록
- cpstatus에 "정상" 입력하고 확인시간 기록 -> 시간 field 추가
- 5분에 한번씩 task 설정
- "정상"인 cp에 대해서 마지막 확인시간과 현재시간이 600초 이상이면 "통신장애" 기록
- "통신장애"인 cp에 대해서 마지막 확인시간과 현재시간이 3600초(1시간) 이상이면 "충전기장애" 기록

## 전체 application  구동 방법
- 첫번째 터미날
``````
$ python manage.py runserver
``````
- 두번째 터미날
``````
$ celery -A ocpp_svr worker -l INFO -P gevent
``````
- 세번째 터미날
``````
$ celery -A ocpp_svr beat -l INFO
``````

## 230919 - dashboard 작성