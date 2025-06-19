from config import Gemini

def main():
    model = Gemini()
    while True:
        txt = input()
        if txt == None:
            continue
        else:
            if model.text_generation(txt) == 'Tp$#_0':
                print('thanks')
                break
            else:
                print(model.text_generation(txt))#test test

if __name__ == '__main__':
    main()






