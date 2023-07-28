# Исключение: неверный тип аргумента.
class InvalidArgumentType(Exception):

	#==========================================================================================#
	# >>>>> СВОЙСТВА <<<<< #
	#==========================================================================================#

	# Сообщение об ошибке.
	__Message = "\""

	#==========================================================================================#
	# >>>>> МЕТОДЫ <<<<< #
	#==========================================================================================#

	# Конструктор: вызывается при обработке исключения.
	def __init__(self, Value: str, Type: str): 
		# Обеспечение доступа к оригиналу наследованного свойства.
		super().__init__(self.__Message) 
		# Добавление данных в сообщение об ошибке.
		self.__Message += Value + "\" isn't \"" + Type + "\"."
		
			
	# Информатор: вызывается при выводе исключения в консоль.
	def __str__(self):
		return self.__Message

# Исключение: активированы взаимоисключающие флаги.
class MutuallyExclusiveFlags(Exception):

	#==========================================================================================#
	# >>>>> СВОЙСТВА <<<<< #
	#==========================================================================================#

	# Сообщение об ошибке.
	__Message = "\""

	#==========================================================================================#
	# >>>>> МЕТОДЫ <<<<< #
	#==========================================================================================#

	# Конструктор: вызывается при обработке исключения.
	def __init__(self, Command: str): 
		# Обеспечение доступа к оригиналу наследованного свойства.
		super().__init__(self.__Message) 
		# Добавление данных в сообщение об ошибке.
		self.__Message += Command + "\"."
		
			
	# Информатор: вызывается при выводе исключения в консоль.
	def __str__(self):
		return self.__Message

# Исключение: активированы взаимоисключающие ключи.
class MutuallyExclusiveKeys(Exception):

	#==========================================================================================#
	# >>>>> СВОЙСТВА <<<<< #
	#==========================================================================================#

	# Сообщение об ошибке.
	__Message = "\""

	#==========================================================================================#
	# >>>>> МЕТОДЫ <<<<< #
	#==========================================================================================#

	# Конструктор: вызывается при обработке исключения.
	def __init__(self, Command: str): 
		# Обеспечение доступа к оригиналу наследованного свойства.
		super().__init__(self.__Message) 
		# Добавление данных в сообщение об ошибке.
		self.__Message += Command + "\"."
		
			
	# Информатор: вызывается при выводе исключения в консоль.
	def __str__(self):
		return self.__Message

# Исключение: недостаточно аргументов.
class NotEnoughArguments(Exception):

	#==========================================================================================#
	# >>>>> СВОЙСТВА <<<<< #
	#==========================================================================================#

	# Сообщение об ошибке.
	__Message = "\""

	#==========================================================================================#
	# >>>>> МЕТОДЫ <<<<< #
	#==========================================================================================#

	# Конструктор: вызывается при обработке исключения.
	def __init__(self, Command: str): 
		# Обеспечение доступа к оригиналу наследованного свойства.
		super().__init__(self.__Message) 
		# Добавление данных в сообщение об ошибке.
		self.__Message += Command + "\"."

	# Информатор: вызывается при выводе исключения в консоль.
	def __str__(self):
		return self.__Message

# Исключение: слишком много аргументов.
class TooManyArguments(Exception):

	#==========================================================================================#
	# >>>>> СВОЙСТВА <<<<< #
	#==========================================================================================#

	# Сообщение об ошибке.
	__Message = "\""

	#==========================================================================================#
	# >>>>> МЕТОДЫ <<<<< #
	#==========================================================================================#

	# Конструктор: вызывается при обработке исключения.
	def __init__(self, Command: str):
		# Обеспечение доступа к оригиналу наследованного свойства.
		super().__init__(self.__Message) 
		# Добавление данных в сообщение об ошибке.
		self.__Message += Command + "\"."
			
	# Информатор: вызывается при выводе исключения в консоль.
	def __str__(self):
		return self.__Message

# Исключение: неизвестная комманда.
class UnknownCommand(Exception):

	#==========================================================================================#
	# >>>>> СВОЙСТВА <<<<< #
	#==========================================================================================#

	# Сообщение об ошибке.
	__Message = "\""

	#==========================================================================================#
	# >>>>> МЕТОДЫ <<<<< #
	#==========================================================================================#

	# Конструктор: вызывается при обработке исключения.
	def __init__(self, Command: str): 
		# Обеспечение доступа к оригиналу наследованного свойства.
		super().__init__(self.__Message) 
		# Добавление данных в сообщение об ошибке.
		self.__Message += Command + "\"."
		
			
	# Информатор: вызывается при выводе исключения в консоль.
	def __str__(self):
		return self.__Message