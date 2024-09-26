import sys
import os
import inspect

def load_classes(plugin_dir):
	# Перебирем файлы в папке plugins
	class_container = {}
	for fname in os.listdir(plugin_dir):

		# Нас интересуют только файлы с расширением .py
		if fname.endswith(".py"):

			# Обрежем расширение .py у имени файла
			module_name = fname[: -3]

			# Пропустим файлы base.py и __init__.py
			if module_name != "base" and module_name != "__init__":
				print("Load module %s" % module_name)

				# Загружаем модуль и добавляем его имя в список загруженных модулей
				__import__(plugin_dir+'.'+module_name)
				for name, cls in inspect.getmembers(sys.modules[plugin_dir+'.'+module_name], inspect.isclass):
					if name.endswith('Base'):
						continue
					class_container[name] = cls
			else:
				print("Skip " + fname)
	return class_container

#декоратор для выбора имени
def set_name(object, **args):
	print("Выберите имя")
	while True:
		name = input()
		print(f"Имя будет:{name}, вы уверены? y/n")
		answer = input()
		if answer == 'y' or answer == 'yes':
			break
		else:
			print("Выберите имя снова")
	
	return object(name = name, **args)



class Game:
	def __init__(self) -> None:
		clas_dir = "classes"
		self.class_types = load_classes(clas_dir)
		enemy_dir = "enemies"
		self.enemy_types = load_classes(enemy_dir)

	def pick_class(self):
		print("Выберите класс вашего персонажа")
		while True:
			for cls in self.class_types:
				print(cls)
			picked_cls = input()
			if picked_cls in self.class_types:
				print(f"Вы выбрали класс: {picked_cls}")
				self.char = set_name(self.class_types[picked_cls])
				break

	def pick_enemy(self):
		print("Выберите вид вашего противника")
		while True:
			for cls in self.enemy_types:
				print(cls)
			picked_enemy = input()
			if picked_enemy in self.enemy_types:
				print(f"Вы выбрали противника: {picked_enemy}")
				self.enemy = set_name(self.enemy_types[picked_enemy])
				break


	def start_game(self):
		self.pick_class()
		self.pick_enemy()




if __name__ == "__main__":
	game = Game()
	game.start_game()

	