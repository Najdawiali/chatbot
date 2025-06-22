from config import Gemini
from db import MovieQuery
from pdfile import PDFGenerator

def main():
    model = Gemini()
    while True:
        txt = input()
        if txt == None:
            continue
        else:
            text = model.text_generation(txt)
            if text == 'Tp$#_0':
                print('You welcome')
                break
            else:
                if text[-1] == '1':
                    print(text[:-1])
                elif text[-1] == '2':
                    movie = (text[:-1])
                    mq = MovieQuery()
                    movie_details = mq.get_movie_story(movie)
                    if movie_details == 'Movie not found.':
                        print('Movie not found.')
                    else:
                        final_result = model.highlights(movie_details)
                        pdf = PDFGenerator(final_result)
                        pdf.generate_pdf()



if __name__ == '__main__':
    main()