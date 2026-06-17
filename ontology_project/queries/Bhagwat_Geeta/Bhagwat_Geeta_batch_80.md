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

### Verse 1 (Bhagwat_Geeta 31.394)
- **Original**: अर्जुन बोले-हे कृष्ण
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 31.395)
- **Original**: तो फिर यह मनुष्य स्वयं न चाहता हुआ भी बलात्‌ लगाये हुएकी भाँति किससे प्रेरित होकर पापका आचरण करता है 2
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 31.396)
- **Original**: श्रीभयवानुवाच काम एष क्रोध एव रजोगुणसमुद्धव:। महाशनो महापाप्मा विद्धयेनमिह वैरिणम्‌
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 31.397)
- **Original**: * अध्याय 31% 59 श्रीभगवान्‌ बोले--रजोगुणसे उत्पन्न हुआ यह काम ही क्रोध है, यह बहुत खानेवाला अर्थात्‌ भोगोंसे कभी न अघानेवाला और बड़ा पापी है, इसको ही तू इस विषयमें वैरी जान
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 31.398)
- **Original**: धूमेनात्रियते वह्िर्यथादर्शों मलेन च। यथोल्बेनावृतो गर्भस्तथा तेनेदमावृतम्‌
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 31.399)
- **Original**: जिस प्रकार धूएँसे अग्नि और मैलसे दर्पण ढका जाता है तथा जिस प्रकार जेरसे गर्भ ढका रहता है, वैसे ही उस कामके द्वारा यह ज्ञान ढका रहता है
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 31.400)
- **Original**: आवृतं ज्ञानमेतेन ज्ञानिनो नित्यवैरिणा। कामरूपेण कौन्‍्तेय दुष्प्रेणानलेन च
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 31.401)
- **Original**: और हे अर्जुन! इस अग्निके समान कभी न पूर्ण होनेवाले कामरूप ज्ञानियोंके नित्य वैरीके द्वारा मनुष्यका ज्ञान ढका हुआ है
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 31.402)
- **Original**: इन्द्रियाणि मनो बुद्धद्विरस्याधिष्ठानमुच्यते। एतैर्विमोहयत्येष ज्ञानमावृत्य देहिनम्‌
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 31.403)
- **Original**: इन्द्रियाँ मन और बुद्धि--ये सब इसके वासस्थान कहे जाते हैं। यह काम इन मन, बुद्धि और इन्द्रियोंके द्वारा ही ज्ञानको आच्छादित करके जीवात्माको मोहित करता है
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 31.404)
- **Original**: 60 * श्रीमद्धगवद्रीता * तस्मात्त्वमिन्द्रियाण्यादौ नियम्य भरतर्षभ। पाप्मानं प्रजहि होनं ज्ञानविज्ञाननाशनम्‌
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 31.405)
- **Original**: इसलिये हे अर्जुन! तू पहले इन्द्रियोंको वशमें करके इस ज्ञान और विज्ञानका नाश करनेवाले महान्‌ पापी कामको अवश्य ही बलपूर्वक मार डाल
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 31.406)
- **Original**: इन्द्रियाणि पराण्याहुरिन्द्रियेभ्य: परे मनः। मनसस्तु परा बुद्ध्रियों बुद्धेः परतस्तु सः
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 31.407)
- **Original**: इन्द्रियोंको स्थूल शरीरसे पर यानी श्रेष्ठ, बलवान्‌ और सूक्ष्म कहते हैं; इन इन्द्रियोंसे पर मन है, मनसे भी पर बुद्धि है और जो बुद्धिसे भी अत्यन्त पर है वह आत्मा है
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 31.408)
- **Original**: एवं बुद्धेः परे बुद्ध्वा संस्तभ्यात्मानमात्मना । जहि शत्रुं महाबाहो कामरूपं दुरासदम्‌
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 31.409)
- **Original**: इस प्रकार बुद्धिसे पर अर्थात्‌ सूक्ष्म, बलवान्‌ और अत्यन्त श्रेष्ठ आत्माको जानकर और बुड्ठिके द्वारा मनको वशमें करके हे महाबाहो! तू इस कामरूप दुर्जय शत्रुको मार डाल
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 31.410)
- **Original**: 3» तत्सदिति श्रीमद्धगवद्गीतासूपनिषत्सु ब्रह्मविद्यायां योगशास्त्रे श्रीकृष्णार्जुनसंवादे कर्मयोगो नाम तृतीयो5ध्याय:
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 31.411)
- **Original**: व्ल्ल् () व्तत>
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 31.412)
- **Original**: अथ चदुर्थोड ध्याय: श्रीभयवानुवाच इमं विवस्वते योगं प्रोक्तवानहमव्ययम्‌। विवस्वान्मनवे प्राह मनुरिक्ष्वाकवे5ब्रवीत्‌
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 31.413)
- **Original**: श्रीभगवान्‌ बोले-मैंने इस अविनाशी योगको सूर्यससे कहा थ; सूर्यने अपने पुत्र वैवस्वत मनुसे कहा और मनुने अपने पुत्र राजा इक्ष्वाकुसे कहा
- **Translation**: 

---

