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

### Verse 1 (Vaivtpuran 543.12474)
- **Original**: वहीं सब ओरसे गोलाकार रासमण्डल बनाया प्रसन्न मुखसे उन्होंने कथा सुनाना आरम्भ किया।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12475)
- **Original**: गया था, जो नाना प्रकारके फूलों और मालाओंसे श्रीनारायण बोले--मुने ! एक दिन श्रीकृष्ण
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12476)
- **Original**: सुस॒ज्जित था। चन्दन, अगुरु, कस्तूरी और केसरसे चैन्रमासके शुक्लपक्षकी त्रयोदशी तिथिको चन्द्रोदय
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12477)
- **Original**: वहाँकी भूमिका संस्कार किया गया था। रासमण्डलके होनेके पश्चात्‌ बृन्दावनमें गये। उस समय जूही,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12478)
- **Original**: चारों ओर फूलोंसे भरे उद्यान तथा क्रीड़ासरोवर मालती, कुन्द और माधवाके पुष्पोंका स्पर्श करके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12479)
- **Original**: थे। उन सरोवरोंमें हंस, कारण्डव तथा जलकुकुट
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12480)
- **Original**: » भ्रीकृष्णजन्मखण्ड + पड अंक %$# 6 # 6 # & # & & % # ऋ# &%& %ऋ % & ####ऋऋ#ऊऋऋऊऋऋकऋऋऋ 44 4 ## ## 4 6 ## ##ऋ#ऋ## 4 #%#ऋकऋ हक 44 $ 4968 ##%#ऋ आदि पक्षी कलरव कर रहे थे। वे जलक्रौड़ाके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12481)
- **Original**: यह एक अद्भुत बात थी। चारों ओर देखकर योग्य सुन्दर तथा सुरत-श्रमका निवारण करनेवाले
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12482)
- **Original**: वंशीध्यनिका अनुसरण करती हुई आगे बढ़ीं। थे। उनमें शुद्ध स्फटिकमणिके समान स्वच्छ तथा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12483)
- **Original**: मन-ही-मन महात्मा श्रीकृष्णके चरणारविन्दोंका निर्मल जल भरा था। उस रासमण्डलमें दही,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12484)
- **Original**: चिन्तन करती जाती थीं। वे अपने सहज तेज अक्षत और जल छिड़के गये थे। केलेके सुन्दर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12485)
- **Original**: तथा श्रेष्ठ रत्रसारमय भूषणोंकी कान्तिसे वनप्रान्तको खम्भोंद्वारा वह चारों ओरसे सुशोभित था। सूतमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12486)
- **Original**: प्रकाशित कर रही थीं। राधिकाकी सुशीला आदि बँधे हुए आमके पह्लवोंके मनोहर बन्दनवारों तथा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12487)
- **Original**: जो अत्यन्त प्यारी तैंतीस सख्ियाँ थीं और समस्त सिन्दूर, चन्दनयुक्त मड्गल-कलशॉसे उसको सजाया
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12488)
- **Original**: गोपियोंमें श्रेष्ठ समझी जाती थीं; वे भी श्रीकृष्णके गया था। मज्गलकलशोंके साथ मालतीकी मालाएँ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12489)
- **Original**: दिये हुए बरसे आकृष्ट-चित्त हो डरी हुई-सी और नारियलके फल भी थे। उस शोभासम्पन्न
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12490)
- **Original**: घरसे बराह' निकलीं। कुलधर्मका त्याग करके रासमण्डलकों देखकर मधुसूदन हँसे। उन्होंने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12491)
- **Original**: निःशड्डू हो वनकी ओर चलीं। वे सब-कौ- कौतूहलवश वहाँ बिनोदकी साधनभूता मुरलीको
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12492)
- **Original**: सब प्रेमातिरिकसे मोहित थीं। फिर उन प्रधान कसर थीं, वैसे ही--लाखोंकी संख्यामें निकल पड़ीं। ये सब बनमें एक स्थानपर इकट्टी हुईं और कुछ देरतक प्रसन्नतापूर्वक वहीं खड़ी रहीं। वहाँ कुछ गोपियाँ अपने हाथोंमें माला लिये आयी थीं। कुछ गोपाडुनाएँ व्रजसे मनोहर चन्दन हाथरमें लेकर वहाँ पहुँची थीं। कई गोपियोंके हाथोंमें बजाया। वह वंशीकी ध्वनि उनकी प्रेयसी गोपाड्रनाओंके प्रेमको बढ़ानेवाली थी। (22 राधिकाने जब वंशीकी मधुर ध्वनि सुनी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12493)
- **Original**: #// तो तत्काल ही वे प्रेमाकुल हो अपनी सुध- बुध खो बैठीं। उनका शरीर ढूँठे काठकौ तरह
- **Translation**: 

---

