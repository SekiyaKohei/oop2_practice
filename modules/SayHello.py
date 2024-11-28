class SayHello:
def
__
init
__(self, target="World"):
self.target = target
def say(self):
print(f"Hello, {self.target}!!")
if_name__== '__main__':
app = SayHello()
app.say()
app = SayHello("Someone")
app.say()