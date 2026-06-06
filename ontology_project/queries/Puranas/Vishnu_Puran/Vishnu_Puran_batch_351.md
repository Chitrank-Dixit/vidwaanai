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

### Verse 1 (Vishnu Puran 0.7001)
- **Original**: उनके साथ ही जो अयोध्यानियासी उन भगवर्दशास्वरूपोंके अतिशय अनुरागी थे उन्होंने भी तन्‍्मये होनेके कारण सालोक्य-सुक्ति प्राप्त की
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7002)
- **Original**: दृष्ट-दलन भगवान्‌ रामके क़ुश और लव नामक दो पुत्र हुए। इसी प्रकार लक्ष्मणजीके अद्भद और चद्रकेतु, भरतजीके तक्ष और पुष्कल तथा शर््रुघ्रजीके सुबाहु और आरसेन नामक पुत्र हुए
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7003)
- **Original**: कुशके अतिथि, अतिथिके निषध, निषधके अनल, अनलके नभ, नभके पुण्डरीक, पुण्डरीकके क्षेमधन्वा, क्षेमघन्लाके देखानीक, देखानीककेे अहीनक, अहीनकके रुझु, रुझके पारियात्रक, पारियाक़कके देवर, देखलके वंघल, खसघल्के उत्क, उत्कके वद्जनाभ, वज़्नाभके शद्भगण, शब्ब॒णके युषिताश्र॒ और यूषिताश्रके विश्वसह नामक पूत्र हुआ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7004)
- **Original**: 105-106
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7005)
- **Original**: विश्वसहके हिरण्यनाभ नामक पुत्र हुआ जिसने जैमिनिके शिष्य महायोगीश्वर याज़वल्क्यजीसे योगविद्या प्राप्त की थी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7006)
- **Original**: हिएण्यनाभका पुत्र पुष्य था, उसका धुबसन्धि, घुबसन्धिका सुदर्शन, सुदर्शनका अग्निवर्ण, अग्निवर्णका शोघग तथा दीघ्रगका पुत्र मर हुआ जो इस समय भी योगाभ्यासमें तत्पर हुआ कल्मपग्राममें स्थित है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7007)
- **Original**: 108-109
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7008)
- **Original**: आगामी युगमें यह सूर्यवंशीय क्षत्रियोंका प्रवर्तक होगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7009)
- **Original**: मरूका पुत्र प्रसुश्रुत, प्रसुश्नुतका सुसन्धि, सुसन्थिका अमर्ष, अमर्षका सहस्वान्‌, सहस्वानका विश्वभव तथा बकिश्वभमवका पुत्र बृहद्वल हुआ जिसको भारतीय युद्धमें अर्जुनके पुत्र अभिमन्युने मारा था
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7010)
- **Original**: 111-112
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7011)
- **Original**: इस प्रकार मैंने यह इक्ष्वाकुकुलके प्रधान-प्रधान राजाओंका वर्णन किया। इनका चरित्र सुननेसे मनुष्य सकल पापोसे मुक्त हो जाता है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7012)
- **Original**: मा इति श्रीविष्णुपुराणे चतुर्थेडशे चतुर्थोष्ध्याय:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7013)
- **Original**: कि" पु 9 -+ «*_..- जैर “+++>
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7014)
- **Original**: श्रीविष्णुपुराण पाँचवाँ अध्याय निमि-चरित्र और निमिंधाका वर्णन श्रीपााशर उवाच इक्बाकुतनयों योउसौ निर्मिनाम सहर्त्न वत्सरे सत्रमारेभे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7015)
- **Original**: वसिष्ठ॑ च होतार॑ वरयापास
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7016)
- **Original**: तमाह वसिष्ठोहहमिद्रेण पश्चवर्षशत- यागार्थ प्रथम वृत:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7017)
- **Original**: तदनन्तरं प्रतिपाल्यता- मागतस्ततवरापि ऋत्विगभविष्यामीत्युक्ते स पृथिवीपतिर्न किख्ितुक्तवान्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7018)
- **Original**: वसिष्लोउप्यनेन. समन्वीष्सितमित्यमरपते- यागमकरोत्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7019)
- **Original**: सो5पि तत्काल एबान्यैगौत- मादिभिर्यागमकरोत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7020)
- **Original**: समाप्ते चामरपतेर्यागे त्वरया वसिष्ठो निमियज्ञं करिष्यामीत्याजगाम
- **Translation**: 

---

