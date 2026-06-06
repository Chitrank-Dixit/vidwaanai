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

### Verse 1 (Vaivtpuran 13.11782)
- **Original**: अपने बाह्य रूप-सौन्दर्यसे साहसिकको मोहित सुस्थिर यौवनसे सम्पन्न थे। पचास कामिनियोंके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11783)
- **Original**: कर लिया। तदनन्तर बे दोनों गन्धमादनके एकान्त पति होकर सदा श्रृज्ञारमें ही तत्पर रहते थे।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11784)
- **Original**: रमणीय स्थानमें जाकर यथेच्छ विहार करने लगे। ब्रह्माजीके वरदानसे तुम्हें सुमधुर कण्ठ प्राप्त हुआ
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11785)
- **Original**: वहीं मुनिवर दुर्वासा योगासनसे विराजमान होकर था और तुम सम्पूर्ण गायकोंके राजा समझे जाते
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11786)
- **Original**: श्रीकृष्णके चरणारविन्दोंका चिन्तन कर रहे थे। थे। उन्हीं दिनों दैववश ब्रह्माका शाप प्राप्त होनेसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11787)
- **Original**: तिलोत्तमा और साहसिक उस समय कामबश तुम दासीपुत्र हुए और वैष्णवोंके अवशिष्ट
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11788)
- **Original**: चेतनाशून्य थे। उन्होंने अत्यन्त निकट ध्यान भोजनजनित पुण्यसे इस समय साक्षात्‌ ब्रह्माजीके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11789)
- **Original**: लगाये बैठे हुए मुनिको नहीं देखा। उनके पुत्र हो। अब तो तुम असंख्य कल्पोंतक जीवित
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11790)
- **Original**: उच्छूद्डल अभिसारसे मुनिका ध्यान सहसा भद्ग रहनेवाले महान्‌ वैष्णवशिरोमणि हो। ज्ञानमयी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11791)
- **Original**: हो गया। उन्होंने उन दोनोंकौ कुत्सित चेष्टाएँ दृष्टेसे सब कुछ देखते और जानते हो तथा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11792)
- **Original**: देख क्रोधमें भरकर कहा। महादेबजीके प्रिय शिष्य हो। मुने! उस पाद्म-। . दुर्वासा बोले--ओ गदहेके समान आकार-
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11793)
- **Original**: 522 « संक्षिप्त ब्रह्मवैर्तपुराण * #%%##%##### ### ## ### ## ###### कक कक ऋ कक ऋ%$%%%ऋ%%+ 55 # 68 #####%% 55% वाले निर्लज्ज नराधम! उठ। भक्तशिरोमणि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11794)
- **Original**: और चेतना नहीं रह जाती है। बलिका पुत्र होकर भी तू इस तरह पशुवत्‌। नारद! ऐसा कहकर तिलोत्तमा रोती हुई आचरण कर रहा है। देवता, मनुष्य, दैत्य, गन्धर्व
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11795)
- **Original**: दुर्वासाजीकी शरणमें गयी। भूतलपर विपत्तिमें पड़े तथा राक्षस-ये सभी सदा अपनी जातिमें [बिना भला किन्‍्हें ज्ञान होता है? उन दोनोंकी लज्जाका अनुभव करते हैं। पशुओंके सिवा सभी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11796)
- **Original**: व्याकुलता देखकर मुनिको दया आ गयी। उस मैथुन-कर्ममें लज्जा करते हैं। विशेषतः गदहेकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11797)
- **Original**: समय उन मुनिवरने उन्हें अभय देकर कहा। जाति ज्ञान तथा लज्जासे हीन होती है; अत:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11798)
- **Original**: . दुर्वासा बोले--दानव ! तू विष्णुभक्त बलिका दानवश्रेष्ट! अब तू गदहेकी योनिमें जा। [पुत्र है। उत्तम कुलमें तेरा जन्म हुआ है। तू तिलोत्तमे। तू भी उठ। पुंथली स्त्री तो निर्लज्ञ पैतृक परम्परासे विष्णुभक्त है। मैं तुझे होती ही है। दैत्यके प्रति तेरी ऐसी आसक्ति
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11799)
- **Original**: निश्चितरूपसे जानता हूँ। पिताका स्वभाव पुत्रमें है तो अब तू दानवयोनिमें ही जन्म ग्रहण कर।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11800)
- **Original**: अवश्य रहता है। जैसे कालियके सिरपर अक्डित ऐसा कहकर रोषसे जलते हुए दुर्वासामुनि
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11801)
- **Original**: हुआ श्रीकृष्णणा चरणचिह्न उसके वंशमें उत्पन्न वहाँ चुप हो गये। फिर वे दोनों लज्जित
- **Translation**: 

---

