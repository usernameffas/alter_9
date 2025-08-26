"""
Mars Mission Computer Monitoring System

미션 컴퓨터의 시스템 지표를 지속적으로 모니터링하는 프로그램
멀티스레딩과 멀티프로세싱을 활용하여 실시간 감시 기능 제공

작성자: Mars Mission Team
날짜: 2025-08-26
"""

import time          # 시간 관련 함수 사용 (sleep, strftime)
import threading     # 멀티스레딩 구현을 위한 모듈
import multiprocessing  # 멀티프로세싱 구현을 위한 모듈
import random        # 시뮬레이션용 랜덤 데이터 생성


class MissionComputer:
    """
    미션 컴퓨터 클래스
    
    화성 미션에서 사용되는 컴퓨터의 시스템 정보, 부하 상태, 센서 데이터를
    모니터링하는 기능을 제공하는 클래스
    
    Attributes:
        computer_id (int): 컴퓨터 식별 번호
    """
    
    def __init__(self, computer_id=1):
        """
        MissionComputer 인스턴스 초기화
        
        Args:
            computer_id (int): 컴퓨터 식별 번호 (기본값: 1)
        """
        self.computer_id = computer_id  # 각 컴퓨터를 구분하기 위한 고유 ID
    
    def get_mission_computer_info(self):
        """
        시스템 정보를 20초마다 출력하는 메소드
        
        컴퓨터의 기본 하드웨어 및 소프트웨어 정보를 지속적으로 모니터링
        - OS 정보
        - CPU 정보  
        - RAM 정보
        - 저장장치 정보
        - 현재 시간
        """
        while True:  # 무한 루프로 지속적인 모니터링
            # 시스템 정보 딕셔너리 생성
            info = {
                'Computer ID': self.computer_id,                    # 컴퓨터 식별번호
                'OS': 'Mars Mission OS v2.1',                      # 운영체제 정보
                'CPU': 'Intel Mars-Core i7-9900K',                 # 프로세서 정보
                'RAM': '32GB DDR4',                                 # 메모리 정보
                'Storage': '1TB SSD',                               # 저장장치 정보
                'Timestamp': time.strftime('%Y-%m-%d %H:%M:%S')     # 현재 시간
            }
            
            # 시스템 정보 출력
            print(f'[Computer {self.computer_id}] Mission Computer Info:')
            for key, value in info.items():
                print(f'  {key}: {value}')
            print('-' * 50)  # 구분선 출력
            
            # 20초 대기 (요구사항: 20초마다 출력)
            time.sleep(20)
    
    def get_mission_computer_load(self):
        """
        시스템 부하를 20초마다 출력하는 메소드
        
        컴퓨터의 실시간 성능 지표를 모니터링
        - CPU 사용률
        - 메모리 사용률
        - 디스크 사용률
        - 네트워크 I/O
        - 시스템 온도
        """
        while True:  # 무한 루프로 지속적인 모니터링
            # 시뮬레이션을 위한 랜덤 부하 데이터 생성
            load = {
                'Computer ID': self.computer_id,                        # 컴퓨터 식별번호
                'CPU Usage': f'{random.uniform(10, 90):.2f}%',          # CPU 사용률 (10-90%)
                'Memory Usage': f'{random.uniform(30, 80):.2f}%',       # 메모리 사용률 (30-80%)
                'Disk Usage': f'{random.uniform(20, 70):.2f}%',         # 디스크 사용률 (20-70%)
                'Network I/O': f'{random.uniform(1, 100):.2f} MB/s',    # 네트워크 속도 (1-100 MB/s)
                'Temperature': f'{random.uniform(35, 75):.1f}°C',       # 시스템 온도 (35-75°C)
                'Timestamp': time.strftime('%Y-%m-%d %H:%M:%S')         # 현재 시간
            }
            
            # 시스템 부하 정보 출력
            print(f'[Computer {self.computer_id}] System Load:')
            for key, value in load.items():
                print(f'  {key}: {value}')
            print('-' * 50)  # 구분선 출력
            
            # 20초 대기 (요구사항: 20초마다 출력)
            time.sleep(20)
    
    def get_sensor_data(self):
        """
        센서 데이터를 지속적으로 출력하는 메소드
        
        화성 환경 및 우주선 상태를 모니터링하는 센서 데이터
        - 대기압
        - 외부 온도
        - 태양광 패널 전압
        - 배터리 잔량
        - 통신 신호 강도
        """
        while True:  # 무한 루프로 지속적인 모니터링
            # 시뮬레이션을 위한 랜덤 센서 데이터 생성
            sensor_data = {
                'Computer ID': self.computer_id,                            # 컴퓨터 식별번호
                'Atmospheric Pressure': f'{random.uniform(0.6, 0.8):.3f} kPa',  # 화성 대기압 (0.6-0.8 kPa)
                'External Temperature': f'{random.uniform(-80, -20):.1f}°C',     # 화성 외부 온도 (-80 ~ -20°C)
                'Solar Panel Voltage': f'{random.uniform(22, 28):.2f}V',         # 태양광 패널 전압 (22-28V)
                'Battery Level': f'{random.uniform(70, 100):.1f}%',              # 배터리 잔량 (70-100%)
                'Communication Signal': f'{random.uniform(85, 100):.1f}%',       # 통신 신호 강도 (85-100%)
                'Timestamp': time.strftime('%Y-%m-%d %H:%M:%S')                  # 현재 시간
            }
            
            # 센서 데이터 출력
            print(f'[Computer {self.computer_id}] Sensor Data:')
            for key, value in sensor_data.items():
                print(f'  {key}: {value}')
            print('-' * 50)  # 구분선 출력
            
            # 10초 대기 (센서 데이터는 더 자주 체크)
            time.sleep(10)


