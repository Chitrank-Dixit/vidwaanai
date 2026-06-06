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

### Verse 1 (Bramha 0.2161)
- **Original**: पितृमातृसुदृद्भ्रातकलत्राणां. कृत. च। धमिनां श्रोत्रियाणां च दरिद्राणां तपस्विनाम्‌
- **Translation**: 

---

### Verse 2 (Bramha 0.2162)
- **Original**: उक्त दैन्यं च॒ विविध त्यक्त्वा लज्जां जनार्दन। देवतिर्यड्मनुष्येनबु.. स्थावरेघु चरेषु. च
- **Translation**: 

---

### Verse 3 (Bramha 0.2163)
- **Original**: न विद्यते तथा स्थान यत्राहं न गतः प्रभो। कदा मे नरके बासः कदा स्वर्ग जगत्पते
- **Translation**: 

---

### Verse 4 (Bramha 0.2164)
- **Original**: कदा मनुष्यलोकेषु कदा तिर्यग्गतेैपु च। जलयज्ले वथा चक्रे घटी रज्जुनिबन्धना
- **Translation**: 

---

### Verse 5 (Bramha 0.2165)
- **Original**: याति चोर्ध्वमधथ्व कदा मध्ये च तिष्ठति। तथा चाहं सुरश्रेष्ट कर्मरज्जुसमावृत:
- **Translation**: 

---

### Verse 6 (Bramha 0.2166)
- **Original**: अधश्चोध्व॑ तथा मध्ये भ्रमन्‌ गच्छामि योगत:। एवं संसारचक्रे5स्मिन्‌ू भैरवे रोमहर्षणे
- **Translation**: 

---

### Verse 7 (Bramha 0.2167)
- **Original**: भ्रमामि सुचिरं काल॑ नान्त॑ पश्यामि कहिंचित्‌ । न जाने कि करोम्यच्य हरे व्याकुलितेद्धिय:
- **Translation**: 

---

### Verse 8 (Bramha 0.2168)
- **Original**: शोकतृष्णाभिभूतो5ह॑ कांदिशीको विचेतन:। इदानीं त्वामह॑ देव विह्लल: शरण गत:
- **Translation**: 

---

### Verse 9 (Bramha 0.2169)
- **Original**: जाहि मां दुःखितं कृष्ण मग्न॑ संसारसागरे
- **Translation**: 

---

### Verse 10 (Bramha 0.2170)
- **Original**: कृपा कुरु जगन्नाथ भक्त मां यदि मन्यसे
- **Translation**: 

---

### Verse 11 (Bramha 0.2171)
- **Original**: त्वदृते नास्ति मे बन्धुर्यो$सौ चिन्तां करिष्यति
- **Translation**: 

---

### Verse 12 (Bramha 0.2172)
- **Original**: देव त्वां नाथमासाद्य न भयं मे5स्ति कुजचित्‌
- **Translation**: 

---

### Verse 13 (Bramha 0.2173)
- **Original**: जीविते मरणे चैव योगक्षेमे5थवा प्रभो। ये तु त्वां विधिवद्देव नार्चयन्ति नराधमा:
- **Translation**: 

---

### Verse 14 (Bramha 0.2174)
- **Original**: सुगतिस्तु क्थ तेषां भवेत्संसारबन्धनात्‌ । कि तेषां कुलशीलेन विद्यया जीवितेन च
- **Translation**: 

---

### Verse 15 (Bramha 0.2175)
- **Original**: येषां न जायते भक्तिर्जगद्धातरि केशवे। प्रकृतिं त्वासुरी प्राप्प ये त्वां निन्‍दन्ति मोहिता:
- **Translation**: 

---

### Verse 16 (Bramha 0.2176)
- **Original**: पतन्ति नरके घोरे जायमाना: पुनः पुतः।न तेषां निष्कृतिस्तस्माद्विद्यत नरकार्णवात्‌
- **Translation**: 

---

### Verse 17 (Bramha 0.2177)
- **Original**: ये दूषयन्ति दुर्वृत्तास्त्वां देव पुरुषाथमा:। यत्र यत्र भवेजन्म मम कर्मनिबन्धनातू
- **Translation**: 

---

### Verse 18 (Bramha 0.2178)
- **Original**: तत्र तत्र हरे भक्तिस्त्वयि चास्तु दृढ्य सदा। आराध्य त्वां सुरा दैत्या नशाश्वान्येडपि संयता:
- **Translation**: 

---

### Verse 19 (Bramha 0.2179)
- **Original**: अवापु: परमां सिद्धिं कस्त्वां देव न पूजयेत्‌ । न शवनुवन्ति ब्रह्माद्या: स्तोतुं त्वां त्रिदशा हरे
- **Translation**: 

---

### Verse 20 (Bramha 0.2180)
- **Original**: कर्थ मानुषयुद्धचाहं स्तौमि त्वां प्रकृते: परम्‌ । तथा चाज्ञानभावेन संस्तुतो5सि मया प्रभो
- **Translation**: 

---

