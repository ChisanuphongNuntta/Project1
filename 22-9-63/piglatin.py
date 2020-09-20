def main():
    enter = input('Enter your sentense to change to pig latin : ')
    enter = (enter.split())
    x = (enter[0])
    if x == "A""E""I""O""U":
        print(enter[1:]+x+'HAY')
    else:
        print(enter[1:]+x+'AY')
    

main()