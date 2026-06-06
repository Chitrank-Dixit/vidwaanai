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

### Verse 1 (Vishnu Puran 0.10641)
- **Original**: 14 मथुराबासिन॑ लोक तत्रानीय जनार्दन: । आसच्ने कालयवने मथुरां च स्वयं ययौ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10642)
- **Original**: 15 बहिरावासिते सैन्ये मधुराया निरायुध: । निर्जगाम च गोविन्दो दरदर्श यवनश्च तम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10643)
- **Original**: 16 स ज्ञात्वा बासुदेवब ते बाहुप्रहरर्ण नृपः। अनुयातो महायोगिच्नेतोभिः प्राप्यते न यः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10644)
- **Original**: 17 तेनानुयातः कृष्णो5पि प्रविधेश महागुहाम्‌ । यत्न शेते महाब्रीयों मुचुकुन्दो नरेश्वर:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10645)
- **Original**: 18 जाब्रुगण भो यादवॉको पराभूत न कर सके
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10646)
- **Original**: ऐसा बिचारकर श्रौगोविन्दने समुद्रसे बारह योजन भूमि माँगी और उसमें द्वारकापुरी निर्माण की
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10647)
- **Original**: जो इन्द्रकी अपरावतौपुरीके समान महान्‌ उद्यान, गहरी खाई, सैकड़ों सरोवर तथा अनेकों महल्ोंसे सुशोचित थी। 14। कालयबनके समीष आ जातेपर श्रीजनार्दन सम्पूर्ण मधुरा- निवासियॉफ्य द्वास्कामें ले आये और फिर स्वयं मथुरा स्तैट गये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10648)
- **Original**: जब कालयबनकी सेनाने मधुराको पेर लिया तो श्रीकृष्णचन्द्र बिना शास्त्र लिये मथुरासे बाहर निकल आये। तब यबनराज कऋालयबनने उन्हें देखा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10649)
- **Original**: सहायोगीश्वरोंका चित्त भी जिन्हें प्राप्त नहीं कर पाता उन्हीं आासूदेणकों केवल याहुरूप ास्रोंसे ही युक्त [अर्थात्‌ खाली हाथ] देखकर यह उनके पीछे दौड़ा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10650)
- **Original**: काल्यबनसे पीछा किये जाते हुए श्रीकृष्णचन्द्र उस यवनेन रणे गम्ये मागधस्य भविष्यति
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10651)
- **Original**: 9 [ एक ओर जयसन्धका आक्रमण और दूसरी ओर महा गुहामें खुस गये जिसमें महालीर्यश्ञाली राजा मुचुकुन्द
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10652)
- **Original**: आ0 23 ] सोडपि प्रक्षिष्टो यखनों दूष्ठा शय्यागतं नृपम्‌ । पादेन ताडयामास मत्वा कृष्णं सुदुर्मति:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10653)
- **Original**: 19 उत्थाय मुचुकुन्दोषपि दर्दर्श यबनं नृषः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10654)
- **Original**: 20 दृष्टपात्रश् तेनासौ जज्वाल यबनो$मिना । तत्क्रोधजेन मैत्रेय भस्मीभूतश्च तत्क्षणात्‌ । 29 स हि देवासुरे युद्धे गतो हत्वा महासुरान्‌ । निद्रार्तस्सुमहाकालं निद्रां वश्ने वर सुरान्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10655)
- **Original**: 22 प्रोक्तश्न देवैस्संसुप्ते यस्त्वामुत्थापयिष्यति । देहजेनाअना सहास्स तु भस्मीभविष्यति
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10656)
- **Original**: 23 एबं दग्ध्वा स त॑ पाप॑ दृष्ठा च पधुसूदनम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10657)
- **Original**: कस्त्वमित्याह सो5प्याह जातो5ह शशिनः कुछे वसुदेवस्य तनयो . यदोरवैशसमुद्धव:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10658)
- **Original**: 24 मुचुकुन्दो5पि तत्रासौ वृद्धगार्ग्यवचो5स्मरत्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10659)
- **Original**: 25 संस्पृत्य प्रणिपत्यैंन सर्व सर्वेश्वरं हरिम्‌। प्राह ज्ञातों भवान्विष्णोरंशस्त्व॑ परमेश्वर
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10660)
- **Original**: 26 पुरा गार्म्येण कश्चितमष्टाबिशतिमे युगे। ड्वापरात्ते हरे्जन्‍्म यदुबंशे भविष्यति
- **Translation**: 

---

