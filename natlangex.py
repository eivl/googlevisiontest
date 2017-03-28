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

example_text = '''Islamsk Råd Norges ansettelse av nikab-kledde Leyla Hasic som kommunikasjonsarbeider kan skape avstand mellom muslimer og ikke-muslimer, mener flere.
«Islamsk Råd gjør det virkelig ikke lett for norske muslimer», skrev redaktør Didrik Søderlind i Humanist, Human-Etisk Forbunds tidsskrift, på Twitter tirsdag morgen.

Han reagerer på Klassekampens nyhet om at Islamsk Råd Norge (IRN) har ansatt nikab-kledde Leyla Hasic (32) til å drive kommunikasjonsarbeid. Hun har markert seg som forsvarer av det ansiktsdekkende sløret.
Ifølge Klassekampen er Hasic ansatt som administrasjonskonsulent. Etter stillingsbeskrivelsen er oppgavene hennes kommunikasjonsarbeid, søknadsskriving og IT-drift. Etter det avisen får opplyst, har 32-åringen fungert i stillingen siden februar.

– Én ting er at det å kommunisere med nikab er vanskelig. Men en annen ting er at den representerer en islamsk praksis som er veldig fremmed for mange norske muslimer, sier Søderlind til VG.

– Mitt inntrykk er at toneangivende muslimske krefter har advart mot nikab-bruk, fordi det fremstår som fremmedartet og er egnet til å skape større avstand. Jeg tror at dette er uheldig for norske muslimer, sier han.

Stortingsrepresentant for Venstre Abid Raja, som selv er muslim, sier han er dypt skuffet over IRN, som han mener mener gjør norske muslimer til latter.

– Jeg har forståelse for om nordmenn blir støtt og provosert over dette. Jeg som muslim blir selv støtt og provosert, sier han til VG.

'''
sentiment, entities = language_analysis(example_text)
print(sentiment.score, sentiment.magnitude)

for e in entities:
    print(e.name, e.entity_type, e.metadata, e.salience)
