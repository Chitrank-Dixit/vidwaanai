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

### Verse 1 (Vaivtpuran 543.16614)
- **Original**: तेजसे उद्दी्त हो रहो थीं और उनका मुख सुबर्णकी-सी और प्रभा सैकड़ों चन्द्रमाओंके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16615)
- **Original**: लज्जावश झुक गया था। नारद! तब राजा समान थी, उनके सर्बाज्रमें चन्दनका अनुलेप
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16616)
- **Original**: भीष्यकने वेदमन्त्रोच्चारणपूर्वक दानकों विधिसे हुआ था, मालतीकी माला उनकी शोभा बढ़ा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16617)
- **Original**: देवेश्वरी रुक्मिणीको परिपूर्णतम श्रीकृष्णके हाथों रही थी और सात बालक राजकुमारोंद्वारा वे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16618)
- **Original**: सौंप दिया। उस समय हर्षपूर्वक बैठे हुए वहाँ लायी गयी थीं। ऐसी महालक्ष्मीस्वरूपा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16619)
- **Original**: श्रीकृष्णने वसुदेवजीकी आज्ञासे 'स्वस्ति' ऐसा पतित्रता रुक्मिणीदेवीको देवेन्द्रों, मुनीद्धों, कहकर रुक्मिणीदेवीकों उसी प्रकार ग्रहण कर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16620)
- **Original**: 6 2 £ 3
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16621)
- **Original**: 4369 ) 8
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16622)
- **Original**: घ 2 200 ]00700 08 । 8
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16623)
- **Original**: 3] लिया, जैसे भगवान्‌ शंकरने भवानीको ग्रहण
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16624)
- **Original**: हो रत्लनिर्मित सिंहासनोंपर आसीन थीं। वे सभी । न हा क्ज्कर 7
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16625)
- **Original**: जगदीश्वर श्रीकृष्णो निकट आया देखकर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16626)
- **Original**: अपने-अपने आसनोंसे उठ पड़ी और प्रसन्नतापूर्वक 3
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16627)
- **Original**: उन्हें एक रमणीय रत्नसिंहासनपर बैठाया। फिर पल । समागत देवाब्ताओं तथा मुनिपत्नियोंने अज्ञलि बाँधकर क्रमश: पृथक्‌-पृथक्‌ उन माधवकी >> स्तुति की। महारानी सुभद्राने वरसहित कन्याको 5757 36.
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16628)
- **Original**: भोजन कराया और सुवासित जल तथा कर्पूरयुक्त £
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16629)
- **Original**: उत्तम पान प्रदान किया। तदनन्तर वहाँ दुर्गदिवीने हडआ 25 35:2
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16630)
- **Original**: मड्भलपत्रिका दी और उनसे उसे पढ़नेके लिये किया था। इसके बाद राजाने परिपूर्णतम परमात्मा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16631)
- **Original**: कहा। तब देवियोंके उस समाजमें श्रीकृष्ण श्रीकृष्णको पाँच लाख अशर्फियाँ दक्षिणामें दीं।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16632)
- **Original**: मुस्कराते हुए उस पत्रिकाको पढ़ने लगे। (उसमें इस प्रकार मुनियों और देवेन्द्रोंकी सभामें उस
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16633)
- **Original**: लिखा था--) लक्ष्मी, सरस्वती, दुर्गा, सावित्री, शुभ कर्मके समाप्त होनेपर राजा मोहबश कन्याकों
- **Translation**: 

---

