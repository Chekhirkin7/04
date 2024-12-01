from pathlib import Path

def total_salary(path_to_file):
	all_salary = 0
	aver_salary = 0
	try:
		with open(path_to_file, "r", encoding="utf-8") as file:
			lines = file.readlines()

			if not lines:
				return "Файл порожній"
			
			for i in lines:
				_, salary = i.strip().split(",")
				salary = int(salary)
				all_salary += salary
			
			aver_salary = all_salary / len(lines)

	except FileNotFoundError:
		return "Файл не знайдено"
	
	except Exception as e:
		return f"Сталася помилка: {e}"
	
	return f"Загальна сума заробітної плати: {all_salary}, Середня заробітна плата: {aver_salary:.0f}"


print(total_salary("/Users/a7/Documents/Go_IT/Repozitories/goit-algo-hw-04/task_1/mounth__salary.txt"))