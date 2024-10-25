
from datetime import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                all_data.append(line)



filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов (Линейный вызов: 0:00:15.064035)
start = datetime.now()
for name in filenames:
    read_info(name)
end = datetime.now()
time = end - start
print(f'Линейный вызов: {time}')

# Многопроцессный вызов (Многопроцессный вызов: 0:00:09.992224)
if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
        end = datetime.now()
        time = end - start
        print(f'Многопроцессный вызов: {time}')