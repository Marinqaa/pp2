movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def single_movie(name):
    for m in movies:
        if m["name"] == name and m["imdb"] > 5.5:
            return True
        elif m["name"] == name and m["imdb"] < 5.5:
            return "Sorry, imdb less than 5.5"
name = str(input())
print(single_movie(name))
def above_5dot5(movies):
    movies_above = []
    for m in movies:
        if m["imdb"] > 5.5:
            movies_above.append(m["name"])
    return movies_above
print(above_5dot5(movies))
def movies_average_score(movies_list):
    movies_scores = []
    for m in movies_list:
        score = m["imdb"]
        movies_scores.append(score)
    average_score = sum(movies_scores) / len(movies_scores)
    return average_score
average = movies_average_score(movies)
print(average)

def m_category(category):
    m_category = []
    for m in movies:
        if m["category"] == category:
            m_category.append(m["name"])
    return m_category
category = input()
new_list = m_category(category)
print(m_category(category))
