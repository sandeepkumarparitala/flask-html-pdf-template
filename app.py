from flask import Flask, escape, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    data={
        "name": "Steve Jobs",
        "profilePic": '/static/profile.jpg',
        "currentRole": "VP-operations",
        "companyName":"Johnson & Jhonson",
        "highestDegree":"MBA, Columbia Bussiness School",
        "gender": "male",
        "ethnicity": "non-hispanic white",
        "phone": "9080-90-90099",
        "skillOnePercentage": "80",
        "skillTwoPercentage": "30",
        "skillThreePercentage": "90",
        "bio": True,
        "phd": False,
        "rAndD": True,
        "mba": True,
        "mAndA": False,
        "ventureCapital": True,
        "email":"abcd@abc.com",
        "readinessValue": "40",
        "treeData": [
                {
                  "id": "A",
                  "name": "Apples",
                },
                {
                  "id": "B",
                  "name": "Bananas",
                },
                {
                  "id": "O",
                  "name": "Oranges",
                },
                {
                  "id": "K",
                  "name": "Anne",
                  "parent": "A",
                  "value": 5,
                },
                {
                  "name": "Rick",
                  "parent": "K",
                  "value": 3,
                },
                {
                  "name": "Peter",
                  "parent": "A",
                  "value": 4,
                },
                {
                  "name": "Anne",
                  "parent": "B",
                  "value": 4,
                },
                {
                  "name": "Rick",
                  "parent": "B",
                  "value": 10,
                },
                {
                  "name": "Peter",
                  "parent": "B",
                  "value": 1,
                },
                {
                  "name": "Anne",
                  "parent": "O",
                  "value": 1,
                },
                {
                  "name": "Rick",
                  "parent": "O",
                  "value": 3,
                },
                {
                  "name": "Peter",
                  "parent": "O",
                  "value": 3,
                },
                {
                  "name": "Susanne",
                  "parent": "Kiwi",
                  "value": 2,
                },
              ],
        "about": "18+ years of experience in business development and Mergers and Acquisitions, completing over $70 billion in high value growth-oriented transactions, in fields ranging from medical devices and pharmaceuticals to semiconductors and software. In his most recent role as VP, Business Development, he added many platforms and technologies to Ethicon's portfolio, including those in digital surgery (3Di, Auris investment and collaboration), GERD (Torax), Interventional Oncology (NeuWave, Auris collaboration), Wound Closure (barbed sutures) and Energy (Megadyne)"
    }
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)