def run_multithread():
    """
    멀티스레드 실행 함수 (3번 과제)
    
    하나의 runComputer 인스턴스를 생성하고
    get_mission_computer_info(), get_mission_computer_load(), get_sensor_data()
    세 개의 메소드를 각각 별도의 스레드로 동시 실행
    
    스레드의 특징:
    - 같은 메모리 공간을 공유
    - 같은 프로세스 내에서 실행
    - 컨텍스트 스위칭 비용이 적음
    """
    print('=== Multi-threading Mode ===')
    
    # runComputer 인스턴스 생성 (요구사항)
    runComputer = MissionComputer(1)
    
    # 각 메소드를 위한 스레드 생성
    # Thread 객체를 생성할 때 target 매개변수에 실행할 함수 지정
    thread1 = threading.Thread(target=runComputer.get_mission_computer_info)  # 시스템 정보 스레드
    thread2 = threading.Thread(target=runComputer.get_mission_computer_load)  # 시스템 부하 스레드
    thread3 = threading.Thread(target=runComputer.get_sensor_data)            # 센서 데이터 스레드
    
    # 데몬 스레드로 설정
    # 데몬 스레드: 메인 프로그램이 종료되면 함께 종료되는 스레드
    thread1.daemon = True
    thread2.daemon = True
    thread3.daemon = True
    
    # 모든 스레드 시작
    # start() 메소드를 호출하면 스레드가 실행되기 시작함
    thread1.start()  # 시스템 정보 모니터링 시작
    thread2.start()  # 시스템 부하 모니터링 시작
    thread3.start()  # 센서 데이터 모니터링 시작
    
    # join() 메소드: 해당 스레드가 종료될 때까지 메인 스레드가 대기
    # 하지만 while True 때문에 실제로는 무한 실행됨
    thread1.join()  # thread1이 종료될 때까지 대기
    thread2.join()  # thread2가 종료될 때까지 대기
    thread3.join()  # thread3이 종료될 때까지 대기


def computer_process_info(computer_id):
    """
    runComputer1용 프로세스 함수
    
    get_mission_computer_info() 메소드만 실행하는 독립적인 프로세스
    
    Args:
        computer_id (int): 컴퓨터 식별번호
    """
    # runComputer1에 해당하는 인스턴스 생성
    computer = MissionComputer(computer_id)
    
    # 시스템 정보 모니터링만 실행
    computer.get_mission_computer_info()


def computer_process_load(computer_id):
    """
    runComputer2용 프로세스 함수
    
    get_mission_computer_load() 메소드만 실행하는 독립적인 프로세스
    
    Args:
        computer_id (int): 컴퓨터 식별번호
    """
    # runComputer2에 해당하는 인스턴스 생성
    computer = MissionComputer(computer_id)
    
    # 시스템 부하 모니터링만 실행
    computer.get_mission_computer_load()


