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

### Verse 1 (Vishnu Puran 0.11261)
- **Original**: तब उसके बाद स्वप्रसे जगनेपर जब उसने उस पुरुषक न देखा तो वह उसे देखनेके लिये अत्यन्त उत्सुक होकर अपनी सख्तलीकी ओर लक्ष्य करके निर्लज्ञतापूर्वक कहते लरूगी--“हे नाथ ! आप कहाँ चले गये 2”
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11262)
- **Original**: बाणासुरकी मन्त्री कुम्भाण्ड था; उसकी चित्रलेस्ता नामकी पुत्री थी, बह उषाकी सख्त्री थी, [ उषाका यह प्रत्मप सुनकर ] उसने पूछा--'“यह तुम किसके विषयमें कह रहो हो ?'
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11263)
- **Original**: किन्तु जब लज्जावश उषाने उसे कुछ भी न बतलाया तब चित्रलेखाने [ सन बात गुप्त रखनेका ] विश्वास दिलाकर उषासे सब जुत्तात्त कहला
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11264)
- **Original**: आ0 32 ] विदितार्था तु तामाह पुनश्रोषा यथोदितम्‌। देव्या तथैव तत्पाप्तौ यो ह्युपायः कुरुच्च तम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11265)
- **Original**: 19 चि्रलेस्तेचाच दुर्विज्ेयमिर्द वक्तु प्राप्तुं वापि न शकयते । तथापि किज्ञलिल्कर्तव्यमुपकारं प्रिये तब
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11266)
- **Original**: 20 सप्राष्टदिनपर्यन्त ताबत्कालः प्रतीक्ष्यताम्‌। इत्युक्त्वाभ्यन्तरं गत्वा उपायं तमथाकरोत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11267)
- **Original**: 29 श्रीपयजगर उवाच ततः पटे सुरान्देत्यान्गन्थर्वाश्व प्रधानतः । मनुष्यांश विलिख्यास्यै चित्रलेखा व्यदर्शयत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11268)
- **Original**: 22 अपास्य सा तु गयन्धर्वास्तथोरगसुरासुरान्‌ । मनुष्येषु ददौ दृष्टिं तेघ्नप्ययकवृष्णिषु
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11269)
- **Original**: 23 कृष्णरामौ विलोक्यासीत्सुभ्ूर्ठजाजडेव सा । प्रह्मुज्नदर्शने व्रीडारदृष्टि निन्‍येउन्यतो द्विज
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11270)
- **Original**: 24 दृष्टमात्रे ततः कान्ते प्रद्युम्नतनये द्विज। दृष्ठात्यर्थवित्यसिन्या छज़जा क्लापि निराकृता
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11271)
- **Original**: 25 सो5यं सो5यपमितीत्युक्ते तया सा योगगामिनी । चित्नलेस्वाब्रबीदेनामुषां बाणसुतां तदा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11272)
- **Original**: 26 नचित्रलेखोवाच अय॑ कृष्णस्थ पौत्रस्ते भर्ता देव्या प्रसादित: । अनिरुद्ध इति ख्यात: प्रख्यात: प्रियदर्शनः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11273)
- **Original**: 27 प्राप्नोषि यदि भर्तारमिर्म प्राप्त त्वयासखिलम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11274)
- **Original**: दुष्प्रवेशा पुरी पूर्व द्वारका कृष्णपालिता
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11275)
- **Original**: 28 तथापि यत्राद्धर्तारमानयिष्यामि ते सखि
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11276)
- **Original**: रहस्यमेतद्क्तत्य॑न कस्यचिदषि त्वया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11277)
- **Original**: 29 अचिरादागमिष्यामि सहस्व विरहें मम
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11278)
- **Original**: पक्कम अंझ 397 लिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11279)
- **Original**: चित्रकेखाके सब बात जान केनेपर उषाने जो कुछ श्रीपार्वतीजीने कहा था वह भी उसे सुत्रा दिया और कहा कि अब जिस प्रकार उसका पुनः समागम हों वही उपाय करो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11280)
- **Original**: चित्रलेसाने कहा--हे प्रिये ! तुमने जिस पुरुषक्े देखा है उसे तो जानना भी यहुत कठिन है फिर उसे बतलाना या पाना कैसे हो सकता है ? तथापि मैं तुम्हारा कुछ-न-कुछ उपकार तो करूँगी ही
- **Translation**: 

---

