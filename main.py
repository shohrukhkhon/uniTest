import random
import string

def questionsAndAnswer():
    questionsAnswer = []
    file = getFileContents('./files/questions.txt')
    questionsWithOptions = file.split('@')
    questionsWithOptions.pop(0)
    for questionWithOptions in questionsWithOptions:
        questionAndAnswer = []
        questionAndOptions = questionWithOptions.split('$')
        questionAndAnswer.append(questionAndOptions[0])
        questionNumber = int(questionAndOptions[0].split('.')[0])
        questionAndOptions.pop(0)
        options = questionAndOptions
        for option in options:
            optionByLetter = option.split(')')
            if optionByLetter[0] == answerKeys()[questionNumber]:
                questionAndAnswer.append(option)

        questionsAnswer.append(questionAndAnswer)
    return questionsAnswer


def answerKeys():
    file = getFileContents('./files/answers.txt')
    return file.splitlines()


def getFileContents(filename):
    with open(filename) as f:
        return f.read()


def toHtml():
    html = '<!doctype html><html lang="tj"><head><meta charset="UTF-8"></head><body>'
    for questionAndAnswer in questionsAndAnswer():
        html += '<p><b>%(question)s</b><br><span>%(answer)s</span></p><hr>' % {
            "question": questionAndAnswer[0], "answer": questionAndAnswer[1]
        }
    html += '</body></html>'
    return html


def writeToFile():
    html = toHtml()
    randomString = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    file = './html/%s.html' % randomString
    with open(file, 'x') as f:
        return f.write(html)


def htmlFooter():
    return "</body></html>"


if __name__ == '__main__':
    writeToFile()
