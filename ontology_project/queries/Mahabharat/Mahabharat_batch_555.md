# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Mahabharat 0.5541)
- **Original**: घोड़ोंको घायछ कर दिया; फिर एक बाण मास्कर उसके गिर पड़े।
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5541)
- **Original**: घोड़ोंको घायछ कर दिया; फिर एक बाण मास्कर उसके गिर पड़े।
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5542)
- **Original**: धनुषको काट डाला। सात्यकिने उसे फेंककर दूसरा धनुष तदनन्तर, राजा युधिष्ठिरने धनुष उठाया और तेज किये
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5542)
- **Original**: धनुषको काट डाला। सात्यकिने उसे फेंककर दूसरा धनुष तदनन्तर, राजा युधिष्ठिरने धनुष उठाया और तेज किये
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5543)
- **Original**: उठाया और कृतबर्माकी छातीपें दस बाण मारे; फिर अनेकों हुए भल्ल्मोंसे एक ही क्षणमें बहुत-से झत्नुओंका नाश कर
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5543)
- **Original**: उठाया और कृतबर्माकी छातीपें दस बाण मारे; फिर अनेकों हुए भल्ल्मोंसे एक ही क्षणमें बहुत-से झत्नुओंका नाश कर
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5544)
- **Original**: भल्लोंके प्रहारसे उसके रथ और जूएकी ईबाको काट डाला। डाला। उनके आणोंसे आच्छादित होनेके कारण आपके
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5544)
- **Original**: भल्लोंके प्रहारसे उसके रथ और जूएकी ईबाको काट डाला। डाला। उनके आणोंसे आच्छादित होनेके कारण आपके
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5545)
- **Original**: यही नहीं, उसके थोड़ों, पार्श्वकक्षकों तथा सारधिको भी सैनिकोने आँखें मीच कीं और आपसमें ही एक-दूसरेको
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5545)
- **Original**: यही नहीं, उसके थोड़ों, पार्श्वकक्षकों तथा सारधिको भी सैनिकोने आँखें मीच कीं और आपसमें ही एक-दूसरेको
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5546)
- **Original**: मौतके घाट उतार दिया। घायल करके वे बहुत कष्ट पाने लगे। उस समय उनके
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5546)
- **Original**: मौतके घाट उतार दिया। घायल करके वे बहुत कष्ट पाने लगे। उस समय उनके
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5547)
- **Original**: . कृतवर्मांको रथहीन देख कृपाचार्यने उसे अपने रथपर झरीरोंसे खूनकी धाराएँ बह रही थरं और वे अपने अख-झख््र
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5547)
- **Original**: . कृतवर्मांको रथहीन देख कृपाचार्यने उसे अपने रथपर झरीरोंसे खूनकी धाराएँ बह रही थरं और वे अपने अख-झख््र
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5548)
- **Original**: बिठा लिया और दूर हटा ले गये। अब दु्वोधनकी सेना फिर खोकर जीवनसे भी हाथ धो रहे थे।
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5548)
- **Original**: बिठा लिया और दूर हटा ले गये। अब दु्वोधनकी सेना फिर खोकर जीवनसे भी हाथ धो रहे थे।
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5549)
- **Original**: भागने लगी। पाष्डबॉंको बेगसे आते और अपनी सेनाको मद्रराजका एक छोटा भाई था, जो अभी नवयुवक था,
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5549)
- **Original**: भागने लगी। पाष्डबॉंको बेगसे आते और अपनी सेनाको मद्रराजका एक छोटा भाई था, जो अभी नवयुवक था,
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5550)
- **Original**: भागती देख दुर्योधनने अकेले ही समस्त पाण्डबोंको रोका।
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5550)
- **Original**: भागती देख दुर्योधनने अकेले ही समस्त पाण्डबोंको रोका।
- **Translation**: 

---

