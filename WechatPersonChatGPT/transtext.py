from datetime import datetime

from dataclasses import dataclass
import openai
import csv


def append_question2file(question: str) -> None:
    row = {'question': question,
           'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

    with open(file="data/user_question.csv", mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        writer.writerow(row)


@dataclass
class ProcessTextOutput:
    status: bool = False
    text: str = None


class ProcessTextChatGpt:
    """
    这里提供了OpenAi的chatGpt模板
    只需要将config的session_token参数修改即可。

    """

    def __init__(self) -> None:
        openai.api_key = "aaa"

    def trans(self, x: str) -> ProcessTextOutput:
        res = x.replace("@天天向上", "")
        #append_question2file(question=res)

        if len(res) > 1:

            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=res,
                    max_tokens=1024,
                    n=1,
                    stop=None,
                    temperature=0.6,
                )
                generated_text = response["choices"][0]["text"]
                #res = f"\n[input]: {res}\n[datetime]: {datetime.now()}\n[result]: {generated_text}"
                res = generated_text

                return ProcessTextOutput(
                    status=True,
                    text=res
                )
            except Exception as e:
                print(e)
                res = "sorry~ 我出错了~"

                print("error 1")
                return ProcessTextOutput(
                    status=True,
                    text=res
                )
        else:
            return ProcessTextOutput()


if __name__ == '__main__':
    pt = ProcessTextChatGpt()
    x = pt.trans("@天天向上 请用中文给我讲讲原神的故事")
    print(x.text)

