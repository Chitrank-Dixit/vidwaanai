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

### Verse 1 (Vaivtpuran 543.13734)
- **Original**: मधुर है। प्राचीन कालकी बात है। इन्द्र सौ शिवके यश तथा दैववश उनके दर्प-भड्डको बात
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13735)
- **Original**: यज्ञोंका अनुष्ठान करके समस्त देवताओंके स्वामी सुनी । पार्वतीके गर्वभंजनका और शिव-पार्वतीके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13736)
- **Original**: तथा महान्‌ ऐश्वर्यसे सम्पन्न हो गये। तपस्याके विवाहका भी वर्णन सुना। अब इन्द्रके तथा अन्य
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13737)
- **Original**: फलसे प्रतिदिन उनके ऐश्वर्यकी वृद्धि होने लगी। लोगोंके भी अभिमानके चूर्ण होनेके प्रसज्जोंको बृहस्पतिजीने उन्हें सिद्ध-मन्त्रकी दीक्षा दी। क्रमश: सुनना चाहती हूँ; कृपया विस्तारपूर्वक कहें। उन्होंने पुष्करमें सौ वर्षोतक उस महामन्त्रका जप श्रीकृष्ण बोले--सुन्दरि! इन्द्रके दर्प-
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13738)
- **Original**: किया। जपसे वह मन्त्र सिद्ध हो गया और इनका भड्ढकी बात तीनों लोकॉंमें प्रसिद्ध है। वह प्रसड्भ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13739)
- **Original**: मनोरथ पूरा हुआ। मनुष्य सम्पत्तिसे मोहित हुआ सुन्दर, अनुपम तथा कानोंके लिये अमृतके समान
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13740)
- **Original**: ब्रह्मस्वरूपा प्रकृतिका आदर नहीं करता; अत:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13741)
- **Original**: + श्रीकृष्णजन्मखण्ड « 597 442202202020000002002 22 00/0 224 24 200 482/ 00 4/442 88 4400 40000 44 40444 44444. 8
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13742)
- **Original**: प्रकृतिने इन्द्रको शाप दे दिया। इसीलिये उन्हें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13743)
- **Original**: इन्द्रने भयभीत होकर मुनिके चरण पकड़ लिये। अपने गुरुकी ओरसे भी अत्यन्त क्रोधपूर्वक शाप
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13744)
- **Original**: तब गौतमजीने कुपित होकर उनसे कहा। मिला। एक दिन इन्द्र अपनी सभामें बैठे थे।। गौतम बोले--इन्द्र! तुझे घिक्कार है। तू प्रकृतिके शापसे उनकी बुद्धि मारी गयी थी; अत:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13745)
- **Original**: देवताओंमें श्रेष्ठ समझा जाता है। कश्यपजीका वे गुरुको आते देखकर भी न तो उठे और न
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13746)
- **Original**: पुत्र है; ज्ञानी है और जगत्स्ष्टा ब्रह्माजीका प्रपौत्र प्रसन्नतापूर्वक उन्हें प्रणाम ही किया। यह देख
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13747)
- **Original**: है तो भी तेरी ऐसी बुद्धि कैसे हो गयी? जिसके बृहस्पतिजी क्रोधसे युक्त हो उस सभामें नहीं
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13748)
- **Original**: नाना साक्षात्‌ प्रजापति दक्ष हैं और माता पतिक्रता बैठे, उलटे पाँव घर लौट आये। वहाँ भी वे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13749)
- **Original**: अदिति देवी हैं, उसका इतना पतन आश्चर्यकी ताराके निकट नहीं ठहरे, तपस्याके लिये बनमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13750)
- **Original**: बात है! तू वेदोंका ज्ञान प्राप्त करके ज्ञानी चले गये। उन्होंने मन-ही-मन दुःखी होकर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13751)
- **Original**: कहलाता है; किंतु कर्मसे योनि-लम्पट है; अतः कहा--'इन्द्रकी सम्पत्ति चली जाय।' तदनन्तर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13752)
- **Original**: तेरे शरीरमें एक सहस््र योनियाँ प्रकट हो जाय॑ँ। इन्द्रकों सुबुद्धि प्राप्त हुह और वे बोले--'मेरे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13753)
- **Original**: पूरे एक वर्षतक तुझे सदा योनिकौ हो दुर्गन्ध स्वामी यहाँसे कहाँ चले गये।' ब्राप्त होती रहेगी। तत्पश्चात्‌ सूर्यकी आराधना यों कहकर बे बेगपूर्वक सिंहासनसे उठे और
- **Translation**: 

---