def computer_process_sensor(computer_id):
    """
    runComputer3용 프로세스 함수
    
    get_sensor_data() 메소드만 실행하는 독립적인 프로세스
    
    Args:
        computer_id (int): 컴퓨터 식별번호
    """
    # runComputer3에 해당하는 인스턴스 생성
    computer = MissionComputer(computer_id)
    
    # 센서 데이터 모니터링만 실행
    computer.get_sensor_data()


def run_multiprocess():
    """
    멀티프로세스 실행 함수 (4-5번 과제)
    
    runComputer1, runComputer2, runComputer3 세 개의 인스턴스를 
    각각 별도의 프로세스로 실행하여
    get_mission_computer_info(), get_mission_computer_load(), get_sensor_data()
    메소드를 독립적으로 실행
    
    프로세스의 특징:
    - 독립적인 메모리 공간을 가짐
    - 서로 다른 프로세스 간 데이터 공유 불가
    - 한 프로세스가 크래시되어도 다른 프로세스에 영향 없음
    - 멀티코어 CPU를 효율적으로 활용 가능
    """
    print('=== Multi-processing Mode ===')
    
    # 3개의 독립적인 프로세스 생성
    # Process 객체를 생성할 때 target에는 실행할 함수, args에는 함수의 인수 지정
    
    # runComputer1: 시스템 정보 담당 (Computer ID = 1)
    process1 = multiprocessing.Process(
        target=computer_process_info,  # 실행할 함수
        args=(1,)                      # 함수에 전달할 인수 (computer_id=1)
    )
    
    # runComputer2: 시스템 부하 담당 (Computer ID = 2)
    process2 = multiprocessing.Process(
        target=computer_process_load,  # 실행할 함수
        args=(2,)                      # 함수에 전달할 인수 (computer_id=2)
    )
    
    # runComputer3: 센서 데이터 담당 (Computer ID = 3)
    process3 = multiprocessing.Process(
        target=computer_process_sensor, # 실행할 함수
        args=(3,)                       # 함수에 전달할 인수 (computer_id=3)
    )
    
    # 모든 프로세스 시작
    # start() 메소드를 호출하면 새로운 프로세스가 생성되어 실행됨
    process1.start()  # runComputer1 프로세스 시작
    process2.start()  # runComputer2 프로세스 시작
    process3.start()  # runComputer3 프로세스 시작
    
    # join() 메소드: 해당 프로세스가 종료될 때까지 메인 프로세스가 대기
    # 하지만 while True 때문에 실제로는 무한 실행됨
    process1.join()  # process1이 종료될 때까지 대기
    process2.join()  # process2가 종료될 때까지 대기
    process3.join()  # process3이 종료될 때까지 대기


if __name__ == '__main__':
    """
    메인 실행 부분
    
    Python에서 스크립트가 직접 실행될 때만 아래 코드가 실행됨
    다른 모듈에서 import할 때는 실행되지 않음
    """
    
    # 프로그램 시작 메시지 출력
    print('Mars Mission Computer Monitoring System')
    print('=' * 50)
    
    # 1단계: 멀티스레딩 실행
    print('Starting Multi-threading...')
    print('runComputer 인스턴스로 3개 메소드를 멀티스레드 실행')
    print('Ctrl+C를 눌러서 중단하고 다음 단계로 진행하세요.\n')
    
    try:
        # 멀티스레드 모드 실행
        run_multithread()
    except KeyboardInterrupt:
        # Ctrl+C 입력 시 다음 단계로 진행
        print('\n멀티스레딩 모드 종료. 멀티프로세싱 모드로 전환합니다.\n')
    
    # 2단계: 멀티프로세싱 실행
    print('Starting Multi-processing...')
    print('runComputer1, runComputer2, runComputer3 인스턴스를 멀티프로세스로 실행')
    print('각각 다른 메소드를 담당합니다.')
    print('Ctrl+C를 눌러서 프로그램을 완전히 종료하세요.\n')
    
    try:
        # 멀티프로세스 모드 실행
        run_multiprocess()
    except KeyboardInterrupt:
        # Ctrl+C 입력 시 프로그램 종료
        print('\n프로그램을 종료합니다.')
    
    print('Mars Mission Computer Monitoring System 종료')
