import openai
from flask import Flask, request, render_template

app = Flask(__name__)

# 設定你的OpenAI API金鑰
openai.api_key = "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"

def generate_itinerary(location, days):
    # 使用OpenAI生成行程
    prompt = f"為我生成一個在{location}旅行{days}天的行程："
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )
    print("輸入 token 數量:", response.usage["prompt_tokens"])
    print("生成 token 數量:", response.usage["generated_tokens"])

    return response.choices[0].text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        days = int(request.form['days'])
        
        # 調用你的行程生成流程，生成行程
        generated_itinerary = generate_itinerary(location, days)
        
        # 將生成的行程整合成回覆
        reply = f"您的{days}天行程安排如下：\n\n{generated_itinerary}"
        
        return render_template('result.html', reply=reply)
    
    return render_template('travelbot.html')

if __name__ == '__main__':
    app.run()
