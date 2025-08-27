# ================================================================
# [모듈 임포트]
# ================================================================
# 이 프로그램은 'Mission Computer'라는 가상 시스템을 시뮬레이션한다.
# - platform: OS, CPU 정보 조회
# - psutil  : CPU, 메모리 등 자원 사용량 측정
# - json     : 출력 데이터를 JSON 형식으로 변환
# - time     : 일정 시간 간격을 두고 반복 실행
# - threading: 멀티스레드 동시 실행 지원
# - multiprocessing: 멀티프로세스 동시 실행 지원
# - random   : 더미 센서 데이터 생성을 위해 난수 활용
import platform
import psutil
import json
import time
import threading
import multiprocessing
import random


# ================================================================
# [DummySensor 클래스]
# ================================================================
# - 가상의 '환경 센서' 역할을 한다.
# - 실제 센서에서 데이터를 가져오는 대신, 무작위(random) 값을 생성한다.
# - 이런 방식은 소프트웨어 개발에서 '테스트 시뮬레이션' 용도로 자주 사용된다.
# ================================================================
class DummySensor:
    """
    화성 기지(Mars Base)의 환경 데이터를 모사하는 더미 센서 클래스
    """

    def __init__(self):
        # 센서 데이터는 딕셔너리(Dictionary)로 관리한다.
        # 미리 측정 항목들을 정의하고, 초기값은 0.0으로 둔다.
        self.env_values = {
            'mars_base_internal_temperature': 0.0,   # 내부 온도 (°C)
            'mars_base_external_temperature': 0.0,   # 외부 온도 (°C)
            'mars_base_internal_humidity': 0.0,      # 내부 습도 (%)
            'mars_base_external_illuminance': 0.0,   # 외부 조도 (lux)
            'mars_base_internal_co2': 0.0,           # 내부 CO2 농도 (%)
            'mars_base_internal_oxygen': 0.0         # 내부 산소 농도 (%)
        }

    def set_env(self):
        """
        환경 값을 난수로 갱신한다.
        - random.uniform(a, b): [a, b] 사이의 실수 난수를 발생시킴
        - round(val, n): 소수점 n자리로 반올림
        """
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18.0, 30.0), 2)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0.0, 21.0), 2)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50.0, 60.0), 2)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500.0, 715.0), 2)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 3)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4.0, 7.0), 2)

    def get_env(self):
        """
        현재 저장된 센서 데이터를 반환한다.
        """
        return self.env_values


# ================================================================
# [MissionComputer 클래스]
# ================================================================
# - '임무용 컴퓨터'를 흉내 내는 시뮬레이션 클래스
# - 실제 우주 기지라면 컴퓨터가 담당할 "모니터링 기능"을 간략히 모사한다.
#   1) 시스템 기본 정보 제공
#   2) 자원 사용률(CPU, 메모리) 모니터링
#   3) 센서 데이터 수집
# ================================================================
class MissionComputer:
    def __init__(self, name='MissionComputer'):
        self.name = name
        self.ds = DummySensor()  # 센서 연결

    def get_mission_computer_info(self):
        """
        [역할] 20초마다 시스템 기본 정보를 JSON 형식으로 출력
        - platform 모듈로 운영체제/CPU 정보 조회
        - psutil 모듈로 메모리 용량 조회
        """
        while True:
            try:
                info = {
                    'Instance': self.name,
                    '운영체계': platform.system(),                  # 예: Windows, Linux, Darwin
                    '운영체계_버전': platform.version(),            # OS 버전 문자열
                    'CPU_타입': platform.processor(),              # CPU 모델명
                    'CPU_코어_수': psutil.cpu_count(logical=False), # 물리적 코어 수
                    '메모리_크기_GB': round(psutil.virtual_memory().total / (1024 ** 3), 2)
                }
                print(json.dumps(info, indent=4, ensure_ascii=False))
            except Exception as e:
                print(f"[{self.name}] 시스템 정보 조회 에러: {e}")
            time.sleep(20)

    def get_mission_computer_load(self):
        """
        [역할] 20초마다 CPU 및 메모리 사용량을 출력
        - psutil.cpu_percent(interval=1): 1초 평균 CPU 사용률
        - psutil.virtual_memory().percent: 메모리 사용률(%)
        """
        while True:
            try:
                load = {
                    'Instance': self.name,
                    'CPU_실시간_사용량_%': psutil.cpu_percent(interval=1),
                    '메모리_실시간_사용량_%': psutil.virtual_memory().percent
                }
                print(json.dumps(load, indent=4, ensure_ascii=False))
            except Exception as e:
                print(f"[{self.name}] 시스템 부하 조회 에러: {e}")
            time.sleep(20)

    def get_sensor_data(self):
        """
        [역할] 5초마다 'DummySensor'로부터 환경 데이터를 수집하여 출력
        """
        while True:
            try:
                self.ds.set_env()                   # 센서 데이터 갱신
                sensor_data = self.ds.get_env()     # 새 데이터 가져오기
                result = {'Instance': self.name}    # 인스턴스 정보 추가
                result.update(sensor_data)
                print(json.dumps(result, indent=4, ensure_ascii=False))
            except Exception as e:
                print(f"[{self.name}] 센서 데이터 조회 에러: {e}")
            time.sleep(5)


