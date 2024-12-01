def get_cats_info(path):
	dict_cats = []
	try:
		with open(path, "r", encoding="utf-8") as file:
			lines = file.readlines()

			if not lines:
				return "Файл порожній"
			
			for i in lines:
				id, name, age = i.strip().split(",")
				dict_cats.append({"id": id, "name": name, "age": age})
			
	except FileNotFoundError:
		return "Файл не знайдено"
	
	except Exception as e:
		return f"Сталася помилка: {e}"

	return dict_cats

cats_info = get_cats_info("/Users/a7/Documents/Go_IT/Repozitories/goit-algo-hw-04/task_2/cats.txt")
print(cats_info)