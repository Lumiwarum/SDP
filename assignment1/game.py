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
				#присваивание через декоратор
				self.char = set_name(self.class_types[picked_cls])
				break
		# get the action dict
		actions = {}
		for ac_name, action  in inspect.getmembers(self.char, predicate=inspect.ismethod):
			if ac_name.startswith("_"):
				continue
			actions[ac_name] = action
		self.actions = actions


	def pick_enemy(self):
		print("Выберите вид вашего противника")
		while True:
			for cls in self.enemy_types:
				print(cls)
			picked_enemy = input()
			if picked_enemy in self.enemy_types:
				print(f"Вы выбрали противника: {picked_enemy}")
				#присваивание через декоратор
				self.enemy = set_name(self.enemy_types[picked_enemy])
				break

	def choose_action(self):
		print("Выберите вид действия")
		while True:
			for act in self.actions:
				print(act)
			choosen_act = input()
			if choosen_act in self.actions:
				damage = self.actions[choosen_act]()
				if self.enemy._take_damage(damage):
					print("Вы победили!!! перезапустите игру чтобы начать заново")
					break
				damage_char, pierce = self.enemy.attack()
				if self.char._take_damage(damage_char, pierce):
					print("Вы умерли, перезапустите игру чтобы начать заново")
					break
				


				


	def start_game(self):
		self.pick_class()
		self.pick_enemy()
		self.choose_action()




if __name__ == "__main__":
	game = Game()
	game.start_game()

	