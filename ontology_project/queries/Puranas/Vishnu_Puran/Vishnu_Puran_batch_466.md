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

### Verse 1 (Vishnu Puran 0.9301)
- **Original**: 6 तेनेय॑ दूषिता सर्वा यमुना सागरड्रमा। न॒ नरैगेोधिनैश्वापि तृषातैरुपभुज्यते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9302)
- **Original**: 7 तदस्य नागराजस्यथ कर्तव्यों निग्रहो मया। निखासास्तु सुर्ख॑ येन चरेयुर््रेजबासिन:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9303)
- **Original**: 8 एतदर्थ तु लोकेउस्मिन्नवतार: कृतो मया .। यदेषामुत्पथस्थानां कार्या शान्तिर्दुरात्मनाम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9304)
- **Original**: 9 तदेत॑ नातिदूरस्थे कदम्बमुरुशआस्ििनम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9305)
- **Original**: अधिरुह्य पतिष्यामि हृदेउस्मिन्ननिलाशिनः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9306)
- **Original**: 10 श्रीपराशर उवाच इत्थं विचित्त्य बद॒ध्वा च गाढं परिकर तत: । निपपात हुदे तत्र नागराजस्थ लेगतः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9307)
- **Original**: 19 तेनातिफ्तता तत्र क्षोभितस्स . महाहुदः । अत्यर्थ दूरजातांस्तु समसिश्नन्महीरुहान्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9308)
- **Original**: 12 काकछचियनागका महाभयकर कुण्ड देखा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9309)
- **Original**: उसकी विषाग्रिके प्रसारसे किनारेके वृक्ष जल गये थे और वायुके थपेड़ोंसे उछलते हुए जलकणोंका स्पर्श होनेसे पक्षिगण दग्ध हो जाते थे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9310)
- **Original**: मृत्युक॑ अपर मुखके समान उस महाभर्यंकर कुण्डको देखकर भगवान्‌ मधुसूदनने विचार फिया--
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9311)
- **Original**: “इसमें दुष्टात्मा कालियनाग रहता है जिसका विष ही शास्त्र है और जो दुष्ट मुझ ! अर्थात्‌ मेरी विभूति गरुड ] से पराजित हो समुद्रको छोड़कर भाग आया है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9312)
- **Original**: इसने इस समुद्रगामिती सम्पूर्ण यमुनाकों दूषित कर दिया है, अब इसका जल प्यासे मनुष्यों और गौओंके भी काममें नहीं आता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9313)
- **Original**: अतः मुझे इस नागराजका दमन करना चाहिये, जिससे ब्रजवासी लोग निर्भय होकर सुख्रपूर्वक रह सकें
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9314)
- **Original**: “इन कुमार्गगामी दुरात्माओऑंकों श्ान्त्त करना चाहिये, इसलिये हो तो मैंने इस लोकमें अवतार लिया है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9315)
- **Original**: अतः अब मैं इस ऊँयी-ऊँची शाखाओवाले पासहीके कदम्बवृक्षपर घढ़कर बायुभक्षी नागराजके कुण्डमें कूदता हैँ.
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9316)
- **Original**: श्रीपराशरजी बोले--हे मैत्रेय ! ऐसा विचारकर भगवान्‌ अपनी कमर कसकर बेगपूर्वक नागराजके कुप्छमें कूद पड़े
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9317)
- **Original**: डनके कूदनेसे उस महाहृदने अत्यन्त द्योभित होकर दूरस्थित वृक्षोंको भो भिगो दिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9318)
- **Original**: 326 श्रीविष्णुपुराण ( आ* 7 तेअहिदुष्टविषज्वालातप्राम्नुपवनोक्षिता:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9319)
- **Original**: जज्वलु: पादपास्सशो ज्वाल्गव्याप्तदिगन्तरा:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9320)
- **Original**: 13 आस्फोटबामास तदा कृष्णो नागहदे भुजप्‌ । तच्छब्दश्रवणाधाशु नागराजो5भ्युपागमत्‌
- **Translation**: 

---

