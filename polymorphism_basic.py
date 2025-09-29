class remote:
    def remote_control(self):
        print("You can control electronic items using remote")


class Tv(remote):
    def remote_control(self):
        print("You can control These things using tv remote")
        print("power on")
        print("Change Channel")
        print("Change volume")
        print("power off")

class Fan(remote):
    def remote_control(self):
        print("You can control These things using Fan remote")
        print("Power on")
        print("increase fan speed")
        print("decrease fan speed")
        print("Power off")

class Ac(remote):
    def remote_control(self):
        print("You can control These things using Ac remote")
        print("Power on")
        print("increase temperature")
        print("decrease temperature")
        print("Power off")

        
ob=Tv()
ob.remote_control()
print()
ob=Fan()
ob.remote_control()
print()
ob=Ac()
ob.remote_control()

        