from google.cloud import language


def language_analysis(text):
    client = language.Client()
    document = client.document_from_text(text)
    sent_analysis = document.analyze_sentiment()
    print(dir(sent_analysis))
    sentiment = sent_analysis.sentiment
    ent_analysis = document.analyze_entities()
    entities = ent_analysis.entities
    return sentiment, entities

example_text = '''Islamic Council Norway employing nikab clad Leyla Hasic that communication work can create distance between Muslims and non-Muslims mean more.
"Islamic Council makes it really easy for Norwegian Muslims," ​​wrote editor Didrik Søderlind in Humanist, Humanist Society journal, Twitter Tuesday morning.

He responds to the class struggle news that the Islamic Council of Norway (IRN) has appointed nikab-clad Leyla Hasic (32) to engage in communications work. She has distinguished himself as defender of the face covering veil.
According to the class struggle is Hasic employed as a management consultant. After the job description, the tasks her communications work, writing applications and IT operations. After the newspaper gets lit, the 32-year-old acted in the position since February.

- One thing is that it communicate with nikab is difficult. But another thing is that it represents an Islamic practice which is very foreign to many Norwegian Muslims, says Søderlind VG.

- My impression was that the leading Muslim forces have warned nikab-user, because it appears alien and is apt to widen. I think that this is unfortunate for Norwegian Muslims, he said.

Member of Parliament for the Liberal Party Abid Raja, himself a Muslim, said he was deeply disappointed by IRN, which he believes thinks makes Norwegian Muslims to laugh.

- I understand about Norwegians are offended and angered by this. I as a Muslim becomes even offended and angered, he says to VG.


'''
sentiment, entities = language_analysis(example_text)
print(sentiment.score, sentiment.magnitude)

for e in entities:
    print(e.name, e.entity_type, e.metadata, e.salience)
