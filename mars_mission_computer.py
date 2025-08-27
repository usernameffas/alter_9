# ----------------------------- 모듈 임포트 -----------------------------
import platform
import psutil
import json
import time
import threading
import multiprocessing
import random


# ----------------------------- DummySensor 클래스 -----------------------------
class DummySensor:
    """
    화성 기지의 환경 데이터를 무작위로 생성하는 더미 센서
    """

    def __init__(self):
        # 센서 데이터 저장용 딕셔너리 초기화
        self.env_values = {
            'mars_base_internal_temperature': 0.0,   # 내부 온도 (°C)
            'mars_base_external_temperature': 0.0,   # 외부 온도 (°C)
            'mars_base_internal_humidity': 0.0,      # 내부 습도 (%)
            'mars_base_external_illuminance': 0.0,   # 외부 조도 (lux)
            'mars_base_internal_co2': 0.0,           # 내부 CO2 농도 (%)
            'mars_base_internal_oxygen': 0.0         # 내부 O2 농도 (%)
        }

    def set_env(self):
        # 무작위 값 생성 (범위는 임의로 설정)
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18.0, 30.0), 2)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0.0, 21.0), 2)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50.0, 60.0), 2)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500.0, 715.0), 2)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 3)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4.0, 7.0), 2)

    def get_env(self):
        return self.env_values


# ----------------------------- MissionComputer 클래스 -----------------------------
class MissionComputer:
    """
    임무 컴퓨터 시뮬레이션 클래스
    - 시스템 정보 출력
    - 시스템 부하 출력
    - 센서 데이터 출력
    """

    def __init__(self, name='MissionComputer'):
        self.name = name
        self.ds = DummySensor()  # 더미 센서 연결

    def get_mission_computer_info(self):
        """ 20초 마다 시스템 기본 정보 출력 """
        while True:
            try:
                info = {
                    'Instance': self.name,
                    '운영체계': platform.system(),
                    '운영체계_버전': platform.version(),
                    'CPU_타입': platform.processor(),
                    'CPU_코어_수': psutil.cpu_count(logical=False),
                    '메모리_크기_GB': round(psutil.virtual_memory().total / (1024 ** 3), 2)
                }
                print(json.dumps(info, indent=4, ensure_ascii=False))
            except Exception as e:
                print(f"[{self.name}] 시스템 정보 조회 에러: {e}")
            time.sleep(20)

    def get_mission_computer_load(self):
        """ 20초 마다 CPU/메모리 부하 상태 출력 """
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
        """ 5초 마다 센서 데이터 출력 """
        while True:
            try:
                self.ds.set_env()
                sensor_data = self.ds.get_env()
                result = {'Instance': self.name}
                result.update(sensor_data)
                print(json.dumps(result, indent=4, ensure_ascii=False))
            except Exception as e:
                print(f"[{self.name}] 센서 데이터 조회 에러: {e}")
            time.sleep(5)


# ----------------------------- 실행부 -----------------------------
def run_threads():
    """
    하나의 MissionComputer 인스턴스를 만들고
    3개의 메소드를 각각 스레드로 실행
    """
    runComputer = MissionComputer('Threaded-Computer')

    t1 = threading.Thread(target=runComputer.get_mission_computer_info)
    t2 = threading.Thread(target=runComputer.get_mission_computer_load)
    t3 = threading.Thread(target=runComputer.get_sensor_data)

    t1.daemon = True
    t2.daemon = True
    t3.daemon = True

    t1.start()
    t2.start()
    t3.start()

    # 메인 스레드가 유지되도록 join (무한루프라 종료 안됨)
    t1.join()
    t2.join()
    t3.join()


def run_processes():
    """
    MissionComputer 인스턴스를 3개 만들고
    각기 다른 프로세스로 실행
    """
    runComputer1 = MissionComputer('Process-1')
    runComputer2 = MissionComputer('Process-2')
    runComputer3 = MissionComputer('Process-3')

    p1 = multiprocessing.Process(target=runComputer1.get_mission_computer_info)
    p2 = multiprocessing.Process(target=runComputer2.get_mission_computer_load)
    p3 = multiprocessing.Process(target=runComputer3.get_sensor_data)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


if __name__ == '__main__':
    print('--- 멀티스레드 실행 ---')
    threading.Thread(target=run_threads).start()

    print('--- 멀티프로세스 실행 ---')
    run_processes()
