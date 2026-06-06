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

### Verse 1 (Vishnu Puran 0.4021)
- **Original**: नम, है $ रकम बारहवाँ अध्याय नवग्रहोंका वर्णन तथा लोकान्तरसम्बन्धी व्याख्यानका उपसंहार श्रीपराज्षर उवाच रथख्नरिचक्र: सोमस्य कुन्दाभास्तस्य वाजिन: । श्रीपराशरजी बोले--चन्द्रमाका रथ तीन
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4022)
- **Original**: पहियोवाला है, उसके बाम तथा दक्षिण ओर कुल्द- वामदक्षिणतो युक्ता दश तेन चरत्यसौ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4023)
- **Original**: कुसुमके समान श्वेतवर्ण दस घोड़े जुते हुए हैं। घुवके वीध्याश्रयाणि ऋक्षाणि घुवाधारेण वेगिना । हासवृद्धिक्रमस्तस्थ रइमीनां सवितुर्यथा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4024)
- **Original**: 2 अर्कस्पेव हि तस्याश्वा: सकृद्युक्ता वहन्ति ते । कल्पमेक॑ मुनिश्नेष्ठ वारिगर्भसमुद्धवा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4025)
- **Original**: 3 क्षीण पीत॑ सुरैः सोममाष्याययति दीप्रिपान्‌ । मैत्रेयेककर्ल सन्‍्ते रश्मिनेकेन भास्कर:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4026)
- **Original**: 4 क्रमेण येन पीतोउसो देवैस्तेन निशाकरम्‌ । आप्याययत्यनुदिन॑ भास्करो बारितस्करः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4027)
- **Original**: 5 सम्भृत॑ चार्थमासेन तत्सोमस्थे सुधामृतम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4028)
- **Original**: पिबन्ति देवा पैश्रेय सुधाहारा यतोहमरा:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4029)
- **Original**: 6 ज्रयस्मिंशत्सहसत्राणि अयस्थविंशच्छतानि कन । अयख्यिंशत्तथा देवा: पिबन्ति क्षणदाकरम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4030)
- **Original**: 7 कलाहयाबशिष्टस्तु प्रव्िष्ट: सूर्यमण्डलम्‌। अमाख्यरइ्मौ बसति अम्ताबास्या ततः स्मृता
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4031)
- **Original**: 8 अप्सु तस्मिन्नहोरात्रे पूर्व विशति चन्द्रमा: । ततो वीरुत्सु बसति प्रयात्यक तत: क्रमातू
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4032)
- **Original**: 9 छिनत्ति वीरुधो यस्तु वीरुत्संस्थे निशाकरे । पत्र वा पातयत्येक॑ ब्रह्महत्यों स विन्दति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4033)
- **Original**: 10 सोम॑ पछदएशे भागे किश्निच्छिप्टे कल्म्रत्मके । अपराहे पितृगणा जघन्य पर्युपासते
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4034)
- **Original**: 11 आधारपर स्थित उस वेगशाली रथसे चन्द्रदेव भ्रमण करते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4035)
- **Original**: है और नागवीथिपर आश्रित अश्विनी आदि नक्षत्रोंक्रा भोग करते हैं। सूर्यके समान इनकी किरणोंके भी घटने- बढ़नेका निश्चित क्रम है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4036)
- **Original**: हे सुनिश्रेष्ठ ! सूर्यके समान समुद्रगर्भसे उत्पन्न हुए उसके घोड़े भी एक यार जोत दिये जानेपर एक कल्पपर्यन्त रथ खींचते रहते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4037)
- **Original**: है मैत्रेय ! सुरगणके पान करते रहनेसे क्षीण हुए कलामात्र चन्द्रमाका प्रकाशमय सूर्यदेक अपनी एक किरणसे पुनः पोषण करते हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4038)
- **Original**: जिस क्रमसे देवगण चन्द्रमाका पान करते हैं उसी क्रमसे जल्लापहारी सूर्यदेव उन्हें शुह्ता प्रतिपदासे प्रतिदिन पुष्ट करते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4039)
- **Original**: हे सैत्रेय ! इस प्रकार आधे महीनेमें एकत्रित हुए चद्रमाके अमृतक्य देवगण फिर पीने लगते हैं क्योंकि देवताओंका आहार तो अमृत हो है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4040)
- **Original**: लैंतीस हजार, तैंतीस सौ, तैंतीस (36333) देवगण चत्रस्थ अपृतका पान करते हैं
- **Translation**: 

---

