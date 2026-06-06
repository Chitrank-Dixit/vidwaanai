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

### Verse 1 (Mahabharat 0.7001)
- **Original**: काँप उठी। वे अपनी पसलियों, भुजाओं और जाँघोंसे मांस राजाका अन्तःकरण बहुत शुद्ध था। उन्होंने जब उस पक्षीको
- **Translation**: 

---

### Verse 2 (Mahabharat 0.7001)
- **Original**: काँप उठी। वे अपनी पसलियों, भुजाओं और जाँघोंसे मांस राजाका अन्तःकरण बहुत शुद्ध था। उन्होंने जब उस पक्षीको
- **Translation**: 

---

### Verse 3 (Mahabharat 0.7002)
- **Original**: काट-काटकर जल्दी-जल्दी तराजू भरने लगे तथापि बह धरय्भीत होकर अपनी गोदमें आया देखा तो उसे धीरज देते
- **Translation**: 

---

### Verse 4 (Mahabharat 0.7002)
- **Original**: काट-काटकर जल्दी-जल्दी तराजू भरने लगे तथापि बह धरय्भीत होकर अपनी गोदमें आया देखा तो उसे धीरज देते
- **Translation**: 

---

### Verse 5 (Mahabharat 0.7003)
- **Original**: मौसराज्ि उस कबूतरके बराबर न हुई। जब राजाके शरीरका हुए कहा--“कपोत ! अब तुझें किसी भी पक्षीका डर नहीं
- **Translation**: 

---

### Verse 6 (Mahabharat 0.7003)
- **Original**: मौसराज्ि उस कबूतरके बराबर न हुई। जब राजाके शरीरका हुए कहा--“कपोत ! अब तुझें किसी भी पक्षीका डर नहीं
- **Translation**: 

---

### Verse 7 (Mahabharat 0.7004)
- **Original**: मांस चुक गया और रक्तकी धारां बहाता हुआ केबल है; किंतु यह तो बता, तुझें यह पहान्‌ भय कहाँ और किससे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.7004)
- **Original**: मांस चुक गया और रक्तकी धारां बहाता हुआ केबल है; किंतु यह तो बता, तुझें यह पहान्‌ भय कहाँ और किससे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.7005)
- **Original**: हष्डियोंका ढाँचामात्र रह गया, तब वे मांस काटनेका काम बंद प्राप्त हुआ ? तूनें क्या अपराध किया है ? जिससे घबराया
- **Translation**: 

---

### Verse 10 (Mahabharat 0.7005)
- **Original**: हष्डियोंका ढाँचामात्र रह गया, तब वे मांस काटनेका काम बंद प्राप्त हुआ ? तूनें क्या अपराध किया है ? जिससे घबराया
- **Translation**: 

---

### Verse 11 (Mahabharat 0.7006)
- **Original**: करके स्वयं ही तराजूपर चढ़ गये। हुआ-सा यहाँ आया है। मैं तुझे अभय देता हूँ, मेरे पास आ
- **Translation**: 

---

### Verse 12 (Mahabharat 0.7006)
- **Original**: करके स्वयं ही तराजूपर चढ़ गये। हुआ-सा यहाँ आया है। मैं तुझे अभय देता हूँ, मेरे पास आ
- **Translation**: 

---

### Verse 13 (Mahabharat 0.7007)
- **Original**: . यह देखकर इच्रसहित तीनों लोकके देवता राजा जानेपर अब कोई तुझे पकड़नेका जिचार भी मनयें नहीं ला
- **Translation**: 

---

### Verse 14 (Mahabharat 0.7007)
- **Original**: . यह देखकर इच्रसहित तीनों लोकके देवता राजा जानेपर अब कोई तुझे पकड़नेका जिचार भी मनयें नहीं ला
- **Translation**: 

---

### Verse 15 (Mahabharat 0.7008)
- **Original**: उश्ीनरके पास आ पःँचे और आकाशमें खड़े होकर सकता। यह काश्ञौंका राज्य और अपना जीवनतक तेरी
- **Translation**: 

---

### Verse 16 (Mahabharat 0.7008)
- **Original**: उश्ीनरके पास आ पःँचे और आकाशमें खड़े होकर सकता। यह काश्ञौंका राज्य और अपना जीवनतक तेरी
- **Translation**: 

---

### Verse 17 (Mahabharat 0.7009)
- **Original**: भेरी तथा दुल्दुभी बजाने लगें। देवताओंने राजा बृषदर्भ रक्षाके छिये निछावर कर दूँगा। तू विश्वास कर, अब तुझे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.7009)
- **Original**: भेरी तथा दुल्दुभी बजाने लगें। देवताओंने राजा बृषदर्भ रक्षाके छिये निछावर कर दूँगा। तू विश्वास कर, अब तुझे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.7010)
- **Original**: (उश्ञीनर) को अमृतसे नहलाया, उनके ऊपर अत्यन्त तनिक भी भय नहीं है।'
- **Translation**: 

---

### Verse 20 (Mahabharat 0.7010)
- **Original**: (उश्ञीनर) को अमृतसे नहलाया, उनके ऊपर अत्यन्त तनिक भी भय नहीं है।'
- **Translation**: 

---

