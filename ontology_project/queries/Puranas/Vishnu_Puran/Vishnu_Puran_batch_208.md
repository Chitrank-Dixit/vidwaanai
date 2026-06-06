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

### Verse 1 (Vishnu Puran 0.4141)
- **Original**: एक दिन खे स्ानके लिये नदीपर गये और वहाँ खान करनेके अनत्तर उन्होंने स्त्रानोत्तर क्रियाएँ. कों
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4142)
- **Original**: हे ब्रह्मन्‌! इतनेहोमें ठउस नदी-तोरपर एक आसजन्रप्रसवा (शीघ्र ही बच्चा जननेबाली) प्यासी हुरिणी बार्मेसे जल पीनेके लिये आयी
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4143)
- **Original**: 148 ततः समभवत्तत्र पीतप्राये जले तथा। सिंहस्य नादः सुमहान्सर्वप्राणिभयड्ूर:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4144)
- **Original**: 14 ततः सा सहसा त्रासादाप्लुता निम्नगातटम्‌ । अत्युचारोहणेनास्या नहाां गर्भ: पपात ह
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4145)
- **Original**: 15 तमूहामान॑ वेगेन वीचिमालापरिप्रुतम्‌ जग्राह स नृषो गर्भात्यतितं मृगपोतकम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4146)
- **Original**: 16 प्रोत्तुडक्रमणेन च। मैत्रेय सापि हरिणी पषात चर ममार क्
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4147)
- **Original**: 17 हरिणीं तां विल्ोक्य्राथ विपन्नां नृपतापस: । मृगपोत॑ समादाय निजपाश्रममागतः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4148)
- **Original**: 18 चकारानुदिनं चासौं मृगपोतस्थ तै नृपः । पोषणं पुष्यमाणश्च स तेन ववृधे मुने
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4149)
- **Original**: 19 चचाराश्रमपर्यन्ते तृणानि गहनेषु सः। दूर गत्वा च शार्दूलत्रासादभ्याययों पुनः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4150)
- **Original**: 20 प्रातर्गत्वातिदूरं चर सायप्रायात्यथाश्रमम्‌ पुनश्च भरतस्थाभूदाश्रमस्योटजाजिरे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4151)
- **Original**: 21 तस्य तस्मिन्यूगे दृरसमीपपरियर्तिनि । आसीक्षेत: समासक्ते न ययावन्यतों द्विज
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4152)
- **Original**: 22 विमुक्तराज्यतनयः प्रोन्झिताशेषबान्धव: । ममत्व॑ स चअकारोचैस्तस्मिन्हरिणबालके
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4153)
- **Original**: 23 कि वृकैर्भक्षितो व्याप्रै:ः कि सिंहेन निपातित: । चिरायमाणे निष्क्रान्ते तस्यासीदिति मानसम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4154)
- **Original**: 24 एपा वसुमती तस्य सखुुराग्रक्षतकर्तुरा । प्रीतये मप जातोउसो क्व ममैणकबालकः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4155)
- **Original**: 25 विषाणाग्रेण मद्ठाहुं कण्ड्ूयनपरो हि सः । क्षेपेणाभ्यागतो5रण्यादपि मां सुखयिष्यति
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4156)
- **Original**: 26 एते लूनशझिखास्तस्यथ दशनैरचिरो ढ्तैः । कुझाः काशा विराजन्ते बटव: सामगा इब
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4157)
- **Original**: 27 इत्थे चिरगते तस्मिन्स चक्रे मानस मुनि: । भ्रीतिप्रसन्ननदनः पार्श्रत्थे चाभवन्पृगे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4158)
- **Original**: 28 श्रीविष्णुपुराण [ अ" 13 उस समय जब वह प्रायः जल पी चुकों थी, वहाँ सब अ्णियाँकों भयभीत कर देनेवाली सिंहक्त्र गम्भीर गर्जना सुनायों पड़ी
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4159)
- **Original**: तब वह अत्यन्त भयभीत हो अकस्मात्‌ उछलकर नदीके तटपर चढ़ गयी; अतः अत्यन्त उच्नस्थानपर चढ़नेके कारण उस्रका गर्भ नदीमें गिर गया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4160)
- **Original**: नदीकी तरज्ञमालाओमें पड़कर बहते हुए उस गर्भ- अष्ट मृगब्रालककों राजा भरतने पकड़ लिया
- **Translation**: 

---

