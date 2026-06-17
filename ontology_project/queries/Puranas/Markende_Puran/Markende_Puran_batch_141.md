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

### Verse 1 (Markende Puran 0.2801)
- **Original**: दैत्येश्वर! मुत्युकी उत्क्रान्तिदा नामवालों शक्ति भी आपने छोन ली हैं तथा रंगन्का हो गया, अत: वे हिमालवपर रहनेवालों
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2802)
- **Original**: वरुणका पाश और समुद्रमें होनेवाले सब प्रकारके कालिकादेबीके नामसे विख्यात हुई
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2803)
- **Original**: त़द्रन्तर शुप्घ निशु्णके धृत्य चण्ड-मुण्ड वहाँ आये और उन्होंने परम मनोहर रूप भारण करनेवाली अम्बिकादेवीकों देखा
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2804)
- **Original**: फिर ते शुम्भके पास जाकर बोले--' महाराज! एक अत्यन्त मनोहर स्त्री है, जो अपनी दिव्य कान्तिसे हिमालयको प्रकाशित कर रहीं है
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2805)
- **Original**: जैसा उत्तम रूप कहों किसोने भी नहों देखा होगा। असुरेश्चर। पता जलगाइये, वह देवी कौन हैं और उसे पकड़ लीजिये
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2806)
- **Original**: स्ल्रियोंमें तो बह रक्न है, उसका प्रत्येक अज्ज बहुत ही प्षुग्दर है तथा तरह अपने श्रोक्षज्ञोंकी प्रभासे सम्पूर्ण दिशाओँपें प्रकाश फैला रही है। दैत्ययाज़
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2807)
- **Original**: अभों वह ड्विपालदपर हो माजूद है, आप उसे देख सकते हैं
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2808)
- **Original**: प्रभो! तीनों लोकोमें माँध, हाथी और घोड़े आदि जितने भी रह हैं, वे सत इस समय आपके परमें शोभा पाते हैं
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2809)
- **Original**: हाथियोंपें 2+भूत ऐराबत, यह गास्जितका दृक्ष और यह उच्चै:श्षत। धौड़ा--यह सब आपने इद्धसे ले लिया है
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2810)
- **Original**: हंसोंसे जुता हुआ 4ह विमान भो आपके आगनपें शोभा पाता है। वह रत्रभूत अदभुत 'बिपान, जो पहले ब्रह्माजीके पास था, अब आपके यहाँ लाया गया है
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2811)
- **Original**: यह महापदा गामच्छ निधि आ5 कुबेरसे छोन लाये हैं। समुद्रने भी आपको क्लिल्किनी शारकी माली भेंट की है, जो केसरॉसे सुशोशित है और जिसके ऋमल कभी कुम्हलाते नहीं
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2812)
- **Original**: सुर्णकों वर्षा करनेवाज्ञा बरुणका छात्र भी आपके रल आपके भाई निशुम्भके अधिकारमें हैं। ऑनने भी श्वत: शुद्ध किवे हुए दो वस्त्र आपको सेकामें अर्पित किये हैं
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2813)
- **Original**: दैत्यराज ! इस प्रकार सभो रत्न आपने एकत्र कर लिये हैं। फिर जो यह स्त्रियोंपें रत्नकूप कल्याणमयी देवी है, इसे आप क्यों नहीं अपने अधिकारमें कर लेते 2
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2814)
- **Original**: ऋष्सकब 4 1021 $ निशब्बेत्रि वच्च: शुप्भ: से तदा चण्डमुण्डयो:। ग्रेषय्रामास सुम्रीव॑ दूते देव्या महासुरधू
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2815)
- **Original**: इति चेति चर वक्तव्या स्रा गत्वा वचनान्मम। यथाचाभ्येति सम्प्रीत्या तथा कार्य त्वया लघु
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2816)
- **Original**: स तन्न गत्या यप्नास्ते शैलोद्वेशे उतिशोभने। सा देबी ता ततः प्राह एलक्ष्णं मघुरचा गिरा।604
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2817)
- **Original**: ऋषि कहते हैं--
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2818)
- **Original**: चण्ड-मुण्डका यह वचन सुनकर शुम्भने महादैत्व सुग्रीबको दूत बनाकर देवोंके पास भेजा और कहा--' तुम मेरी आज्ञासे उसके सामने ये-ये बातें कहना और ऐसा उपाय करना जिससे प्रसन्न होकर वह शीघ्र ही बरहाँ आ जाव'
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2819)
- **Original**: 1502-103
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2820)
- **Original**: वह दूत पर्बतके अत्यन्त रमणीय प्रदेशमें, जहाँ देवों मौजूद थीं, गया और मधुर वाणीमें कोमल बचन बोला
- **Translation**: 

---

