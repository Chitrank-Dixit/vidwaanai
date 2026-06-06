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

### Verse 1 (Vaivtpuran 543.12494)
- **Original**: स्थिर और चित्त ध्यानमें एकतान हो गया।।।19 क्षणभरमें चेत होनेपर पुनः मुरलीकी ध्वनि उनके कानोंमें पड़ी। वे बैठी थीं, फिर उठकर खड़ी "गा 5 हो गयां। अब उन्हें बार-बार उद्देग होने लगा,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12495)
- **Original**: साथ वहाँ आयी थीं। कुछ गोपकन्याएँ कुंकुम, वे आवश्यक कर्म छोड़कर घरसे निकल पड़ीं।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12496)
- **Original**: ताम्बूल-पात्र तथा काझ्नन, वस्त्र लिये आयी थीं।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12497)
- **Original**: प्ड्ट * संक्षिप्त ब्रह्मवैव्॑तपुराण « %##%###%4# 8 ####%#%$#%##%# %####### 8 अंक कंकऋकऋककऋकऋऋकऋकऋऋ कक # 4 4 कक कक के कुछ शीघ्रतापूर्वक उस स्थानपर आयोीं, जहाँ। श्रीराधाने भी किशोर अवस्थासे युक्त चन्द्रावली (राधा) सानन्द खड़ी थीं। वे सब
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12498)
- **Original**: श्यामसुन्दकी ओर दृष्टिपात किया। वे नूतन एकत्र हो प्रसन्नतापूर्वक मुस्कराती हुईं वहाँ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12499)
- **Original**: यौवनसे सम्पन्न तथा रत्रमय आभरणोंसे विभूषित राधिकाकी वेशभूषा सँवारकर बड़े हर्षके साथ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12500)
- **Original**: थे। करोड़ों कामदेवॉकी लावण्यलीलाके मनोहर आगे बढ़ीं। मार्गमें बारंबार वे हरि-नामका जप
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12501)
- **Original**: धाम प्रतीत होते थे और बाँके नयनोंसे उनकी करती थीं। बृन्दाबनमें पहुँचकर उन्होंने रमणीय
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12502)
- **Original**: ओर निहारती हुई उन प्राणाधिका राधिकाकों देख रासमण्डल देखा, जहाँका दृश्य स्वर्गसे भी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12503)
- **Original**: रहे थे। उनके परम अद्भुत रूपकी कहीं उपमा अधिक सुन्दर था। चन्द्रमाकी किरणें उस
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12504)
- **Original**: नहीं थी। वे विचित्र वेशभूषा तथा मुकुट धारण बनप्रान्तको अनुरञ्ञित कर रही थीं। अत्यन्त
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12505)
- **Original**: किये सानन्द मुस्करा रहे थे। बाँके नेत्रोंक कोणसे निर्जन, विकसित कुसुमोंसे अलंकृत तथा फूलोंकों
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12506)
- **Original**: बार-बार प्रीतमकी ओर देख-देखकर सती राधाने छूकर प्रवाहित होनेवाली मलयबायुसे सुबासित
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12507)
- **Original**: लज्ञावश मुखको आँचलसे ढक लिया और वे वह रम्य रासमण्डल नारियोंके प्रेमभावको जगानेवाला
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12508)
- **Original**: मुस्कराती हुई अपनी सुध-बुध खो बैठीं। और मुनियोंके भी मनको मोह लेनेवाला था।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12509)
- **Original**: प्रेममावका उद्दीपन होनेसे उनके सारे अड्भ उन सबको वहाँ कोकिलोंकी मधुर काकली
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12510)
- **Original**: पुलकित हो उठे। तदनन्तर श्रीकृष्ण एवं राधिकाका सुनायी दी। भ्रमरोंका अत्यन्त सूक्ष्म मधुर गुझ्ारव
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12511)
- **Original**: परस्पर प्रेम-शृज्जार हुआ। भी बड़ा मनोहर जान पड़ता था। वे भ्रमर मुने! नौ लाख गोपियाँ और उतने ही गोप- भ्रमरियोंके साथ रह फूलोंका मकरन्द पान करके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12512)
- **Original**: विग्रहधारी श्यामसुन्दर श्रीकृष्ण-ये अठारह लाख मतवाले हो गये थे। गोपी-कृष्ण रासमण्डलमें परस्पर मिले। नारद! तदनन्तर शुभ वेलामें सम्पूर्ण सखियोंके साथ
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12513)
- **Original**: वहाँ कड्ढूणों, किड्छिणियों, वलयों और श्रेष्ठ रत्न- श्रीकृष्णके चरणकमलोंका चिन्तन करके श्रीराधिकाने
- **Translation**: 

---