# ================================================================
# [멀티스레딩 실행부]
# ================================================================
# - 하나의 MissionComputer 객체에서
#   세 가지 작업(info, load, sensor)을 각각 "스레드"로 실행한다.
# - 스레드(Thread): 같은 프로세스 내부에서 자원을 공유하면서 병렬 실행
#   → 자원 공유에 유리하지만, 동시성 문제(경쟁 조건)가 생길 수 있음.
# ================================================================
def run_threads():
    runComputer = MissionComputer('Threaded-Computer')

    # 각 기능을 별도의 스레드로 실행 (대상 함수 지정)
    t1 = threading.Thread(target=runComputer.get_mission_computer_info)
    t2 = threading.Thread(target=runComputer.get_mission_computer_load)
    t3 = threading.Thread(target=runComputer.get_sensor_data)

    # Daemon 스레드 → 메인 프로그램이 종료되면 같이 종료됨
    t1.daemon = True
    t2.daemon = True
    t3.daemon = True

    # 스레드 시작
    t1.start()
    t2.start()
    t3.start()

    # join() → 무한 루프여서 실제 종료는 되지 않음
    t1.join()
    t2.join()
    t3.join()


# ================================================================
# [멀티프로세싱 실행부]
# ================================================================
# - MissionComputer 객체를 세 개 생성하고,
#   각 기능을 "별도의 프로세스"로 실행한다.
# - 프로세스(Process): 운영체제가 할당하는 독립된 실행 단위
#   → 자원을 따로 쓰므로 안정적이지만, 생성 비용이 크고 공유가 불편하다.
# ================================================================
def run_processes():
    runComputer1 = MissionComputer('Process-1')
    runComputer2 = MissionComputer('Process-2')
    runComputer3 = MissionComputer('Process-3')

    p1 = multiprocessing.Process(target=runComputer1.get_mission_computer_info)
    p2 = multiprocessing.Process(target=runComputer2.get_mission_computer_load)
    p3 = multiprocessing.Process(target=runComputer3.get_sensor_data)

    # 프로세스 시작
    p1.start()
    p2.start()
    p3.start()

    # join → 기다리지만, 이 역시 무한 루프라 종료되지 않음
    p1.join()
    p2.join()
    p3.join()


# ================================================================
# [메인 실행부]
# ================================================================
# __name__ == '__main__' 구문:
# - 현재 파일을 직접 실행할 때만 아래 코드가 동작
# - 다른 모듈에서 import될 경우 실행되지 않음
# ================================================================
if __name__ == '__main__':
    print('--- 멀티스레드 실행 ---')
    threading.Thread(target=run_threads).start()  # 스레드 방식 병렬 실행

    print('--- 멀티프로세스 실행 ---')
    run_processes()  # 프로세스 방식 병렬 실행
