def func(x,y):
    pass
func1 = lambda y : func(3,y)
#замыкание
func(1,2)
func2(1)(3) #каррирование
