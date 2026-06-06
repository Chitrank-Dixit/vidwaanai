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

### Verse 1 (Vishnu Puran 0.1981)
- **Original**: टम्यासे घोष, यामीसे नागवीथी और अरुन्तौसे समस्त पृथिवी- विषयक प्राणी हुए तथा सदूरूपासे सर्बात्मक सड्भल्पकी उत्पत्ति हुई
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1982)
- **Original**: 107-108
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1983)
- **Original**: नाना प्रकारका वस्तु (तेज अथना घन) ही जिनका प्राण है ऐसे ज्योति आदि जो आठ वसुगण विज्यात हैं, अब मैं उनके वंद्ाका विस्तार बतात हूँ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1984)
- **Original**: उनके नाम आप, घुव, सोम, धर्म, अनिल (वायु), अनल (अग्नि), प्रत्यूष और प्रभास कहे जाते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1985)
- **Original**: आपके पूत्र वैतण्ड, श्रम, शान्त और ध्यनि हुए तथा धुक्‍के पुत्र लोक-संहारक भगवान्‌ काल हुए
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1986)
- **Original**: भगवान्‌ वर्चा सोमके पुत्र थे जिनसे पुरुष वर्चस्वी (तेजस्वी) हो जाता है और धर्मके उनकी भार्या मनोहरासे द्रविण, हुत एवं हज्यवह तथा शिशिर, प्राण और वरुण नामक पुत्र हुए्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1987)
- **Original**: 112-113
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1988)
- **Original**: आ0 15 ] प्रथम अंश 54 34 अविवननिनननिनिककििनककी,.... . .......अ ििककककक... _ अनिलमस्य झ्षिवा भार्या तस्या: पुत्रो पनोजबः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1989)
- **Original**: अविज्ञातगतिश्षैव द्रौ पुत्रनावनिलस्य तु
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1990)
- **Original**: 114 अभ्निपुत्र: कुमारस्तु शरस्तम्बे व्यजायत । तस्य शाखो विशाखश्न नैगमेयश्न पृष्ठजा:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1991)
- **Original**: 195 अप कृत्तिकानां तु कार्त्तिकेय डति स्मृत:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1992)
- **Original**: 116 दिदु: पुत्रे ऋषि नाम्नाथ देवलम्‌ । द्जै पुत्री देवलस्पापि क्षमावन्तौ मनीषिणों
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1993)
- **Original**: 117 बृहस्पतेस्तु भगिनी वरस्त्री ब्रहाचारिणी । योगसिद्धा जगत्कृत्सत्रमसक्ता विचरत्युत । प्रभासस्य तु सा भार्या वसूनामष्टमस्य तु
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1994)
- **Original**: 118 विश्वकर्मा महाभागस्तस्यां जज्ले प्रजापति: । कर्ता शिल्पसहल्नाणां त्रिदशानां च वर्द्धकी
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1995)
- **Original**: 119 भूषणानां च सर्वेधां कर्ता शिल्पवर्ता वर: । यः सर्वेषां विमानानि देवतानां चकार ह । मनुष्याओ्रोपजीवन्ति यस्य शिल्प महात्मन:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1996)
- **Original**: 120 तस्य पुत्रास्तु ऋत्वारस्तेषां नामानि में धृणु । स्द्धश्ष वीर्यवान्‌ । त्वपुक्षाप्यात्मज: पुत्रो विश्वरूपो महातपा:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1997)
- **Original**: 121 हरश्ल॒ बहुरूपश्च॒ त्र्यम्बकआआपराजित: । वृषाकपिश्न शम्मुश्न कपर्दी रैबतः स्पृत:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1998)
- **Original**: 122 मृगव्याधश्ष शर्वभ्ञ कपाली चर महामुने । एकाददौते कथिता रुद्राखिभुवनेश्वरा: । शर्त स्वेके समाख्यात॑ रुद्राणाममितौजसाम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1999)
- **Original**: 123 कश्यपस्य तु भार्या यास्तासां नामानि मे शरूणु । अदितिर्दितिर्दनुश्ैबारिष्टा च सुरसा ख़सा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2000)
- **Original**: 124 सुरभिर्विनता चैव ताम्रा क्रोधवशा इरा । कहूर्मुनिश्न धर्मज्ञ तदपत्यानि मे श्रूणु
- **Translation**: 

---

