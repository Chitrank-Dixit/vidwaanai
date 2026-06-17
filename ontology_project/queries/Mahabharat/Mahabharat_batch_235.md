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

### Verse 1 (Mahabharat 0.2341)
- **Original**: जानेवाले कर्म मध्यम गओणीके हैं; जड्धासे होनेयाले कार्य भरह्मत्माओंके कुछ तथा खियोंके दुक्षरित्रका मूल नहीं जाना
- **Translation**: 

---

### Verse 2 (Mahabharat 0.2341)
- **Original**: जानेवाले कर्म मध्यम गओणीके हैं; जड्धासे होनेयाले कार्य भरह्मत्माओंके कुछ तथा खियोंके दुक्षरित्रका मूल नहीं जाना
- **Translation**: 

---

### Verse 3 (Mahabharat 0.2342)
- **Original**: अधम हैं और भार ढोनेका काम महा अधम है। राजन्‌ ! अब जा सकता। राजन्‌ ! ब्राह्मणोंकी पूजा करनेवाला, दाता,
- **Translation**: 

---

### Verse 4 (Mahabharat 0.2342)
- **Original**: अधम हैं और भार ढोनेका काम महा अधम है। राजन्‌ ! अब जा सकता। राजन्‌ ! ब्राह्मणोंकी पूजा करनेवाला, दाता,
- **Translation**: 

---

### Verse 5 (Mahabharat 0.2343)
- **Original**: आप दुर्योधन, झकुनि, मूर्ख दुःशासन तथा कर्णपर राज्यका कुदुम्बीजनोंके प्रति कोमलताका बर्ताव करनेबाल्पय और
- **Translation**: 

---

### Verse 6 (Mahabharat 0.2343)
- **Original**: आप दुर्योधन, झकुनि, मूर्ख दुःशासन तथा कर्णपर राज्यका कुदुम्बीजनोंके प्रति कोमलताका बर्ताव करनेबाल्पय और
- **Translation**: 

---

### Verse 7 (Mahabharat 0.2344)
- **Original**: भार रखकर उन्नति कैसे चाहते हैं ? भरत्रेष्ठ ! पाण्डव तो झीलवान्‌ राजा चिस्कालतक पृथ्वीका पालन करता है। झूर,
- **Translation**: 

---

### Verse 8 (Mahabharat 0.2344)
- **Original**: भार रखकर उन्नति कैसे चाहते हैं ? भरत्रेष्ठ ! पाण्डव तो झीलवान्‌ राजा चिस्कालतक पृथ्वीका पालन करता है। झूर,
- **Translation**: 

---

### Verse 9 (Mahabharat 0.2345)
- **Original**: सभी उत्तम गुणोंसे सम्पन्न हैं और आपकमें पफिताका-सा भाव विद्वार्‌ और सेवाधर्मको जाननेवाले--ये तीन प्रकारके मनुष्य
- **Translation**: 

---

### Verse 10 (Mahabharat 0.2345)
- **Original**: सभी उत्तम गुणोंसे सम्पन्न हैं और आपकमें पफिताका-सा भाव विद्वार्‌ और सेवाधर्मको जाननेवाले--ये तीन प्रकारके मनुष्य
- **Translation**: 

---

### Verse 11 (Mahabharat 0.2346)
- **Original**: रखकर बर्ताव करते हैं; आप भी उनपर पुत्रभाव रखकर पृथ्वीसे सुबर्णरूपी पुष्पका सक्षय करते हैं। भारत ! बुद्धिसे
- **Translation**: 

---

### Verse 12 (Mahabharat 0.2346)
- **Original**: रखकर बर्ताव करते हैं; आप भी उनपर पुत्रभाव रखकर पृथ्वीसे सुबर्णरूपी पुष्पका सक्षय करते हैं। भारत ! बुद्धिसे
- **Translation**: 

---

### Verse 13 (Mahabharat 0.2347)
- **Original**: उचित बर्ताव कीजिये
- **Translation**: 

---

### Verse 14 (Mahabharat 0.2347)
- **Original**: उचित बर्ताव कीजिये
- **Translation**: 

---

### Verse 15 (Mahabharat 0.2348)
- **Original**: 39--77
- **Translation**: 

---

### Verse 16 (Mahabharat 0.2348)
- **Original**: 39--77
- **Translation**: 

---

### Verse 17 (Mahabharat 0.2349)
- **Original**: कम औ विदुरनीति (चौथा अध्याय) विदुसजी कहते हैं--डस बिषयमें दत्ताश्रेय और साध्य
- **Translation**: 

---

### Verse 18 (Mahabharat 0.2349)
- **Original**: कम औ विदुरनीति (चौथा अध्याय) विदुसजी कहते हैं--डस बिषयमें दत्ताश्रेय और साध्य
- **Translation**: 

---

### Verse 19 (Mahabharat 0.2350)
- **Original**: बुद्धिमान्‌ जान पड़ते हैं; अतः हमलोगोंकों विज्ञत्तापूर्ण अपनी देवताओंके संवादरूप इस प्राचीन इतिहासका उदाहरण दिया
- **Translation**: 

---

### Verse 20 (Mahabharat 0.2350)
- **Original**: बुद्धिमान्‌ जान पड़ते हैं; अतः हमलोगोंकों विज्ञत्तापूर्ण अपनी देवताओंके संवादरूप इस प्राचीन इतिहासका उदाहरण दिया
- **Translation**: 

---

