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

### Verse 1 (Vaivtpuran 543.14694)
- **Original**: स्त्रीका गुरु है। नाथ! ज्यों हो आप यहाँसे गये दण्डनीय अपराधीको बाँधकर लाया गया हो।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14695)
- **Original**: त्यों ही राधाको मूर्चछ्छा आ गयी। ये सहसा घाससे निकट आकर कृपानिधान श्रीकृष्णने राधाकों ढकी हुई भूमिपर गिर पड़ीं। उस समय मैंने गोदमें बिठा लिया, उन्हें सचेत किया और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14696)
- **Original**: इनके मुँहपर उत्तम शीतल जलका छींटा दिया, प्रयोधक वचनोंद्वारा समझाया। होशमें आकर देवी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14697)
- **Original**: तब इनको साँस चलने लगी और कुछ-कुछ राधाने जब प्राणवल्लभको देखा, तब वे सुस्थिर चेतना आयी। मेरी सखी क्षण-क्षणमें पुकार उठती * दम्पत्योीं: समता नास्ति यत्र यत्र हि मन्दिर । अलक्ष्मोस्तत्र तत्रेवः विफल जीवन तयो:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14698)
- **Original**: (69। 64)
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14699)
- **Original**: 638 + संक्षिप्त श्रह्मतैवर्तपुराण +* ऊकऋ$###### #
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14700)
- **Original**: # # # ## # ऋ कक ऋऊ कक क # # ## ##### ###ऋऊकऋ अ&%6#6%#### 55%: ## 8 थीं--'हे नाथ! हे कृष्ण!” फिर दूसरे हो क्षण
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14701)
- **Original**: सुखद बचन बोले। संतप्त हो रोने लगतीं और तत्काल मूर्च्छित हो श्रीभगवान्‌ने कहा--प्रिये रत्ने! यद्यपि मैं जाती थीं। राधिकाका शरौर विरहाग्रिसे संतप्त हो ईश्वर हूँ और मिलनमें बाधा डालनेवाले शापका तपायी हुई लोहेको छड़ीके समान अग्नितुल्य हो
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14702)
- **Original**: खण्डन कर सकता हूँ, तथापि ऐसा करना मेरे गया था; इसे छूआ नहीं जाता था। राधाके लिये
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14703)
- **Original**: लिये उचित नहीं है। मैं नियतिके नियमको बदला सोने और जागनेमें, दिन और रातमें, घर और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14704)
- **Original**: नहीं करता हूँ। समस्त ब्रह्मण्डोंमें मैंने जो मर्यादा बनमें, जल, थल और आकाशमें तथा चन्द्रोदय
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14705)
- **Original**: स्थापित को है, उसीका सहारा लेकर देवता, और सूर्योदयमें कोई भेद नहीं रह गया है। इनकी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14706)
- **Original**: मुनि और मनुष्य कर्म करते हैं (फिर उसको आकृति मृतकतुल्य एवं जडवत्‌ हो गयी है। ये
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14707)
- **Original**: मैं ही कैसे तोड़ दूँ)। सुन्दरि! सुदामके शापसे एक ही स्थानपर रहकर सदा सम्पूर्ण जगत्‌को
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14708)
- **Original**: हम दोनों दम्पतिको परस्पर जो कुछ समयके विष्णुमय देखती हैं: चिकने पद्कूपर कमलोंके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14709)
- **Original**: लिये वियोग प्राप्त होनेवाला है, वह यद्यपि हमें सजल पत्र बिछाकर जो शबय्या तैयार की गयी अभीष्ट नहीं है, तथापि होकर ही रहेगा। थी; उसपर ये आपके लिये विरहातुर होकर सोयी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14710)
- **Original**: सुमध्यमे! मैं राधाको वर देता हूँ। उस वरके थीं। प्यारी सखियाँ निरन्तर श्वेत चँवर डुलाकर अनुसार जाग्रतू-अवस्थामें ही इन्हें मुझसे वियोगका सेवा करने लगीं। इनके अज्ञोंपर चन्दनमिश्रित अनुभव होगा; परंतु स्वप्रमें राधाकों निरन्तर मेरा जल छिड़का गया। इनके सारे वस्त्र गीले हो
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14711)
- **Original**: आलिड्डन प्राप्त होता रहेगा। मैंने प्रियाजीको गये, तथापि राधाके अज्जोंका स्पर्श होनेमात्रसे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14712)
- **Original**: अध्यात्मकी बुद्धि प्रदान की है। उससे इनका यहाँका सारा पड्छू सूख गया। स्लिग्ध कमलदल
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14713)
- **Original**: शोक मिट जायगा। रल्रमाले! तुम्हा। कल्याण तत्क्षण जलकर भस्म हो गये। चन्दन सूख गया।
- **Translation**: 

---

