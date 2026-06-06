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

### Verse 1 (Vishnu Puran 0.2061)
- **Original**: 948 पतत्तमुचादवनिर्यमुपेत्त महामतिम्‌ । दधार दैत्यपतिना क्षिप्तं स्वर्गनिवासिना
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2062)
- **Original**: 949 अवाप सह्लुर्य॑ सच्यश्चित्तस्थे मधुसूदने
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2063)
- **Original**: 150 विषाणभट्डमुन्पत्ता मदहारनिं च दियाजा: । यस्य वक्षःस्थले प्राप्ता दैल्येन्द्रपरिणामिता:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2064)
- **Original**: 159 यस्य चोत्पादिता कृत्या दैत्यराजपुरोहिते: । बभूतर नान्ताय पुरा गोविन्दासक्तचेतस:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2065)
- **Original**: 1572 झआम्बरस्य ख मायानां सहस्नमतिमायिन: । यस्मिग्रयुक्त चक्रेण कृष्णस्य वितथीकृतम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2066)
- **Original**: 953 दैल्येद्रसूदोपहते यस्य हालाहलं विषम्‌। जरयामास मतिमानविकारममत्सरी
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2067)
- **Original**: 154 समचेता जगत्यस्मिन्यः सर्वेश्षेव जन्तुषु । यथात्मनि तथान्येषां परं मैत्रगुणान्वित:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2068)
- **Original**: 155 धर्मात्मा सत्यशौर्यादिगुणानामाकर: पर: । उपमानमशेषाणां साधूनां यः सदाभवत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2069)
- **Original**: 1576 भ्रधम अंडा 73 है महाभाग ! उममें प्रह्मादजी सर्वत्र समदर्शी और जितेन्द्रिय थे, जिन्होंने श्रीविष्णुभगवान्‌की परम भक्तिका वर्णन किया था
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2070)
- **Original**: जिनक्यें टैत्यगजद्दारा दीप किये हुए अग्रिने उनके सर्वाज्भमें व्याप्त होकर भी, हृदयमें वासुदेव भगवान्‌के स्थित रहनेसे नहीं जल्म पाया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2071)
- **Original**: जिन महाबुद्धिमानके पाशवद्ध होकर समुद्रके जकूमें पड़े-पड़े इधर-ठधर हिलने-डुलनेसे सारी पृथिवी हिलने छूगी थी
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2072)
- **Original**: जिनका पर्वतके समान कठोर दारीर, सर्वत्र भगवशचित्त रहनेके कारण दैत्यराजके चलाये हुए अख्न-शब्न्रोंसे भो छिलन्न-भिन्न नहीं हुआ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2073)
- **Original**: दैत्यराजद्राय प्रेरित विषाप्रिसे प्रज्वलित मुखबाले सर्प भी जिन महातेजस्वीका अन्त नहीं कर सके
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2074)
- **Original**: जिन्होंने भगवत्स्मरणरूपी कयच धारण किये रहनेके कारण पुरुषोत्तम भगवानका स्मरण करते हुए पत्थरोंकी मार पड़नेपर भी अपने प्राणोंकोा नहीं छोड़ा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2075)
- **Original**: स्वर्गनिवासी दैत्यपतिद्वारा ऊपरसे गिराये जानेपर जिन महामतिको पृथिवीने पास जाकर बीचहीयें अपनी गोदमें धारण कर लिया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2076)
- **Original**: चित्तमें श्रीमधुसूदनभगवानके. स्थित रहनेसे दैत्पराजका नियुक्त किया हुआ सबका शोषण करनेवाल् वायु जिनके शरीरमें लगनेसे श्ञान्त हो गया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2077)
- **Original**: दैल्येन्द्रद्रा आक्रमणके लिये नियूक्त उन्मत्त दिग्गजोंके दाँत जिनके वक्षःस्थलमें लगनेसे टूट गये और उनका सारा मद चार्ण हो गया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2078)
- **Original**: पूर्वकालमें दैत्यराजके पुणेहिितोंकी उत्पत्र की हुई कृत्या भी जिन गोविन्दासक्तचित्त भक्तराजके अन्तका कारण नहीं हो सक्की
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2079)
- **Original**: जिनके ऊपर अ्रयुक्त की हुई अति मायावी शम्बरासुरकी हजारों मायाएँ श्रीकृष्णचन्द्रके चक्रसे व्यर्थ हो गयीं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2080)
- **Original**: जिन मतिमान्‌ और निर्मत्सरने दैल्यराजके रसोइयोंके लाये हुए हत्थहल विषको निर्विकार-भावसे पचा लिया
- **Translation**: 

---

