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

### Verse 1 (Vishnu Puran 0.11741)
- **Original**: 55 ततोअरध्यमादाय तदा जलथिस्सम्मुखं ययौ । प्रथिवेश ततस्तोयं पूजितः पन्नगोत्तमै:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11742)
- **Original**: 56 दृष्ठा बलस्य निर्याणं दारुक॑ प्राह केशवः । इदे सर्व समाच्रक्ष्य बसुदेबोग्रसेनयो:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11743)
- **Original**: 57 निर्याणं बलभद्गस्य यादवानां तथा क्षयम्‌ । योगे स्थित्वाहमप्येतत्परित्यक्ष्ये कलेवरम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11744)
- **Original**: 58 वाच्यश्न द्वारकावासी जनस्सर्वस्तथाहुक: । यथेमां नगरीं सर्वाँ समुद्र: प्लावयिष्यति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11745)
- **Original**: 59 तस्माद्धवद्धिस्सवैंस्तु प्रतीक्ष्यों हार्जुनागमः । न स्थेय॑ द्वारकामध्ये निष्करान्ते तत्र पाण्डजे ।। 60 डनके हाथमें रंगे हुए वे सरकण्डे वज्रके समान प्रतीत होते थे, उन बज्जतुल्य सरकण्डोंसे ही वे उस दारुण युद्धमें एक दूसरेपर प्रहार करने लगे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11746)
- **Original**: हे द्विज! प्रधुप्त और साम्ब आदि कृष्णपुत्रगण, कृतवर्मा, सात्यकि और अनिरुद्ध आदि तथा पृथु, विपृथु, चास्बर्मा, चारूक और अक्रूर आदि यादवगण एक- दूसरेपर एरकारूपी वज्जोंसे प्रहार करने लेंगे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11747)
- **Original**: जब श्रीहरिने उन्हें आपसमें लड़नेसे गेक्त्र तो उन्होंने उन्हें अपने प्रतिपक्षीका सहायक होकर आये हुए समझा और [ उनकी बातकी अवहेलनाकर ] एक-दूसरेकों मारने लगे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11748)
- **Original**: कृष्णचन्द्रने भी कुपित होकर उनका बच करनेके लिये एक मुट्ठी सरकण्डे उठा लिये। ये मुट्ठीभर हो गये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11749)
- **Original**: उन यादवॉको मारने लगे तथा अन्य समस्त यादव भी वहाँ आ-आकर एक-दूसरेको मासने छगे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11750)
- **Original**: हे द्विज ! तदनन्तर भगवान्‌ कृष्णचन्द्रका जैत्र नामक रथ घोड़ोंसे आकुृष्ट हो दारुकके देखते-देखते समुद्रके मध्यपथसे चल्प्र गया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11751)
- **Original**: इसके पश्चात्‌ भगवानके शंख, चक्र, गदा, शार्डघनुष, तरकश और खड़ड आदि आयुध श्रीहरिकी फ्रदक्षिणाकर सूर्यमार्गसे चले गये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11752)
- **Original**: है महामुने ! एक क्षणमें ही महात्मा कृष्णचद्ध और उनके सारधी दारूककों छोड़कर और कोई यदुष्घेशी जीवित न बचा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11753)
- **Original**: उन दोनोंने वहाँ घूमते हुए देखा कि श्रीबलरामजी एक वृक्षके तले बैठे हैं और उनके मुखसे एक यहुत बड़ा सर्प निकल रहा है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11754)
- **Original**: बह विज्ञाल फणधारी सर्प उनके मुखसे निकलकर सिद्ध और नागोंसे पूजित हुआ समुद्रकी ओर गया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11755)
- **Original**: उसी समय समुद्र अर्घध्य लेकर उस (महासर्प) के सम्मुख उपस्थित हुआ और वह नागश्रेष्ठोंसे पृजित हो समुद्रमें घुस गया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11756)
- **Original**: इस प्रकार श्रीबल्रामजीका प्रयाण देखकर श्रोकृष्ण- चन्द्रने दास्कसे कहा--“तुम यह सब जृत्तान्त उम्रसेन और बसुदेवजीसे जाकर कहो"
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11757)
- **Original**: बलभदजीका निर्याण, यादवोंका क्षय और मैं भी योगस्थ होकर दारीर --[ यह सब समाचार उन्हें ] जाकर सुनाओ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11758)
- **Original**: सम्पूर्ण द्वाककाजासी और आहुक (उग्रसेन) से कहना कि अब इस सम्पूर्ण नगरीको समुद्र डुनो देगा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11759)
- **Original**: इसछिये आप सब केवल अर्जुनफे आगमनकी घतीक्षा और करें तथा अर्जुनके यहाँसे लौटते
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11760)
- **Original**: अशड छछछ छउच छ7फछऊख &ल्‍ू ल्‍अश्रीविष्णुपुराण ॑॑॑॑ ऊझझ###[आ0 37 श्ड अ्रीविष्णुपुराण [ आ> 37 तेनैव सह गन्तव्यं बत्र याति स कौरवः
- **Translation**: 

---

